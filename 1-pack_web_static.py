#!/usr/bin/python3
"""
This is a python porgram that uses Fabric to Tranfer
file to my server, by first compressing it.
"""

from fabric.api import local
# from time import strftime
# from datetime import time


def do_pack():
    """
    do_pack funtion or method will create a folder called
    version and create web_static achive in it with date
    """
    try:
        local("mkdir -p version") 
        local("tar -czvf version/web_static_$(%Y%m%d%H%M%s).tgz web_static")
        return "version/web_static_$(%Y%m%d%H%M%s).tgz"

    except Exception as e:
        return None
