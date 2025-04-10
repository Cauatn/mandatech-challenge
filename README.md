# API de Gerenciamento de Tarefas (Desafio MandaTech)

Este projeto é uma API RESTful desenvolvida com **Flask + MongoDB**, estruturada no padrão **DDD (Domain-Driven Design)**.

Permite que usuários possam **criar, visualizar, atualizar e deletar tarefas**, com suporte a status, filtros, testes automatizados e documentação interativa utilizando Flasgger.

## Rodando com Docker  🐳

Caso o fast link não funciona está no rodape do read.me as instruções.
[Clique aqui para o uso com Docker](#como-executar-com-docker)

## Funcionalidades

- Criar nova tarefa
- Listar todas as tarefas
- Filtrar tarefas por status (`pending`, `in_progress`, `done`)
- Atualizar tarefa por ID (`{ "done": true }` ou `{ "in_progress": true }`)
- Deletar tarefa por ID
- Deletar **todas** as tarefas

---

## Estrutura de pastas

```text
mandatech-challenge/
│
├── app/                        # Código principal da aplicação
│   ├── domain/                 # Camada de domínio (regras de negócio)
│   │   ├── repositories/       # Acesso ao banco de dados (MongoDB)
│   │   │   └── mongo_repository.py
│   │   ├── schemas/            # Schemas de validação com Pydantic
│   │   │   └── task_schema.py
│   │   └── services/           # Lógica de negócio (use cases)
│   │       ├── tasks/          # Funções específicas por entidade
│   │       └── task_service.py
│   │
│   ├── interfaces/             # Camada de apresentação (rotas/controllers)
│   │   └── controllers/        # Endpoints REST
│   │
│   └── utils/                  # Utilitários e mensagens reutilizáveis
│       ├── messages.py         # Mensagens fixas da aplicação
│       └── swagger_docs/       # Documentação Swagger por endpoint
│
├── tests/                      # Testes automatizados (Pytest)
│   ├── test_routes.py
│   └── test_service.py
│
├── venv/                       # Ambiente virtual Python (não versionar)
│
├── .env                        # Variáveis de ambiente (config local)
├── .gitignore                  # Arquivos e pastas ignoradas pelo Git
├── config.py                   # Configurações globais (ex: URI do MongoDB)
├── main.py                     # Ponto de entrada da aplicação Flask
├── pytest.ini                  # Configuração do Pytest
├── requirements.txt            # Dependências
└── README.md                   # Este arquivo
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

Por favor, coloque as credenciais do MONGODB no arquivo .env, caso queira o banco de testes, enviei via E-mail.

```bash
python setup_env.py
```

## 5. Rode a aplicação

```bash
python main.py
```

## 6. Acesse ela em:

A Api pode ser verificada com POSTMAN ou soluções alternativas em:

```
http://localhost:5000/tasks
```

# Documentação Swagger

Acesse a interface Swagger em, para fazer as requisições ou simplismente validar todas as rotas, como não existe login, não será necessario nenhuma chave JWT para que funcione o app:

```
http://localhost:5000/apidocs
```
<a name="como-executar-com-docker"></a>
## Como Executar com Docker

1. **Crie o arquivo `.env`** (ou use o `setup_env.py`):

Por favor, setar corrretamente as variaveis de ambiente.

```bash
python setup_env.py
```

2. Construa e suba os containers:

```bash
docker-compose up --build
```

Acesse normalmente a aplicação:

API: http://localhost:5000/tasks
Swagger: http://localhost:5000/apidocs
