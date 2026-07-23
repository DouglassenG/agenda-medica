
# 🏥 Agenda Medica

Aplicacao web para gerenciamento de agendamentos medicos, desenvolvida como desafio tecnico com Python e Flask.

---

## 📋 Sobre o Projeto

O sistema permite o login de um usuario e, apos a autenticacao, exibe os agendamentos medicos em uma tabela interativa com filtros e busca. Os dados de agendamentos sao consumidos via requisicao HTTP de uma API mock em servico separado.

---

## 🛠 Tecnologias Utilizadas

- **Backend:** Python 3.12, Flask 3.1, Werkzeug
- **Banco de Dados:** SQLite
- **Frontend:** HTML5, CSS3, Jinja2, Tabulator.js 6.3
- **HTTP Client:** Requests
- **Testes:** Pytest
- **Containerizacao:** Docker, Docker Compose
- **Gerenciamento de ambiente:** python-dotenv

---

## 📁 Estrutura do Projeto

```text
agenda-medica/
├── app/
│   ├── static/
│   │   └── style.css
│   ├── templates/
│   │   ├── login.html
│   │   └── agenda.html
│   ├── __init__.py
│   ├── auth.py
│   ├── models.py
│   └── api_client.py
├── api_mock/
│   └── server.py
├── public/
│   └── imagem-login.png
├── tests/
│   ├── __init__.py
│   ├── test_auth.py
│   └── test_api.py
├── .env.example
├── .gitignore
├── Dockerfile
├── Dockerfile.api
├── docker-compose.yml
├── requirements.txt
├── run.py
├── seed.py
└── README.md
```
---

## 🚀 Como Executar

### 🐳 Com Docker

```bash
docker-compose up --build
```

A aplicacao estara disponivel em `http://localhost:5000`.

### 💻 Sem Docker

**1. Criar e ativar o ambiente virtual:**

```bash
python -m venv venv

# Windows
.\venv\Scripts\Activate.ps1

# Linux/Mac
source venv/bin/activate
```

**2. Instalar dependencias:**

```bash
pip install -r requirements.txt
```

**3. Criar o banco e usuario de teste:**

```bash
python seed.py
```

**4. Iniciar a API mock (Terminal 1):**

```bash
python api_mock/server.py
```

**5. Iniciar a aplicacao (Terminal 2):**

```bash
python run.py
```

**6. Acessar no navegador:** `http://localhost:5000`

---

## 🔑 Credenciais de Teste

| Campo | Valor |
|-------|-------|
| Usuario | `admin` |
| E-mail | `admin@agenda.com` |
| Senha | `admin123` |

---

## 📖 Exemplos de Uso

1. Acesse `http://localhost:5000` e faca login com as credenciais acima
2. A tabela exibe todos os agendamentos disponiveis
3. Utilize o campo de busca para filtrar por **paciente**, **CPF** ou **medico**
4. Cada coluna possui um filtro individual no cabecalho da tabela
5. Clique em "Sair" para encerrar a sessao

---

## ✅ Testes Automatizados

O projeto possui **8 testes** cobrindo autenticacao e API:

```bash
pytest tests/ -v
```

🔐 **Testes de autenticacao (`test_auth.py`):**
- Login com credenciais validas
- Login com credenciais invalidas
- Login com campos vazios
- Logout

🌐 **Testes da API mock (`test_api.py`):**
- Listagem de todos os agendamentos
- Busca por nome de paciente
- Busca sem resultado
- Health check do servico

---

## ⚠️ Tratamento de Erros

A aplicacao trata os seguintes cenarios de forma controlada:

| Cenario | Comportamento |
|---------|---------------|
| Credenciais invalidas | Mensagem "Usuario ou senha invalidos" na tela de login |
| Campos vazios no login | Mensagem "Preencha todos os campos" |
| Nenhum agendamento encontrado | Mensagem "Nenhum registro encontrado" na tabela |
| API indisponivel | Mensagem "Servico de agendamentos indisponivel" |
| Timeout da API | Mensagem "Servico demorou para responder" |
| Resposta invalida da API | Mensagem "Resposta da API em formato invalido" |
| Erro de conexao com o banco | Mensagem "Erro interno" + log no servidor |

Todas as falhas sao registradas via `logging` para facilitar a identificacao da causa.

---

## 🧠 Decisoes Tecnicas

- **Flask Factory Pattern (`create_app`):** permite criar instancias isoladas da aplicacao para testes, evitando estado compartilhado entre execucoes
- **API Mock como servico separado:** simula um cenario real onde o backend consome dados de outro servico via HTTP, rodando na porta 5001
- **Client HTTP com tratamento de excecoes:** o arquivo `api_client.py` trata `ConnectionError`, `Timeout`, `HTTPError` e respostas em formato inesperado, retornando mensagens amigaveis ao usuario
- **Tabulator.js via CDN:** evita necessidade de build no frontend, mantendo o projeto simples e facil de executar
- **SQLite:** banco leve, sem necessidade de servidor externo, ideal para o escopo do desafio
- **Werkzeug para hash de senha:** gera hash seguro com `generate_password_hash` e valida com `check_password_hash`, sem dependencia extra alem do Flask
- **Seed idempotente:** o script `seed.py` pode ser executado varias vezes sem duplicar dados

---

## 🔒 Variaveis de Ambiente

| Variavel | Descricao | Valor padrao |
|----------|-----------|--------------|
| `SECRET_KEY` | Chave secreta do Flask para sessions | `dev-secret-key` |
| `DATABASE_PATH` | Caminho do arquivo SQLite | `database.db` |
| `API_URL` | URL da API mock | `http://localhost:5001` |

---

## 📌 Limitacoes Conhecidas

- Autenticacao baseada em session do Flask (sem JWT)
- Dados de agendamentos mockados em memoria (nao persistidos em banco)
- Sem paginacao na tabela (adequado para o volume de dados do desafio)
- SQLite nao recomendado para ambientes de alta concorrencia

---

Desenvolvido por **Douglas** como desafio tecnico. 🚀
