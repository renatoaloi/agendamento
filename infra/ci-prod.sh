#!/bin/bash
export SECRET_KEY="0av%xx7jd0tlp$ifa29a24vr82(mp^#w5an+0z74w+_-dd97ty"
export DEBUG="False"
export TZ="America/Sao_Paulo"
export APPPATH=/app
export PYTHONPATH=$APPPATH
ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
apt update
apt upgrade
apt install nginx git software-properties-common python3-venv -y
rm -rf /etc/nginx/sites-available/default
cp /infra/nginx.template.conf /etc/nginx/sites-available/default
ln -s /usr/bin/python3.8 /usr/bin/python
git clone https://github.com/renatoaloi/agendamento.git /app
cd /app
mkdir ../database
mkdir ../static
mkdir -p virtualenv
python -m venv virtualenv
./virtualenv/bin/pip install wheel
./virtualenv/bin/pip install -r requirements.txt
./virtualenv/bin/pip install gunicorn
./virtualenv/bin/python manage.py collectstatic --noinput
./virtualenv/bin/python manage.py migrate --noinput
./virtualenv/bin/python manage.py loaddata especialidades profissionais
#./virtualenv/bin/gunicorn agenda.wsgi:application

#cp /infra/gunicorn-systemd.template.service /etc/systemd/system/agendamento.service

cp /infra/gunicorn-systemv.template.service /etc/init.d/agendamento
sed -i -e 's/\r//g' /etc/init.d/agendamento
service agendamento start
service nginx start

tail -f /var/log/nginx/access.log &
