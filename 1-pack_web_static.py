#!/usr/bin/python3
'''
Fabric script that generates a .tgz archive from the contents of the web_static
folder
'''
from datetime import datetime
from fabric.api import local


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
