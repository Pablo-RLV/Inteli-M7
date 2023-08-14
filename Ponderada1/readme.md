# Criando o ambiente para a execução de uma aplicação containerizada

## 1. Instalação do Docker

### 1.1. Instalação do Docker no Ubuntu 22.04 LTS

#### 1.1.1. Atualização dos pacotes

```bash
sudo apt update
```

#### 1.1.2. Instalação dos pacotes necessários para a instalação do Docker

```bash
sudo apt install apt-transport-https ca-certificates curl software-properties-common
```

#### 1.1.3. Adição da chave GPG oficial do Docker

```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

#### 1.1.4. Adição do repositório estável do Docker

```bash
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
```

#### 1.1.5. Atualização dos pacotes

```bash
sudo apt update
```

#### 1.1.6. Instalação do Docker

```bash
sudo apt install docker-ce
```

## 2. Estrutura do projeto

### 2.1. Estrutura de diretórios

```bash
.
├── index.php
├── Dockerfile
├── README.md
```

### 2.2. Descrição dos diretórios

| Diretório | Descrição |
| --- | --- |
| index.php | Arquivo PHP que será executado pelo container |
| Dockerfile | Arquivo que contém as instruções para a criação da imagem do container |
| README.md | Arquivo que contém a documentação do projeto |

## 3. Utilização da imagem do container

O link para a imagem do container no Docker Hub é: <https://hub.docker.com/r/pablorlv/curriculo-php>

### 3.1. Pull da imagem do container

```bash
docker pull pablorlv/curriculo-php:0.0.1
```

### 3.2. Execução da imagem do container

```bash
docker run -d -p 80:80 pablorlv/curriculo-php:0.0.1
```

A partir desse momento, a aplicação estará disponível no endereço <http://localhost>.

## 4. Conclusão

O projeto foi criado com sucesso e a imagem do container foi disponibilizada no Docker Hub, o que permite a qualquer pessoa acessar essa imagem independentemente da sua máquina. Logo, é possível perceber a importância da utilização de containers para a execução de aplicações, pois, além de facilitar a execução da aplicação, também facilita a disponibilização da aplicação para outras pessoas.
