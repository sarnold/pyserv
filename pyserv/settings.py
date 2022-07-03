# -*- coding: utf-8 -*-
"""
Default settings for daemon mode.
"""
import os
from pathlib import Path

from appdirs import AppDirs

from pyserv import version


def init_dirs(dirs):
    """
    Check and create user dirs for logs and PID (doc root is assumed to
    already exist).

    :param: list of Path objs
    """
    for app_path in dirs:
        if not app_path.exists():
            app_path.mkdir(parents=True, exist_ok=True)


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

DEBUG = os.getenv('DEBUG', default=0)
PORT = os.getenv('PORT', default='8080')
IFACE = os.getenv('IFACE', default='127.0.0.1')
HOMEDIR = os.getenv('DOCROOT', default=docroot)
LOGFILE = os.getenv('LOGFILE', default=logdir.joinpath('httpd.log'))
PIDFILE = os.getenv('PIDFILE', default=cachedir.joinpath('httpd.pid'))
LOGDIR = Path(LOGFILE).resolve().parent
PIDDIR = Path(PIDFILE).resolve().parent

# some test output
if __name__ == '__main__':
    show_uservars()
