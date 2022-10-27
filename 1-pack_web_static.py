#!/usr/bin/python3
"""
a Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack
"""
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """ returns the archive path if the archive has been correctly
    generated. Otherwise, it should return None"""
    date = datetime.utcnow()
    archive_path = "versions/web_static_{}{}{}{}{}{}.tgz".format(date.year,
                                                                 date.month,
                                                                 date.day,
                                                                 date.hour,
                                                                 date.minute,
                                                                 date.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(archive_path)).failed is True:
        return None
    return archive_path
