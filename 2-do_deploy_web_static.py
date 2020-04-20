#!/usr/bin/python3
'''
Fabric script that generates a .tgz archive from the contents of the web_static
folder
'''
from os.path import exists, isfile
from datetime import datetime
from fabric.api import local, env, put, run
env.hosts = ['104.196.201.203', '54.175.122.113']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/holberton'

def do_pack():
    '''generate a tgz archive '''

    time = datetime.now().strftime("%Y%m%d%H%M%S")
    stored = "versions/web_static_{}.tgz".format(time)
    local("mkdir -p versions")
    local("mkdir -p versions")
    result = local("tar -cvzf {} web_static".format(stored))

    if result.failed:
        return None
    else:
        return result

def do_deploy(archive_path):
    '''deploy archive to servers'''
    if not isfile(archive_path) and not exists(archive_path):
        return False
    try:
        put(archive_path, '/tmp')
        name = archive_path.split('/')[1][:-4]
        run('sudo mkdir -p /data/web_static/releases/' + name + '/')
        run('sudo chown -R ubuntu:ubuntu /data')
        run('tar -xzf /tmp/' + name + '.tgz'
            ' -C /data/web_static/releases/' + name + '/')
        run('rm /tmp/' + name + '.tgz')
        run('mv /data/web_static/releases/' + name + '/web_static/* ' +
            '/data/web_static/releases/' + name + '/')
        run('rm -rf /data/web_static/releases/' + name + '/web_static')
        run('rm -rf /data/web_static/current')
        run('ln -sf /data/web_static/releases/' + name + '/ ' +
            '/data/web_static/current')
        print('New version deployed!')
    except:
        return False
    return True
