"""
Pyserv TUI helper functions for picotui or similar.
"""

from collections import deque
from pathlib import Path

from pygtail import Pygtail
from scapy.layers.l2 import getmacbyip

HTTPD_ENV = {
    "DEBUG": "0",
    "PORT": "8080",
    "IDEV": "eth0",
    "IFACE": "0.0.0.0",
    "LPNAME": "httpd",
    "DOCROOT": ".",
}
TFTPD_ENV = {
    "DEBUG": "0",
    "PORT": "9069",
    "IDEV": "eth0",
    "IFACE": "0.0.0.0",
    "LPNAME": "tftpd",
    "DOCROOT": ".",
    "SOCK_TIMEOUT": "5",
}


def get_w_env(env):
    """
    Get UI widget settings from env values.
    """
    w_list = ["DEBUG", "PORT", "IDEV", "IFACE", "SOCK_TIMEOUT"]
    w_env = {k: v for k, v in env.items() if k in w_list}
    return w_env


def get_env(name):
    """
    Get environment data from selected (daemon) name.
    """
    env = {}
    if name.startswith('httpd'):
        env.update(HTTPD_ENV)
    elif name.startswith('tftpd'):
        env.update(TFTPD_ENV)
    else:
        TFTPD_ENV["LPNAME"] = 'atftpd'
        env.update(TFTPD_ENV)
    return env


def tail(iterable, max_size):
    """
    Create a tail queue with specified number of lines.
    """
    tailq = deque()
    for thing in iterable:
        if len(tailq) >= max_size:
            tailq.popleft()
        tailq.append(thing.rstrip())
    yield from tailq


def get_log_lines(filename, is_tail=False, keep_offset=True, num_lines=10):
    """
    Get lines from a (log) file.
    """
    lines = []
    if not Path(filename).exists():
        return lines
    pygtail = Pygtail(filename, read_from_end=is_tail, save_on_end=keep_offset)
    for line in tail(pygtail, num_lines):
        lines.append(line.split('UTC ')[1])
    return lines


def host_check(ip: str) -> str:
    """
    Check a remote host using IP address; returns remote MAC address
    if host is UP. Requires root or ``setcap`` on POSIX platforms.
    Windows does not have this limitation.

    :param ip: IP address or resolvable hostname
    """
    return str(getmacbyip(ip))
