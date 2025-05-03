"""
Pyserv TUI helper functions for picotui or similar.
"""

from collections import deque
from pathlib import Path
from typing import Deque, Dict, Generator, Iterable, List, Optional

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
    :returns: core env settings
    """
    w_list = ["DEBUG", "PORT", "IDEV", "IFACE", "SOCK_TIMEOUT"]
    w_env = {k: v for k, v in env.items() if k in w_list}
    return w_env


def get_env(name: str) -> Dict:
    """
    Get environment data from selected (daemon) name.

    :param name: name of the daemon/server command
    :returns: full env settings
    """
    env = {}
    if name.startswith('httpd') or name.startswith('serv'):
        env.update(HTTPD_ENV)
    if name.startswith('tftpd'):
        env.update(TFTPD_ENV)
    if name.startswith('atftpd'):
        TFTPD_ENV["LPNAME"] = 'atftpd'
        env.update(TFTPD_ENV)
    return env


def tail(iterable: Iterable, max_size: int) -> Generator:
    """
    Create a tail queue with specified max number of items (log lines).

    :param iterable: an iterable Python obj, ie, List or Tuple of strings
    :param max_size: max size of tail queue
    :yields: one item
    """
    tailq: Deque = deque()
    for thing in iterable:
        if len(tailq) >= max_size:
            tailq.popleft()
        tailq.append(thing.rstrip())
    yield from tailq


def get_log_lines(
    filename: str,
    is_tail: bool = False,
    keep_offset: bool = True,
    shorten: int = 0,
    num_lines: int = 10,
) -> List[Optional[str]]:
    """
    Get N lines from a (log) file. Set shorten=0 to disable line-splitting.
    Check for empty (falsey) tail items before processing line data.

    :param filename: path to log file as a string
    :param is_tail: read from the end of file
    :param keep_offset: save offset file (keep track of lines that have already been read)
    :param shorten: split lines on spaces and keep the remainder
    :param num_lines: number of lines in tail output
    :return: available log lines up to num_lines
    """
    lines: List = []
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
    :returns: MAC address string
    """
    return str(getmacbyip(ip))
