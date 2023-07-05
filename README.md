# Model API

## Pré-requisitos

- Python 3.x
- MySQL (MariaDB 10.4)

## Instalação

1. Clone o repositório:
`git clone https://github.com/hsfreitas92/model-api.git`

2. Acesse a pasta do projeto:
`cd seu-projeto`

2. Config Ambiente:
- Crie e ative um ambiente virtual (opcional):
  `python3 -m venv venv`
  `source venv/bin/activate`
- Configure as informações de ambiente de dev ou prod no arquivo `wsgi.py`.

4. Instale as dependências:
`pip install -r requirements.txt`

5. Configuração do Banco de Dados:

- Configure as informações do banco de dados no arquivo `config.py` localizado na raiz do projeto.
- Certifique-se de que o MySQL esteja configurado corretamente e acessível.
- Deve ser apontado para o banco atual(teste local) da nortech, criado pela aplicacao via migration.

6. Execute a aplicação:
`set FLASK_APP=app`
`flask run`

A aplicação será executada na URL `http://localhost:5000`.

## Endpoints

- `GET /users`: Retorna todos os usuários cadastrados.
- `POST /users`: Cria um novo usuário.
- `GET /users/{id}`: Retorna um usuário específico com base no ID fornecido.
