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
    docroot = Path('./')
    return logdir, cachedir, docroot


logdir, cachedir, docroot = get_userdirs()

DEBUG = os.getenv('DEBUG', default=False)
PORT = os.getenv('PORT', default='8080')
HOMEDIR = os.getenv('DOCROOT', default=docroot)
LOGFILE = os.getenv('LOGFILE', default=logdir.joinpath('httpd.log'))
PIDFILE = os.getenv('PIDFILE', default=cachedir.joinpath('httpd.pid'))

# some test output
if __name__ == '__main__':
    print(f"pyserv {version}")
    print(f"Default port: {PORT}")
    print(f"Debug output: {DEBUG}")
    print("User paths:")
    print(f"  docroot: {HOMEDIR}")
    print(f"  logfile: {LOGFILE}")
    print(f"  pidfile: {PIDFILE}")
