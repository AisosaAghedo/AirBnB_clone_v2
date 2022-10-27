#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers using the function do_deploy
"""

from fabric.api import *
from os.path import exists
env.hosts = ['3.239.6.186', '52.90.15.34']


def do_deploy(archive_path):
    """Returns True if all operations have been done correctly"""
    if exists(archive_path) is False:
        return False
    try:
        file_path = archive_path.split("/")[-1]
        no_ext = file_path.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False
