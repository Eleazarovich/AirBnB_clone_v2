#!/usr/bin/python3
"""
this fabric script enerates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    archives all th files in the web_static folder
    """
    time = datetime.now()
    time = time.strftime('%Y%m%d%H%M%S')

    local('mkdir -p versions/')
    archive_path = "versions/web_static_{}.tgz".format(time)

    transfer = local('tar -cvzf {} web_static/'.format(archive_path))

    if transfer.succeeded:
        return archive_path
    return None

