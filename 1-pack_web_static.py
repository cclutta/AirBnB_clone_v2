#!/usr/bin/python3
"""
    Script that generates archive from web_static folder
"""
from datetime import datetime
from fabric.api import local
from os import makedirs


def do_pack():
    """ Function that generates the archive. """
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    path = "versions/web_static_{}.tgz".format(timestamp)

    try:
        makedirs("./versions", exist_ok=True)
        local('tar -cvzf {} web_static'.format(path))
        return path

    except Exception:
        return NOne
