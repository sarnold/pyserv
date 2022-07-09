# -*- coding: utf-8 -*-
import os
import sys
from pathlib import Path

from pyserv import VERSION
from pyserv.settings import (
    DEBUG,
    HOMEDIR,
    IFACE,
    LOGDIR,
    LOGFILE,
    PIDDIR,
    PIDFILE,
    PORT,
    get_userdirs,
    init_dirs,
    show_uservars,
)

WIN32 = sys.platform == 'win32'
APPLE = sys.platform == 'darwin'


def test_get_userdirs():
    """We should get Path objs"""
    logdir, cachedir, docroot = get_userdirs()

    for thing in logdir, cachedir, docroot:
        assert isinstance(thing, Path)

    if WIN32:
        assert logdir.name == 'Logs'
    elif APPLE:
        assert logdir.name == VERSION
    else:
        assert logdir.name == 'log'

    assert cachedir.name == VERSION
    assert docroot.name == Path.cwd().name


def test_init_dirs(tmp_path):
    """Create user dirs (usually the paths from get_userdirs)"""
    LOGDIR = tmp_path.joinpath('log')
    PIDDIR = tmp_path.joinpath('run')
    user_dirs = [LOGDIR, PIDDIR]
    init_dirs(user_dirs)

    for thing in user_dirs:
        assert thing.exists()
        assert thing.is_dir()


def test_show_uservars():
    """Start with default env"""
    show_uservars()
