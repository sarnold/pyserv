import os
import sys
from pathlib import Path
from string import Template

import pytest

from pyserv.tui_helpers import (
    HTTPD_ENV,
    TFTPD_ENV,
    get_env,
    get_log_lines,
    get_w_env,
    tail,
)

WIN32 = sys.platform == 'win32'
APPLE = sys.platform == 'darwin'

log_str = """
2025-04-20 19:32:12 UTC INFO tftpd.daemonize(149) Started
2025-04-20 19:32:12 UTC INFO tftpd.listen(95) Server requested on ip 0.0.0.0, port 9069
2025-04-20 19:32:12 UTC INFO tftpd.listen(107) Starting receive loop...
2025-04-20 19:32:24 UTC INFO tftpd.stop(262) Stopped
2025-04-20 19:42:43 UTC INFO tftpd.daemonize(149) Started
2025-04-20 19:42:43 UTC INFO tftpd.listen(95) Server requested on ip 0.0.0.0, port 9069
2025-04-20 19:42:43 UTC INFO tftpd.listen(107) Starting receive loop...
2025-04-20 19:42:56 UTC INFO tftpd.stop(262) Stopped
"""


def test_get_env(capfd):
    """
    Check env data from name.
    """
    for name in ["tftpdaemon", "atftpdaemon", "httpdaemon", "serv"]:
        d_env = get_env(name)
        print(d_env)
        assert 'DEBUG' in d_env
        assert name.startswith(d_env['LPNAME']) or name.startswith("serv")
    d_env = get_env('foop')
    assert d_env == {}


def test_get_w_env():
    """
    Check env matching.
    """
    w_env = get_w_env(TFTPD_ENV)
    print(w_env)
    assert 'PORT' in w_env
    assert 'LPNAME' not in w_env
    assert w_env['PORT'] == '9069'


def test_get_log_lines(tmp_path):
    """
    Create and read a short log file.
    """
    tf1 = tmp_path / "tftpd1.log"
    tf1.write_text(log_str, encoding="utf-8")
    lines = get_log_lines(str(tf1), is_tail=False, keep_offset=False, shorten=3)
    print(lines)
    assert len(lines) == 8
    assert "Started" in lines[0]


def test_get_log_num_lines(tmp_path):
    """
    Create and read a short log file.
    """
    tf2 = tmp_path / "tftpd2.log"
    tf2.write_text(log_str, encoding="utf-8")
    lines = get_log_lines(str(tf2), is_tail=False, keep_offset=False, num_lines=5)
    print(lines)
    assert len(lines) == 5
    assert "Stopped" in lines[0]


def test_get_log_no_lines(tmp_path):
    """
    Try to read a non-existent log file.
    """
    tf3 = tmp_path / "tftpd3.log"
    lines = get_log_lines(str(tf3), is_tail=False, keep_offset=False, num_lines=5)
    print(lines)
    assert len(lines) == 0
