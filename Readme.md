# Estudo de Caso: Criptografia de Arquivos para Backup e Proteção contra Ransomware

Este repositório contém um **script em Python** que demonstra como arquivos podem ser criptografados utilizando a biblioteca `cryptography.fernet`.  
O objetivo é **científico e educacional**, servindo como estudo de caso sobre:
- Técnicas de proteção de dados contra acesso não autorizado.
- Simulação de cenários de ransomware para fins de pesquisa.
- Estratégias de backup seguro com criptografia.

---

## ⚠️ Disclaimer (Português)

Este código é fornecido **exclusivamente para fins acadêmicos e de estudo**.  
Não deve ser utilizado em ambientes de produção, nem para fins maliciosos.  
O autor não se responsabiliza por qualquer uso indevido.  

Este projeto busca **conscientizar** sobre:
- Como ransomware pode atuar criptografando arquivos.
- A importância de **mitigação** através de backups seguros e gestão de chaves.

---

## ⚠️ Disclaimer (English)

This code is provided **strictly for academic and research purposes**.  
It must **not** be used in production environments or for malicious intent.  
The author takes no responsibility for misuse.  

This project aims to **raise awareness** about:
- How ransomware operates by encrypting files.
- The importance of **mitigation** through secure backups and key management.

---

## 🧪 Metodologia /  Methodology

Este estudo foi conduzido em ambiente de laboratório, com o objetivo de simular o funcionamento de ferramentas de criptografia em cenários de **backup seguro** e **ransomware**.  

### Etapas do experimento

1. **Definição do ambiente de teste**  
   - Criação de diretórios específicos contendo arquivos de exemplo (textos, imagens simples).  
   - Garantia de que nenhum arquivo de produção ou pessoal fosse utilizado.  

2. **Geração da chave de criptografia**  
   - A chave é criada dinamicamente com base no computador e usuário.  
   - É enviada por e‑mail para simular um fluxo de armazenamento externo.  
   - O arquivo local da chave é removido após o envio, mantendo apenas a versão em memória durante a execução.  

3. **Criptografia dos arquivos**  
   - Cada arquivo é lido e criptografado com a chave Fernet.  
   - O conteúdo original é sobrescrito com a versão criptografada.  
   - Um arquivo de mensagem (“Leia.txt”) é gerado para indicar que os dados foram protegidos.  

4. **Validação do processo**  
   - Verificação de que todos os arquivos foram alterados.  
   - Testes de recuperação utilizando a chave recebida por e‑mail.  

### Considerações éticas

- O código **não deve ser usado em ambientes reais** para criptografar dados de terceiros.  
- O propósito é **educacional e científico**, demonstrando como ataques de ransomware funcionam e como backups criptografados podem ser implementados.  

### Mitigação e boas práticas

- **Backups offline e em nuvem**: manter cópias redundantes fora do alcance de ataques.  
- **Gestão de chaves**: utilizar cofres digitais para armazenar chaves de forma segura.  
- **Monitoramento de comportamento**: detectar processos que tentam criptografar grandes volumes de arquivos.  
- **Treinamento de usuários**: reduzir riscos de infecção por phishing e engenharia social.  
- **Testes periódicos de restauração**: garantir que backups possam ser recuperados em caso de incidente.  

---

## 🔐 Sugestões de Mitigação / Mitigation and best practices

Para lidar com riscos de ransomware e proteger dados críticos:

- **Backups regulares**: mantenha cópias offline e em nuvem.
- **Gestão de chaves**: nunca perca a chave de criptografia; use cofres digitais (ex.: HashiCorp Vault).
- **Monitoramento de rede**: detecte comportamentos suspeitos de criptografia em massa.
- **Educação de usuários**: conscientização sobre phishing e boas práticas de segurança.
- **Testes de recuperação**: valide periodicamente se backups podem ser restaurados.
- **Ferramentas de zero trust**: a exemplo o Treathlocker, dificultando a execução de programas desconhecidos no perfil do usuário.

---
