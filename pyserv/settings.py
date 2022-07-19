"""
Pyserv default settings for daemon mode.
"""
import importlib
import os
import sys
from pathlib import Path

from appdirs import AppDirs

from pyserv import __version__ as version


def get_userdirs():
    """
    Get platform-agnostic user directory paths via appdirs.

    :return tuple: logdir, piddir, docdir as Path objs
    """
    dirs = AppDirs(appname='pyserv', version=version)
    logdir = Path(dirs.user_log_dir)
    piddir = Path(dirs.user_cache_dir).joinpath('run')
    docdir = Path(os.getcwd())
    return logdir, piddir, docdir


def init_dirs(dirs):
    """
    Check and create user dirs for logs and PID (doc root is assumed
    to already exist).

    :param dirs: list of Path objs
    """
    for usr_path in dirs:
        usr_path.mkdir(parents=True, exist_ok=True)


def platform_check():
    """
    Check to see if we think we are POSIX.

    :return bool: True if POSIX, else False
    """
    valid_os = []
    myname = sys.platform
    is_posix = os.name == 'posix'
    posix_list = [
        'linux',
        'darwin',
        'openbsd',
        'freebsd',
    ]
    valid_os = [x for x in posix_list if x in myname and is_posix]

    return valid_os


def show_uservars():
    """
    Display defaults and (possibly) overridden host paths and environment
    variables.
    """
    print("Python version:", sys.version)
    print("-" * 79)
    print(f"pyserv {version}")

    dirnames = ['log_dir', 'pid_dir', 'doc_dir']
    modname = 'pyserv.settings'
    try:
        mod = importlib.import_module(modname)
        print(mod.__doc__)

        print("Default user vars:")
        for dirname, path in zip(dirnames, mod.get_userdirs()):
            print(f'  {dirname}: {path}')

        print("\nCurrent environment values:")
        print(f"  DEBUG: {DEBUG}")
        print(f"  PORT: {PORT}")
        print(f"  IFACE: {IFACE}")
        print(f"  LOG: {LOG}")
        print(f"  PID: {PID}")
        print(f"  DOCROOT: {DOCROOT}")
        print("-" * 79)

    except (ImportError, NameError) as exc:
        print("FAILED:", repr(exc))


DEBUG = os.getenv('DEBUG', default=None)
PORT = os.getenv('PORT', default='8080')
IFACE = os.getenv('IFACE', default='127.0.0.1')
LOG = os.getenv('LOG', default=str(get_userdirs()[0].joinpath('httpd.log')))
PID = os.getenv('PID', default=str(get_userdirs()[1].joinpath('httpd.pid')))
DOCROOT = os.getenv('DOCROOT', default=str(get_userdirs()[2]))
