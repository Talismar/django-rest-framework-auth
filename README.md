# Django Rest Framework API

Este projeto é uma API simples para um blog desenvolvida usando Django Rest Framework (DRF). O foco desse projeto é passar para a comunidade como fazer um sistema de autenticação e autorização usando JWT.

## Funcionalidades

- Autenticação de usuários
- CRUD de artigos
- Permissões baseadas em autenticação para endpoints de artigos

## Pré-requisitos

- Python 3.x
- Django
- Django Rest Framework
- Django Rest Framework Simple JWT

## Instalação

### 1. Clone o repositório:

```sh
git clone https://github.com/Talismar/django-rest-framework-auth
```

### 2. Instale as dependências:


```sh
pip install -r requirements.txt
```


### 3. Execute as migrações do banco de dados:

```sh
python manage.py migrate
```

### 4. Inicie o servidor de desenvolvimento:

```sh
python manage.py runserver
```

### 5. Acesse a API em `http://localhost:8000/`.

## Endpoints

### Autenticação

- `POST /api/token/`: Obtém um token de acesso JWT para autenticação.

### Artigos

- `GET /api/article/`: Lista todos os artigos.
- `GET /api/article/{id}/`: Obtém detalhes de um artigo específico.
- `POST /api/article/`: Cria um novo artigo (requer autenticação).
- `PUT /api/article/{id}/`: Atualiza um artigo existente (requer autenticação).
- `DELETE /api/article/{id}/`: Deleta um artigo existente (requer autenticação).

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir um pull request ou reportar issues.

## Autor

Talismar - [GitHub](https://github.com/Talismar)

## Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
