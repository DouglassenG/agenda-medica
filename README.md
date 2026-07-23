# Agenda Medica

Aplicacao web para gerenciamento de agendamentos medicos, desenvolvida com Python e Flask.

## Tecnologias

- Python 3.12
- Flask 3.1
- SQLite
- Tabulator.js 6.3
- Docker / Docker Compose
- Pytest

## Como executar com Docker

```bash
docker-compose up --build
```

Acesse `http://localhost:5000` no navegador.

## Como executar sem Docker

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1       # Windows
source venv/bin/activate           # Linux/Mac

pip install -r requirements.txt
python seed.py
```

Em um terminal, inicie a API mock:

```bash
python api_mock/server.py
```

Em outro terminal, inicie a aplicacao:

```bash
python run.py
```

Acesse `http://localhost:5000`.

## Credenciais de teste

- **Usuario:** admin
- **Senha:** admin123

## Exemplos de uso

1. Faca login com as credenciais acima
2. A tabela exibe todos os agendamentos
3. Use o campo de busca para filtrar por paciente, CPF ou medico
4. Cada coluna possui filtro individual no cabecalho

## Testes

```bash
pytest tests/ -v
```

## Decisoes tecnicas

- **Flask Factory Pattern:** permite criar instancias isoladas da app para testes
- **API Mock como servico separado:** simula um cenario real onde o backend consome dados de outro servico via HTTP
- **Tabulator.js via CDN:** evita build de frontend, mantendo o projeto simples
- **SQLite:** banco leve e sem necessidade de servidor externo, ideal para o escopo do desafio
- **Client HTTP com tratamento de erros:** cobre conexao recusada, timeout, resposta invalida e erro HTTP

## Limitacoes conhecidas

- Autenticacao por session (sem JWT)
- Dados de agendamentos mockados (nao persistidos em banco)
- Sem paginacao na tabela (adequado para o volume de dados do desafio)