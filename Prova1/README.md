# Avaliações-M7-Inteli

Esse repositório corresponde à primeira prova do sétimo módulo do Inteli, cujo conteúdo da avaliação corresponde à utilização dos conceitos de conteinerização para criar dois containeres que sejam capazes de carregar o backend (em Python), e um frontend (em JavaScript).

Para essa aplicação, foram criados dois Dockerfile's, cada um em suas respectivas pastas da aplicação, e uma composição entre os conteineres, formada pelo arquivo docker-compose.yml, responsável por comunicar o front e o backend.

O Dockerfile do backend segue a seguinte estrutura:

    FROM python 
    #responsável por importar a imagem do python

    WORKDIR /app
    #cria o diretório do projeto

    COPY . /app
    #copia os arquivos da pasta local para o diretório criado

    RUN pip install -r requirements.txt
    #instala as bibliotecas necessárias

    EXPOSE 8000
    #expõe a porta 8000

    CMD python main.py
    #executa a aplicação

O Dockerfile do frontend segue a seguinte estrutura:

    FROM node:18
    #importa a imagem do node

    WORKDIR /usr/src/app
    #cria o diretório do projeto

    COPY package*.json ./
    #copia o package.json para o diretório criado

    RUN npm install
    #instala os requerimentos

    COPY . .
    #copia os demais arquivos do projeto

    EXPOSE 3000
    #expõe a porta 3000

    CMD [ "node", "server.js" ]
    #executa a aplicação

DockerHub backend: <https://hub.docker.com/repository/docker/pablorlv/python_prova/general>
DockerHub frontend: <https://hub.docker.com/repository/docker/pablorlv/js_prova/general>

A estrutura do docker-compose se encontra abaixo:

    version: '3.1'
    #versão do compose

    services:

    python:
        image: pablorlv/python_prova:0.0.1 #apresenta a imagem a ser utilizada
        ports:
        - 8000:8000 #mapeia as portas
        depends_on:
        - js #apresenta as dependências
        container_name: python_prova #define o nome do container

    js:
        image: pablorlv/js_prova:0.0.1 #apresenta a imagem a ser utilizada
        ports:
        - 3000:3000 #mapeia as portas
        container_name: js_prova #define o nome do container

Para executar a solução, basta clonar esse repositório, navegar até a pasta principal do projeto e utilizar o comando:

    docker-compose-up

A partir disso, a solução começará a ser renderizada e então será possível acessá-la através de localhost.
