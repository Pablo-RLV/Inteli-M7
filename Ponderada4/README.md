# Deploy de modelo de Machine Learning

## Descrição do Projeto

O objetivo deste projeto é criar o deploy do dashboard de um modelo de Machine Learning. O dataset utilizado para o desenvolvimento está disponível em <https://www.kaggle.com/datasets/joebeachcapital/customer-segmentation>, e se trata de um dataset que apresenta a pontuação dos consumidores de um Shopping, a partir das informações de seus ganhos, sexo e idade. O modelo foi treinado utilizando AutoML da biblioteca PyCaret, e o deploy foi realizado utilizando a biblioteca FastAPI, com o frontend desenvolvido em HTML e CSS, e o dashboard formado pela biblioteca Matplotlib. A aplicação foi então Dockerizada para que possa ser executada em qualquer ambiente, inclusive, na nuvem AWS.

## Arquitetura AWS

Para esse projeto, foi criado um ambiente na AWS, utilizando o serviço EC2, que aloca uma máquina virtual na nuvem. A máquina virtual utilizada foi a t2.micro, que se trata de uma máquina de baixo custo, com 1 vCPU e 1GB de memória RAM. A máquina virtual foi criada utilizando o sistema operacional Ubuntu 22.04.2 LTS.

Após a criação da máquina virtual, foi necessário atualizar as dependências e instalar os novos pacotes, além do Docker. Após isso, foi necessário clonar o repositório do projeto para posteriormente executar a aplicação.

Como o quesito de segurança não foi um ponto relevante para essa atividade, o tráfego de dados foi realizado utilizando o protocolo HTTP, e não o HTTPS. Além disso, todas as portas foram liberadas para acesso externo, o que não é recomendado para ambientes de produção.

## Execução

Para executar a aplicação, é necessário navegar até a pasta do projeto, e posteriormente executar o seguinte comando:

```bash
docker-compose up --build
```

Em seguida, abra o navegador e acesse a porta 8000 da máquina virtual. A aplicação deve estar disponível para uso.

(As imagens utilizadas podem ser encontradas no seguinte [link](<https://hub.docker.com/u/pablorlv>))

## Demonstração

O vídeo de demonstração de execução da aplicação está disponível no seguinte [link](<https://youtu.be/zPrpcYPTaQY>).

## Conclusão

A partir dessa atividade, foi possível entender melhor o funcionamento do deploy completo de um modelo preditivo, começando desde o tratamento dos dados, passando pelo treinamento do modelo, até o deploy da aplicação na AWS, integrada a uma visualização de dados.

A partir dos outputs do modelo, é possível entender melhor o perfil dos clientes do shopping, e assim, criar estratégias de marketing mais eficientes, a fim de aumentar as vendas do shopping.
