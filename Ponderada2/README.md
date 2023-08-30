# Aplicação que realiza CRUD com rotas protegidas por autenticação JWT

## Objetivo

O objetivo deste projeto é criar uma aplicação que realize um CRUD em um bloco de anotações, que só pode ser utilizado por usuários autenticados. Para isso, foi utilizado o framework Flask, da linguagem Python, e o banco de dados foi criado a partir do SQLAlchemy. Posteriormente, foi implementado o JWT para autenticação dos usuários, utilizando a biblioteca Flask-JWT-Extended.

Essa aplicação foi então containerizada utilizando o Docker, e as imagens foram enviadas para o Docker Hub. Como arquitetura, foi escolhida a separação da aplicação em dois containers: um para o banco de dados e outro para a aplicação em si. Para a comunicação entre os containers, foi utilizado o Docker Compose.

## Rotas

A aplicação possui as seguintes rotas:

- `/` (GET): Retorna a tela de login.
- `/` (POST): Realiza o login do usuário.

A partir daqui, todas as rotas necessitam de autenticação.

- `/read` (GET): Retorna a tela com as anotações do usuário.
- `/create` (GET): Retorna a tela para criação de uma nova anotação.
- `/create` (POST): Cria uma nova anotação.
- `/update/{id}` (GET): Retorna a tela para edição de uma anotação.
- `/update/{id}` (POST): Edita uma anotação.
- `/delete/{id}` (GET): Deleta uma anotação.

## Como utilizar

Para executar a aplicação, siga os seguintes passos:

- Certifique-se de ter o Docker e o Docker Compose instalados em sua máquina.
- Faça o clone da imagem do Docker Hub do backend com o comando `docker pull pablrlv/api:latest`. O link para o repositório é <https://hub.docker.com/repository/docker/pablorlv/api/general>
- Faça o clone da imagem do Docker Hub do banco de dados com o comando `docker pull pablrlv/db:latest`. O link para o repositório é <https://hub.docker.com/repository/docker/pablorlv/db/general>
- Acesse a pasta do projeto e execute o comando `docker-compose up`
- Acesse <http://localhost:5000> para acessar a aplicação.

## Autenticação

O usuário cadastrado para testes é:
Usuário: `pablo`
Senha: `pablo`

## Demonstração

O vídeo de demonstração do funcionamento da aplicação está disponível em: <https://youtu.be/M6h-nZsfkKI>
