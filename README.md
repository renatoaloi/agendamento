# Sistema de Agendamento de Consultas Médicas

## Introdução

Sistema desenvolvido em Python, utilizando framework Django, e React como interface.

Desenvolvido para propósitos de estudo de TDD e Clean Code.

> Pode ser que você perceba algumas abordagens rudimentares de algumas implementações, mas é de propósito, pois eu decidi lançar mão do uso de alguns frameworks e fazer tudo na unha; havia algumas habilidades que eu queria desenvolver e treinar.
>
> Optei nesse projeto por fazer um desenvolvimento evitando uso de frameworks e módulos como: DRF (Django Rest Framework) e também na parte do front, desisti de usar templates e bootstrap, para treinar um pouco de CSS.

## Pré-requisitos

- Python 3.6+ (eu usei o 3.9)
- virtualenv
- pip
- Node.js
- npm

Opcional:
- VSCode

## Banco de dados

O banco de dados utilizado é o sqlite que acompanha o script scaffolding de criação da aplicação Django, ou seja, não necessita nenhuma configuração adicional.

## Backend

Desenvolvido orientado a TDD, utilizando Python e Django.

### Montagem do ambiente

[ em desenvolvimento ]

## Frontend

Baseado em react, o dashboard é uma aplicação simples de apenas 2 páginas.

### Montagem do ambiente

[ em desenvolvimento ]

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