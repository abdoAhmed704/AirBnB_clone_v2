#!/usr/bin/python3
from fabric import task
from datetime import datetime
import os

@task(name='do-pack')
def do_pack(c):
    """Generates a .tgz archive from the contents of the web_static folder"""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "versions/web_static_{}.tgz".format(timestamp)
    try:
        os.makedirs("versions", exist_ok=True)
        c.local("tar -cvzf {} web_static".format(archive_name))
        return archive_name
    except Exception as e:
        return None

