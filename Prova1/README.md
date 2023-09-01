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
