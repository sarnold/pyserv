# -*- coding: utf-8 -*-
"""
Default settings for daemon mode.
"""
import os
from pathlib import Path

from appdirs import AppDirs

from pyserv import version


def get_userdirs():
    """
    Set platform-agnostic user directory paths via appdirs.

    :return tuple: logdir, cachedir, docroot as Path objs
    """
    dirs = AppDirs('pyserv', 'nerdboy')
    logdir = Path(dirs.user_log_dir)
    cachedir = Path(dirs.user_cache_dir)
    docroot = Path(os.getcwd())
    return logdir, cachedir, docroot


def show_uservars():
    """
    Display user environment settings.
    """
    print(f"pyserv {version}")
    print("\nUser VARS:")
    print(f"  DEBUG: {DEBUG}")
    print(f"  PORT: {PORT}")
    print(f"  IFACE: {IFACE}")
    print(f"  DOCROOT: {HOMEDIR}")
    print(f"  LOGFILE: {LOGFILE}")
    print(f"  PIDFILE: {PIDFILE}")


logdir, cachedir, docroot = get_userdirs()

DEBUG = os.getenv('DEBUG', default=False)
PORT = os.getenv('PORT', default='8080')
IFACE = os.getenv('IFACE', default='127.0.0.1')
HOMEDIR = os.getenv('DOCROOT', default=docroot)
LOGFILE = os.getenv('LOGFILE', default=logdir.joinpath('httpd.log'))
PIDFILE = os.getenv('PIDFILE', default=cachedir.joinpath('httpd.pid'))

# some test output
if __name__ == '__main__':
    show_uservars()
