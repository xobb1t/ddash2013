from fabric.api import *


def vagrant():
    env.hosts = ['127.0.0.1:2222']
    env.user = 'singlepoint'


def production():
    env.hosts = ['singlepointhq.com']
    env.user = 'singlepoint'


@task
def manage(command):
    run('export DJANGO_SETTINGS_MODULE="project.settings.production" && cd ~/src && ~/.env/bin/python manage.py {}'.format(command))


@task
def syncdb():
    manage('syncdb --migrate')


@task
def restart():
    run('sudo supervisorctl restart site')


@task
def collectstatic():
    manage('collectassets')
    manage('collectstatic --noinput --verbosity=0')


@task
def install_requirements():
    run('cd ~/src && ~/.env/bin/pip install -r requirements/production.txt')


@task
def update_code():
    local('git push ssh://{user}@{host}/~/.git'.format(**env))
    run('cd ~/src && git pull')


@task
def deploy():
    update_code()
    install_requirements()
    syncdb()
    collectstatic()
    restart()
