from fabric.contrib.files import append, exists, sed
from fabric.api import env, local, run
import random

REPO_URL='https://github.com/renatoaloi/agendamento.git'

def deploy():
    app_name = 'agendamento'
    app_folder = f'/home/{env.user}/app'
    src_folder = f'{app_folder}/src'
    _prepare_environment(app_folder)
    _create_directory_structure_if_necessary(app_folder)
    _get_latest_source(src_folder)
    _update_virtualenv(src_folder)
    _update_static_files(src_folder)
    _update_database(src_folder)
    _configure_gunicorn(src_folder, app_name)
    _configure_nginx(src_folder)
    _start_services()

def _prepare_environment(app_folder):
    run('export SECRET_KEY="0av%xx7jd0tlp$ifa29a24vr82(mp^#w5an+0z74w+_-dd97ty"')
    run('export DEBUG="False"')
    run(f'export APPPATH={app_folder}')
    run(f'export PYTHONPATH={app_folder}')
    run('sudo apt upgrade -y')
    run('sudo apt update -y')
    #run('export TZ="America/Sao_Paulo"')
    #run('ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone')
    run('sudo apt install nginx git software-properties-common python3-venv -y')

def _create_directory_structure_if_necessary(app_folder):
    for subfolder in ['database', 'static', 'virtualenv', 'src']:
        run(f'mkdir -p {app_folder}/{subfolder}')

def _get_latest_source(src_folder):
    if exists(f'{src_folder}/.git'):
        run(f'cd {src_folder} && git pull')
    else:
        run(f'git clone {REPO_URL} {src_folder}')

def _update_virtualenv(src_folder):
    virtualenv_folder = f'{src_folder}/../virtualenv'
    if not exists(f'{virtualenv_folder}/bin/pip'):
        run(f'python3.7 -m venv {virtualenv_folder}')
    run(f'{virtualenv_folder}/bin/pip install -r {src_folder}/requirements.txt')

def _update_static_files(src_folder):
    run(f'cd {src_folder} && ../virtualenv/bin/python manage.py collectstatic --no-input')

def _update_database(src_folder):
    run(f'cd {src_folder} && ../virtualenv/bin/python manage.py migrate --no-input')

def _configure_gunicorn(src_folder, app_name):
    run(f'sudo cp {src_folder}/infra/gunicorn-systemv.template.service /etc/init.d/{app_name}')
    run(f'sudo chmod a+x /etc/init.d/{app_name}')
    run(f"sudo sed -i -e 's/\\r//g' /etc/init.d/{app_name}")
    run('sudo systemctl daemon-reload')

def _configure_nginx(src_folder):
    run('sudo rm -rf /etc/nginx/sites-available/default')
    run(f'sudo cp {src_folder}/infra/nginx.template.conf /etc/nginx/sites-available/default')

def _start_services():
    run('sudo service agendamento start')
    run('sudo service nginx restart')
