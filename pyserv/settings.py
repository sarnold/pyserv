# -*- coding: utf-8 -*-
"""
Default settings for daemon mode.
"""
import importlib
import os
import sys
from pathlib import Path

from appdirs import AppDirs

from pyserv import VERSION as version
from pyserv import __description__  # noqa: F401


def init_dirs(dirs):
    """
    Check and create user dirs for logs and PID (doc root is assumed
    to already exist).

    :param: list of Path objs
    """
    for usr_path in dirs:
        if not usr_path.exists():
            usr_path.mkdir(parents=True, exist_ok=True)


def get_userdirs():
    """
    Set platform-agnostic user directory paths via appdirs.

    :return tuple: logdir, cachedir, docroot as Path objs
    """
    dirs = AppDirs(appname='pyserv', version=version)
    logdir = Path(dirs.user_log_dir)
    cachedir = Path(dirs.user_cache_dir)
    docroot = Path(os.getcwd())
    return logdir, cachedir, docroot


def show_uservars():
    """
    Display host platform user paths, files and environment.
    """
    print("Python version:", sys.version)
    print("-" * 79)
    print(f"pyserv {version}")

    dirnames = ['log_dir', 'pid_dir', 'doc_root']
    modname = 'pyserv.settings'
    try:
        mod = importlib.import_module(modname)
        print(mod.__description__)

        print("\nDefault user vars:")
        for dirname, path in zip(dirnames, mod.get_userdirs()):
            print(f'  {dirname}: {path}')

    except (ImportError, AttributeError) as exc:
        print("FAILED:", repr(exc))

    print("\nCurrent environment values:")
    print(f"  DEBUG: {DEBUG}")
    print(f"  PORT: {PORT}")
    print(f"  IFACE: {IFACE}")
    print(f"  DOCROOT: {HOMEDIR}")
    print(f"  LOGFILE: {LOGFILE}")
    print(f"  PIDFILE: {PIDFILE}")
    print("-" * 79)


DEBUG = os.getenv('DEBUG', default='0')
PORT = os.getenv('PORT', default='8080')
IFACE = os.getenv('IFACE', default='127.0.0.1')
HOMEDIR = os.getenv('DOCROOT', default=str(get_userdirs()[2]))
LOGFILE = os.getenv('LOGFILE', default=str(get_userdirs()[0].joinpath('httpd.log')))
PIDFILE = os.getenv('PIDFILE', default=str(get_userdirs()[1].joinpath('httpd.pid')))
LOGDIR = Path(LOGFILE).resolve().parent
PIDDIR = Path(PIDFILE).resolve().parent

# some test output
if __name__ == '__main__':
    show_uservars()
