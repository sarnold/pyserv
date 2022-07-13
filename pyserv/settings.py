"""
Pyserv default settings for daemon mode.
"""
import importlib
import os
import sys

from pyserv import __version__ as version


def init_dirs(dirs):
    """
    Check and create user dirs for logs and PID (doc root is assumed
    to already exist).
    :param: list of Path objs
    """
    for usr_path in dirs:
        usr_path.mkdir(parents=True, exist_ok=True)


def platform_check():
    """
    Check to see if we think we are POSIX.

    :return: True if POSIX, else False
    """
    valid_os = False
    myname = sys.platform
    is_posix = os.name == 'posix'
    posix_list = [
        'linux',
        'darwin',
        'openbsd',
        'freebsd',
    ]
    valid_os = any([x for x in posix_list if x in myname and is_posix])

    return valid_os


def show_uservars():
    """
    Display default host paths and environment.
    """
    print("Python version:", sys.version)
    print("-" * 79)
    print(f"pyserv {version}")

    modname = 'pyserv.settings'
    try:
        mod = importlib.import_module(modname)
        print(mod.__doc__)

        print("Default user paths:")
        print(f"  LOG file: {LOG}")
        print(f"  PID file: {PID}")

    except (ImportError, NameError) as exc:
        print("FAILED:", repr(exc))

    print("\nCurrent environment values:")
    print(f"  DEBUG: {DEBUG}")
    print("-" * 79)


DEBUG = os.getenv('DEBUG', default=0)
LOG = 'httpd.log'
PID = 'httpd.pid'

# some test output
if __name__ == '__main__':  # pragma: no cover
    show_uservars()
