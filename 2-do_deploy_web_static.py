#!/usr/bin/python3
"""
    Script that ) that distributes an archive to your web servers
"""
from fabric.api import env, put, run
from os import path

env.hosts = ['44.197.198.112', '3.239.43.67']


def do_deploy(archive_path):
    """ Distributes the archive
    
    Args:
        archive_path: path of the archive
    """

    try:
        if not path.exists(archive_path):
            raise FileNotFoundError
        
        name = archive_path.split("/")[-1]
        name_no_ext = name.split(".")[0]

        remote = "/data/web_static/releases"
        dest = "{}/{}".format(remote, name_no_ext)

        put(archive_path, '/tmp')
        run('mkdir -p {}/'.format(dest))
        run('tar -xzf /tmp/{} -C {}'.format(name, dest))
        run('rm /tmp/{}'.format(name))
        run('mv {}/web_static/* {}/'.format(dest, dest))
        run('rm -rf {}/web_static'.format(dest))
        run('rm -rf /data/web_static/current')
        run('ln -s {}/ /data/web_static/current'.format(dest))

    except Exception:
        print("Error. Version deploy aborted")
        return False

    print("New version deployed!")
    return True
