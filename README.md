Gerenciador de tarefas de usuários

Este projeto consiste na simulação de um sistema simples de visualização de tarefas de usuários. Realizam-se operações CRUD em uma API Rest. O sistema foi construído utilizando o framework Django em Python e o banco de dados em postgresql. Foi utilizado, como container da aplicação o Docker.

A versão do sistema em produção pode ser conferida abaixo. 

https://sm-usertask.herokuapp.com/
 
### API REST
Utilizou-se para criação de uma API Rest a biblioteca: “rest_framework”, que incorpora as principais funcionalidade de uma api, utilizando como base a estrutura do Django. 

### INTERFACE

Para o front-end, utilizou-se basicamente a biblioteca bootstrap, utilizando um template padrão que é parametrido de acordo com a entidade a ser tratada: usuário ou tarefa.

Já para as funções de tratamento dos formulários utilizou-se AJAX, chamando a API através de funções em Jquery.

### MODELO DE DADOS

Existem duas estruturas de dados principais: usuários e tarefas. Cada usuário é identificado pelo seu nome e possui, associado a ele, um conjunto de tarefas, as quais possuem uma descrição e um status, que pode ser: feito e pendente.


### TESTES
Para executarmos os testes, devemos acessar via terminal no diretório raiz os seguintes comandos:

```
docker exec -it usertasks-django-crud_web_1 bash
```

```
python3 manage.py test
```

As duas principais categorias de testes utilizadas implentadas foram os testes de modelo e de visão. Nos testes de modelo, verificamos a conformidade das características dos campos presentes nas estruturas de dados, como tamanho, bem como restrições, como o efeito cascata na remoção. 

Já nos testes de visão, adentramos nas diversas possibilidade de alterações no banco de dados via interface, são elas:

- Criação de usuário;
- Criação de tarefa;
- Recuperação de todos os usuários;
- Recuperação de todas as tarefas de um usuário;
- Edição de status de uma tarefa;
- Remoção de usuário;
- Remoção de tarefa.

Nesses testes, conferimos os dados retornados pelas views, utilizando como base de comparação a aplicação das operações diretamente no banco de dados. Também se o código html retornado reflete a operação realizada, exemplos: "200" para recuperação de dados e "201" para criação.

### INSTALAÇÃO
 
Para acessar o sistema é preciso ter instalado na máquina os seguintes serviços: 
- Docker
- Docker Compose

Posteriormente, deve-se clonar o repositório em:

``` 
$ git clone https://github.com/gabrielmrp/usertasks-django-crud.git
```

Entre na pasta do sistema:

```
$ cd usertasks-django-crud
```

Faça a instalação do sistema através do comando abaixo:
  
```  
$ docker-compose up --build
```

O comando abaixo deve ser acionado para realizar a migração do banco de dados:

```
$ docker-compose run web python3 manage.py migrate
```

Acesse através do endereço:
 
```
http://0.0.0.0:8000

ou

http://localhost:8000
```
