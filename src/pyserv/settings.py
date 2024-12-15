"""
Pyserv default settings for server and daemon modes.
"""
import importlib
import os
import sys
from pathlib import Path

from platformdirs import PlatformDirs

from . import __version__ as version


def get_userdirs():
    """
    Get platform-agnostic user directory paths via appdirs.

    :return tuple: logdir, piddir, docdir as Path objs
    """
    dirs = PlatformDirs(appname='pyserv', appauthor='nerdboy')
    run_check = Path('/run/user').exists()
    run_path = dirs.user_runtime_path if run_check else dirs.user_cache_path
    logdir = dirs.user_log_path
    piddir = run_path
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

    :return list: valid platform name
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
    print(f"Python version: {sys.version}")
    print("-" * 79)
    print(f"pyserv {version}")

    iface = 'all' if not IFACE else IFACE
    dirnames = ['log_dir', 'pid_dir', 'work_dir']
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
        print(f"  IFACE: {iface}")
        print(f"  LPNAME: {LPNAME}")
        print(f"  LOG: {LOG}")
        print(f"  PID: {PID}")
        print(f"  DOCROOT: {DOCROOT}")
        print(f"  SOCK_TIMEOUT: {SOCK_TIMEOUT}")
        print("-" * 79)

    except (ImportError, NameError) as exc:
        print(f"FAILED: {repr(exc)}")


DEBUG = os.getenv('DEBUG', default=None)
PORT = os.getenv('PORT', default='8000')
IFACE = os.getenv('IFACE', default='127.0.0.1')
LPNAME = os.getenv('LPNAME', default='httpd')
LOG = os.getenv('LOG', default=str(get_userdirs()[0].joinpath(f'{LPNAME}.log')))
PID = os.getenv('PID', default=str(get_userdirs()[1].joinpath(f'{LPNAME}.pid')))
DOCROOT = os.getenv('DOCROOT', default=str(get_userdirs()[2]))
SOCK_TIMEOUT = os.getenv('SOCK_TIMEOUT', default='5')
