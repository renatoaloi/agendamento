# Sistema de Agendamento de Consultas

## Introdução

Sistema desenvolvido em Python, utilizando framework Django, e React como interface.

Desenvolvido para propósitos de estudo de TDD e Clean Code.

> Pode ser que você perceba algumas abordagens rudimentares de algumas implementações, mas é de propósito, pois eu decidi lançar mão do uso de alguns frameworks e fazer tudo manualmente; havia algumas habilidades que eu queria desenvolver e treinar.

> Optei nesse projeto por fazer um desenvolvimento evitando uso de frameworks e módulos como: DRF (Django Rest Framework) e também na parte do front, desisti de usar templates e bootstrap, para treinar um pouco de CSS.

## Pré-requisitos

- Python 3.6+ (eu usei o 3.9)
- virtualenv
- pip
- Node.js
- npm
- Docker
- Cloud server (ou um Raspberry Pi, no meu caso)

## Ferramentas

- Python 3.9
- Django 3.2
- Docker
- unittest
- Django.test
- Fabric3
- Jenkins

## Banco de dados

O banco de dados utilizado é o sqlite que acompanha o script scaffolding de criação da aplicação Django, ou seja, não necessita nenhuma configuração adicional.

## Backend

Desenvolvido orientado a TDD, utilizando Python e Django.

### Montagem do ambiente de desenvolvimento

- Clonar o codigo fonte e acessar a pasta do projeto:
```
> git clone https://github.com/renatoaloi/agendamento.git
> cd agendamento
```

- Criar o ambiente virtual e ativar o ambiente:
```
> virtualenv env
> .\env\Scripts\activate (Windows)
```
> Linux
> ```
> ./env/bin/activate
> ```

- Então instalar as dependências
```
> pip install -r requirements.txt
```

> **ATENÇÃO!** 
>
>  > Para efeito de segurança, o banco de dados não está na pasta da aplicação!
>
> Para rodar no ambiente de desenvolvimento, altere o arquivo ```settings.py``` na pasta ```agenda``` para refletir a instalação de desenvolvimento.
>
> Altere de:
> ```
> DATABASES = {
>   [...]
>       'NAME': BASE_DIR / '../database/db.sqlite3',
>   [...]
> }
> ```
> para:
> ```
> DATABASES = {
>   [...]
>       'NAME': BASE_DIR / 'db.sqlite3',
>   [...]
> }
> ```

- Efetuar as migrações do banco de dados:
```
> python manage.py migrate --no-input
```

- Carregar as fixtures (tabelas auxiliares):
```
> python manage.py loaddata especialidades profissionais
```

- Agora é só levantar o servidor de desenvolvimento:
```
> python manage.py runserver
```

- Para testar, abra o navegador e acesse:

```
http://localhost:8000/health-check
```

### Testes Funcionais e Unitários

- Para rodar todos os testes funcionais e unitários execute o seguinte:
```
> python manage.py test
```

Para rodar apenas os testes funcionais execute o seguinte:
```
> python manage.py test functional_tests
```

Para rodar apenas os testes unitários execute o seguinte:
```
> python manage.py test api
```

## Frontend

Baseado em react, o dashboard é uma aplicação simples de apenas 2 páginas.

### Montagem do ambiente

Para configurar o frontend, apenas altere a url de proxy no arquivo ```package.json``` localizado na pasta ```dashboard```, configurando o seguinte:

```
"proxy": "http://localhost:8000",
```

Em seguida apenas atualizar as dependências e levantar o ambiente:

```
> cd dashboard
> npm install
> npm start
```

### STAGING

Criar uma instância de um container Linux (eu optei por um ubuntu):

```
> docker run -it -d --rm --name agendasrv -p 8000:8000 -v C:\Users\seu_user\agendamento\infra:/infra ubuntu bash
```
Para conectar na instância, execute:

```
> docker exec -it agendasrv bash
```

Executar o script ```ci-dev.sh```, dentro da pasta ```infra```.

```
> ./infra/ci-dev.sh
```

Para desligar a instância, execute:

```
> docker stop agendasrv
```

### PROD

### CD/CI

#### Script Fabric3

#### Servidor Jenkins


#### Docker commands

```
> docker run -it -d --rm --name agendasrv -p 80:80 -v C:\Users\gracc\agendamento\infra:/infra ubuntu bash
> docker ps
> docker exec -it agendasrv bash
> docker stop agendasrv
```

#### Fabric3 Deploy to Raspberry Pi

```
> fab deploy:host=192.168.15.18 -u pi
```

#### Gerar Djangos' secret key

```
>>> from django.core.management.utils import get_random_secret_key
>>> print(get_random_secret_key())
```