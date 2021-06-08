Instruções de acesso:

Para acessar o sistema é preciso ter instalado na máquina os seguintes serviços: 
- Docker
- Docker Compose

``` 
$ git clone https://github.com/gabrielmrp/usertasks-django-crud.git
```

Entre na pasta do sistema

```
$ cd usertasks-django-crud
```

Faça a instalação do sistema através do comando abaixo
  
```  
$ docker-compose up --build
```

O comando abaixo deve ser acionado para realizar a migração do banco de dados

```
$ docker-compose run web python3 manage.py migrate
```

Acesse através do endereço:
 
```
http://0.0.0.0:8000

ou

http://localhost:8000
```
