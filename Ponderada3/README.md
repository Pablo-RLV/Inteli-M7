# Deploy de modelo de Machine Learning

## Descrição do Projeto

O objetivo deste projeto é criar uma API para deploy de um modelo de Machine Learning. O dataset utilizado para o desenvolvimento está disponível em <https://www.kaggle.com/datasets/joebeachcapital/customer-segmentation>, e se trata de um dataset que apresenta a pontuação dos consumidores de um Shopping, a partir das informações de seus ganhos, sexo e idade. O modelo foi treinado utilizando AutoML da biblioteca PyCaret, e o deploy foi realizado utilizando a biblioteca FastAPI, com o frontend desenvolvido em HTML e CSS. A aplicação foi então Dockerizada para que possa ser executada em qualquer ambiente, inclusive, possibilitando a execução em nuvem.

## Pré-requisitos

Para executar o projeto, é necessário possuir o Docker instalado em sua máquina Após a instalação, é necessário clonar o repositório em sua máquina.

## Execução

Para executar o projeto, abra o terminal e navegue até a pasta onde o repositório foi clonado. Em seguida, será necessário clonar a imagem do Docker Hub, utilizando o comando:

```bash
docker pull pablorlv/ponderada3:0.0.1
```

(A imagem pode ser encontrada no seguinte [link](<https://hub.docker.com/repository/docker/pablorlv/ponderada3/general>)

Após a clonagem da imagem, execute o comando:

```bash
docker run -p 8000:8000 pablorlv/ponderada3:0.0.1
```

Em seguida, abra o navegador e acesse o endereço <http://localhost:8000/>. A aplicação será carregada e estará pronta para uso.

## Demonstração

A demonstração do funcionamento pode ser acessada no seguinte [link](<https://youtu.be/Rxeptgk9qhU>)

## Conclusão

A partir dessa atividade, foi possível entender melhor o funcionamento do deploy completo de um modelo preditivo, começando desde o tratamento dos dados, passando pelo treinamento do modelo, até o deploy da aplicação. Além disso, foi possível entender melhor o funcionamento do Docker, e como ele pode ser utilizado para facilitar o deploy de aplicações.

A partir dos outputs do modelo, é possível entender melhor o perfil dos clientes do shopping, e assim, criar estratégias de marketing mais eficientes, a fim de aumentar as vendas do shopping.
