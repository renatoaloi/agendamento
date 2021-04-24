#!/bin/bash
#export DEBIAN_FRONTEND=noninteractive
export TZ=America/Sao_Paulo
ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
apt update
apt upgrade
apt install nginx -y
service nginx start
apt install software-properties-common -y
whereis python
ln -s /usr/bin/python3.8 /usr/bin/python
python --version
apt install git -y
git clone https://github.com/renatoaloi/agendamento.git /app
cd /app
mkdir ../database
apt install python3-venv -y
mkdir -p virtualenv
python -m venv virtualenv
./virtualenv/bin/pip install wheel
./virtualenv/bin/pip install -r requirements.txt
./virtualenv/bin/python manage.py migrate --noinput
./virtualenv/bin/python manage.py loaddata especialidades profissionais
./virtualenv/bin/python manage.py runserver 0.0.0.0:8000
