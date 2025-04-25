"""
Pyserv TUI helper functions for picotui or similar.
"""

from collections import deque
from pathlib import Path
from typing import Deque, Dict, Generator, Iterable

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


def get_w_env(env: Dict) -> Dict:
    """
    Get UI widget settings from env values.

    :param env: default environ for selected daemon/server
    """
    w_list = ["DEBUG", "PORT", "IDEV", "IFACE", "SOCK_TIMEOUT"]
    w_env = {k: v for k, v in env.items() if k in w_list}
    return w_env


def get_env(name: str) -> Dict:
    """
    Get environment data from selected (daemon) name.

    :param name: name of the daemon/server command
    """
    env = {}
    if name.startswith('httpd') or name.startswith('serv'):
        env.update(HTTPD_ENV)
    elif name.startswith('tftpd'):
        env.update(TFTPD_ENV)
    elif name.startswith('atftpd'):
        TFTPD_ENV["LPNAME"] = 'atftpd'
        env.update(TFTPD_ENV)
    else:
        print("Invalid command name")
    return env


def tail(iterable: Iterable, max_size: int) -> Generator:
    """
    Create a tail queue with specified max number of lines.
    Check for empty (falsey) items before appending to queue.

    :param iterable: an iterable Python obj, ie, List or Tuple of strings
    :param max_size: max size of tail queue
    """
    tailq: Deque = deque()
    for thing in iterable:
        if len(tailq) >= max_size:
            tailq.popleft()
        tailq.append(thing.rstrip())
    yield from tailq


def get_log_lines(filename, is_tail=False, keep_offset=True, shorten=0, num_lines=10):
    """
    Get N lines from a (log) file. Set shorten=0 to disable line-splitting.

    :param filename: path to log file as a string
    :type filename: str
    :param is_tail: read from the end of file
    :type is_tail: bool
    :param keep_offset: save offset file (keep track of lines that have already been read)
    :type keep_offset: bool
    :param shorten: split lines on spaces and keep the remainder
    :type shorten: int
    :param num_lines: number of lines in tail output
    :type num_lines: int
    :return: available log lines up to num_lines
    :rtype: List
    """
    lines = []
    if not Path(filename).exists():
        return lines
    pygtail = Pygtail(filename, read_from_end=is_tail, save_on_end=keep_offset)
    for line in tail(pygtail.readlines(), num_lines):
        if line:
            if shorten > 0:
                lines.append(line.split(' ', maxsplit=shorten)[shorten])
            else:
                lines.append(line)
    return lines


def host_check(ip: str) -> str:
    """
    Check a remote host using IP address; returns remote MAC address
    if host is UP. Requires root or ``setcap`` on POSIX platforms.
    Windows does not have this limitation.

    :param ip: IP address or resolvable hostname
    """
    return str(getmacbyip(ip))
