# Aplicação que realiza CRUD com rotas protegidas por autenticação JWT

## Objetivo

O objetivo deste projeto é criar uma aplicação que realize um CRUD em um bloco de anotações, que só pode ser utilizado por usuários autenticados. Para isso, foi utilizado o framework Flask, da linguagem Python, e o banco de dados foi criado a partir do SQLAlchemy. Posteriormente, foi implementado o JWT para autenticação dos usuários, utilizando a biblioteca Flask-JWT-Extended.

Essa aplicação foi então containerizada utilizando o Docker, e as imagens foram enviadas para o Docker Hub. Como arquitetura, foi escolhida a separação da aplicação em dois containers: um para o banco de dados e outro para a aplicação em si. Para a comunicação entre os containers, foi utilizado o Docker Compose.

## Como utilizar

Para utilizar a solução de forma local, é necessário ter o Docker e o Docker Compose instalados. Após isso, basta clonar o repositório e executar o comando `docker-compose up` na pasta raiz do projeto. A aplicação estará disponível em `localhost:5000`.

## Rotas

A aplicação possui as seguintes rotas:

- `/` (GET): Retorna a tela de login.
- '/' (POST): Realiza o login do usuário.

A partir daqui, todas as rotas necessitam de autenticação.

- '/read' (GET): Retorna a tela com as anotações do usuário.
- '/create' (GET): Retorna a tela para criação de uma nova anotação.
- '/create' (POST): Cria uma nova anotação.
- '/update/{id}' (GET): Retorna a tela para edição de uma anotação.
- '/update/{id}' (POST): Edita uma anotação.
- '/delete/{id}' (GET): Deleta uma anotação.
