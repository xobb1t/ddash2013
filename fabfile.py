import os
from fabric.api import *
from fabric.contrib.files import append, exists, upload_template


@task
def vagrant():
    env.hosts = ['10.10.0.101']
    env.user = 'singlepoint'


@task
def production():
    env.hosts = ['singlepointhq.com']
    env.user = 'singlepoint'


@task
def upload_public_key():
    with settings(user='root'):
        to = 'singlepoint'
        path = os.path.expanduser('~/.ssh/id_rsa.pub')
        if to and os.path.exists(path):
            key = ' '.join(open(path).read().strip().split(' ')[:2])
            run('mkdir -p /home/{0}/.ssh'.format(to))
            append('/home/{0}/.ssh/authorized_keys'.format(to), key, partial=True)
            run('chown {0}:{0} /home/{0}/.ssh/authorized_keys'.format(to))
            run('chmod 600 /home/{0}/.ssh/authorized_keys'.format(to))
            run('chown {0}:{0} /home/{0}/.ssh'.format(to))
            run('chmod 700 /home/{0}/.ssh'.format(to))


@task
def manage(command):
    run('export DJANGO_SETTINGS_MODULE="project.settings.production" && cd ~/src && ~/.env/bin/python manage.py {}'.format(command))


@task
def syncdb():
    manage('syncdb --migrate')


@task
def restart():
    run('supervisorctl reload')
    run('supervisorctl restart gunicorn')


@task
def collectstatic():
    manage('collectassets')
    manage('collectstatic --noinput --verbosity=0')


@task
def install_requirements():
    run('cd ~/src && ~/.env/bin/pip install -r requirements/production.txt')


@task
def update_code():
    if not exists('~/.git'):
        run('mkdir ~/.git && cd ~/.git && git init --bare')
    local('git push ssh://{user}@{host}/~/.git master'.format(**env))
    if not exists('src'):
        run('git clone .git src')
    with cd('src'):
        run('git pull origin master')


@task
def deploy():
    update_code()
    install_requirements()
    syncdb()
    collectstatic()
    restart()
