import os
import sys
from pathlib import Path

import pytest

import pyserv
from pyserv.settings import (
    get_userdirs,
    init_dirs,
    platform_check,
    show_uservars,
    version,
)

WIN32 = sys.platform == 'win32'
APPLE = sys.platform == 'darwin'


def test_get_userdirs():
    """We should get Path objs"""
    logdir, piddir, docdir = get_userdirs()

    for thing in logdir, piddir, docdir:
        assert isinstance(thing, Path)

    if WIN32:
        assert logdir.name == 'Logs'
    elif APPLE:
        assert logdir.name == version
    else:
        assert logdir.name == 'log'

    assert piddir.name == 'run'
    assert docdir.name == Path.cwd().name


def test_init_dirs(tmp_path):
    """Create user dirs (usually the paths from get_userdirs)"""
    LOGDIR = tmp_path.joinpath('log')
    PIDDIR = tmp_path.joinpath('run')
    user_dirs = [LOGDIR, PIDDIR]
    init_dirs(user_dirs)

    for thing in user_dirs:
        assert thing.exists()
        assert thing.is_dir()


@pytest.mark.skipif(sys.platform == 'win32',
                    reason="daemon not supported on Windows")
def test_platform_check():
    """Test for POSIX platform"""
    iam = platform_check()
    assert iam


def test_show_uservars():
    """Start with default env"""
    show_uservars()


def test_show_uservars_error(monkeypatch):
    """Monkeypatch attr"""
    monkeypatch.delattr('pyserv.settings.LOG', raising=True)
    show_uservars()
