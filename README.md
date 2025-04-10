# API de Gerenciamento de Tarefas (Desafio MandaTech)

Este projeto é uma API RESTful desenvolvida com **Flask + MongoDB**, estruturada no padrão **DDD (Domain-Driven Design)**.

Permite que usuários possam **criar, visualizar, atualizar e deletar tarefas**, com suporte a status, filtros, testes automatizados e documentação interativa utilizando Flasgger.

---

## Funcionalidades

- Criar nova tarefa
- Listar todas as tarefas
- Filtrar tarefas por status (`pending`, `in_progress`, `done`)
- Atualizar tarefa por ID (`{ "done": true }` ou `{ "in_progress": true }`)
- Deletar tarefa por ID
- Deletar **todas** as tarefas

---

## Estrutura de Pastas

Como dito foi utilizado uma estrutura de pastas no padrão DDD, a seguir uma explicação de cada pasta e arquivo utilizado.

```text
mandatech-challenge/
│
├── app/
│   ├── application/        # Camada de aplicação (serviços)
│   ├── infrastructure/     # Acesso ao banco MongoDB
│   ├── interfaces/         # Rotas (API)
│   ├── schemas/            # Schemas de validação com Pydantic
│   └── utils/              # Mensagens e constantes reutilizáveis
│
├── tests/                  # Testes automatizados com pytest
├── main.py                 # Arquivo principal da aplicação Flask
├── config.py               # Configuração (ex: URI do MongoDB)
├── requirements.txt        # Dependências
├── .env                    # Variáveis de ambiente (não versionar)
├── pytest.ini              # Configuração para pytest
└── README.md               # Este arquivo
```

# Como Executar ?

## 1. Clone o repositorio

```bash
git clone https://github.com/cauatn/mandatech-challenge.git
cd .\mandatech-challenge\
```

## 2. Crie um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

## 3. Instale as dependências

```bash
pip install -r requirements.txt
```

## 4. Configure o .env

```bash
python setup_env.py
```

## 5. Rode a aplicação

```bash
python main.py
```

# Documentação Swagger

Acesse a interface Swagger em:

```
http://localhost:5000/apidocs
```
