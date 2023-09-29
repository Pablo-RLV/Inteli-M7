# Deploy de uma aplicação de bloco de notas na AWS

## Arquitetura da solução

Esse projeto consiste em uma integração entre um frontend em Vanilla JS, um backend em FastAPI e um banco de dados em Postgres

## Tecnologias utilizadas

Para cada um dos elementos principais que compõem a arquitetura da solução, foi feita a separação através das tecnologias da AWS. O backend foi alocado para ser executado por um EC2, que seria responsável por atender às chamadas da API. O banco de dados foi alocado no RDS, uma tecnologia que permite a utilização de bancos de dados relacionais na AWS. Por sua vez, o frontend também foi alocado em um EC2, mas sendo renderizado via Apache.

Para a confirmação de funcionamento do banco de dados, foi utilizado o software DBeaver, que possibilita a conexão e visualização com bancos de dados. O momento de confirmação do funcionamento está representado abaixo:

<img src="./media/Captura de tela 2023-09-29 151757.png">

O template para o desenvolvimento da solução está disponível no seguinte repositório <https://github.com/Murilo-ZC/Avaliacao-P2-M7-2023-EC/tree/main>. A principal tarefa da avaliação foi a utilização das tecnologias da AWS para a alocação desses recursos e a sua comunicação.

## Segurança

Como a questão de segurança não era um requisito essencial para a avaliação, o acesso ao banco de dados foi permitido somente com o nome de usuário e senha, e as máquinas do EC2 não foram cadastradas com chave de acesso. Devido ao aluno estar enfrentando algumas dificuldades com o cadastro de grupos de segurança durante a avaliação, foi liberado todo tráfego em todas as portas, para que esse não fosse um impeditivo para a continuidade da aplicação.

Entretanto, é importante salientar que em situações de produção, essas práticas não podem ser empregadas, já que a aplicação estaria extremamente vulnerável a ataques de terceiros.

## Alterações realizadas

Nossas principais alterações foram a substituição das strings de conexão entre as aplicações, que deveriam ser substuídas por aquelas que criamos.

As alterações para conexão da API com o banco de dados estão representadas a seguir:

<img src="./media/Captura de tela 2023-09-29 161136.png">

Por sua vez, as alterações para conexão do frontend com a API estão representadas a seguir:

<img src="./media/Captura de tela 2023-09-29 161353.png">

## Demonstração de funcionamento

Para a utilização da solução, bastou acessar o seguinte endereço: <http://44.211.149.167/>. A partir desse momento, a seguinte tela era disponibilizada ao usuário:

<img src="./media/Captura de tela 2023-09-29 162451.png">

Quando o usuário cria ou exclui alguma nota, pressionando o botão do frontend, automaticamente essa mensagem é enviada para a outra máquina EC2, onde está localizado o backend es FastAPI. Após isso, o backend se comunica com o banco de dados e realiza a operação desejada. Como o frontend possui JavaScript em sua aplicação, sempre que algo é alterado no banco de dados, as novas informações ficam visíveis ao usuário, pois esse backend está "ouvindo" o database.

Entretanto, é preciso analisar também que, por se tratar de uma aplicação presente em diversos "locais", o delay de trânsito das informações começa a ser relevante, pois os dados precisam fazer longos trajetos dentro da AWS antes de chegar ao usuário. Por se tratar de uma aplicação simples, não há problema algum, mas caso milhares de usuários fizerem seu uso, além de algumas funcionalidades de querys mais complexas sejam empregadas, pode ser que essa solução tenha que ser reavaliada para atender melhor as demandas que o negócio exige.

### Itens de demonstração de funcionamento

<img src="./media/Captura de tela 2023-09-29 155746.png">
Construção das duas instâncias de EC2

<img src="./media/Captura de tela 2023-09-29 152806.png">
Confirmação da construção das tabelas no banco de dados

<img src="./media/Captura de tela 2023-09-29 154016.png">
Funcionamento da API do backend

<img src="./media/Captura de tela 2023-09-29 154622.png">
Funcionamento do frontend Apache
