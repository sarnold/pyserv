# -*- coding: utf-8 -*-
import os
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


def test_get_userdirs():
    """We should get Path objs"""
    usr_paths = get_userdirs()

    for thing in usr_paths:
        assert isinstance(thing, Path)

    assert get_userdirs()[0].name == 'log'
    assert get_userdirs()[1].name == VERSION
    assert get_userdirs()[2].name == Path.cwd().name


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
