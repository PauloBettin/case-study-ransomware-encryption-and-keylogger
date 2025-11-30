# ============================================================
# Estudo de Caso: Criptografia de Arquivos em Cenários de Backup/Ransomware
# ============================================================
# Este script é parte de um laboratório acadêmico. Ele demonstra como
# arquivos podem ser descriptigrafados com Python e como a chave pode ser validada. NÃO deve ser usado em produção.
# ============================================================

#Carrega Bibliotecas
from cryptography.fernet import Fernet, InvalidToken
import os
import base64
import tempfile
import shutil

#Carrega chave de descriptografia (Foi baixada do e-mail)
def carregar_chave(nome_arquivo="chave.key"):
    with open(nome_arquivo, "rb") as file:
        return file.read()

#Descriptografa um único arquivo
def descriptografar_arquivo(caminho, chave):
    f = Fernet(chave)
    try:
        with open(caminho, "rb") as file:
            dados_cript = file.read()

        dados = f.decrypt(dados_cript)

        # Escreve com segurança APÓS sucesso
        dir_ = os.path.dirname(caminho) or "."
        fd, tmp_path = tempfile.mkstemp(dir=dir_)
        try:
            with os.fdopen(fd, "wb") as tmp:
                tmp.write(dados)
            shutil.move(tmp_path, caminho)
        except Exception:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)
            raise

        print(f"🔓 Restaurado: {caminho}")

    except InvalidToken:
        print(f"❌ Chave incorreta ou arquivo não corresponde à chave: {caminho}")
    except Exception as e:
        print(f"❌ Erro ao descriptografar {caminho}: {e}")

#Encontra arquivos para descriptografar
def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if not nome.endswith(".py") and not nome.endswith(".key"):
                lista.append(caminho)
    return lista

#Execução principal
def main():
    # ATENÇÃO: use o MESMO arquivo de chave da cifragem.
    # Se a chave foi salva como "HOST-USUARIO.key", ajuste aqui:
    chave = carregar_chave("chave.key")

    diretorios = [
        os.getcwd(),               # pasta de execução
        # r"C:\LabSecurity\backup",
        # r"D:\OutrosArquivos",
    ]

    for diretorio in diretorios:
        print(f"\n📂 Processando diretório: {diretorio}")
        arquivos = encontrar_arquivos(diretorio)
        if not arquivos:
            print("ℹ️ Nenhum arquivo encontrado para descriptografia.")
        else:
            for arquivo in arquivos:
                descriptografar_arquivo(arquivo, chave)

    print("\n✅ Processo concluído.")

if __name__ == "__main__":
    main()
