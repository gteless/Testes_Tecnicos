# 🤖 RPA001 - Automação de Busca de Produtos Amazon

Este projeto é um robô de RPA (Robotic Process Automation) desenvolvido em **Python** utilizando **Selenium**. A solução automatiza o fluxo completo de pesquisa de mercado na Amazon Brasil: desde a autenticação segura até o envio de relatórios estruturados por e-mail.

## 🚀 Funcionalidades

- **Autenticação Segura:** Login automatizado com credenciais protegidas via variáveis de ambiente (`.env`).
- **Busca Dinâmica:** Pesquisa de produtos baseada no input em tempo real do utilizador.
- **Data Scraping Avançado:** Extração robusta de títulos e preços (incluindo frações) da primeira página de resultados.
- **Relatórios Estruturados:** Geração automática de ficheiro CSV formatado para leitura direta no Excel (UTF-16 + `;`).
- **Notificação SMTP:** Envio do relatório em anexo utilizando **SMTP_SSL** com senhas de aplicação do Google.
- **Dual Mode:** Suporte para execução **Visual** (debug) e **Headless** (produção/background).

## 📁 Estrutura do Projeto

```text
RPA001_BuscaProdutosAmazon/
├── log/                # Logs técnicos de execução
├── output/             # Destino dos ficheiros CSV gerados
├── src/                # Módulo de lógica e funções auxiliares
├── .env                # Credenciais sensíveis (não versionado)
├── .gitignore          # Definições de exclusão do Git
├── main.py             # Orquestrador principal do robô
└── requirements.txt    # Dependências do projeto


🛠️ Pré-requisitos
Python 3.10+

Google Chrome instalado.

App Password do Gmail (para envio de e-mails).

⚙️ Instalação e Configuração
Clonar o Repositório:

Bash
git clone [https://github.com/gteless/Testes_Tecnicos.git](https://github.com/gteless/Testes_Tecnicos.git)
cd RPA001_BuscaProdutosAmazon
Configurar Ambiente Virtual (venv):

Bash
python -m venv venv
# Ativar no Windows:
.\venv\Scripts\activate
Instalar Dependências:

Bash
pip install -r requirements.txt
Variáveis de Ambiente:
Cria um ficheiro .env na raiz com o seguinte formato:

Snippet de código
AMAZON_EMAIL=teu_email@exemplo.com
AMAZON_PASSWORD=tua_senha_amazon
EMAIL_FROM=teu_gmail@gmail.com
EMAIL_PASSWORD=tua_senha_de_app_16_digitos
🚀 Como Executar
Para iniciar a automação, corre o seguinte comando:

Bash
python main.py
