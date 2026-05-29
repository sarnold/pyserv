"""
Pyserv TUI helper functions for picotui or similar.
"""

from pathlib import Path
from typing import IO, Dict, List, Optional

from logwatcher.logwatcher import LogWatcher
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


class TLogWatcher(LogWatcher):
    """
    Overriding ``open()`` for decoding may lead to issues in newer Python
    so open in binary mode instead.
    """

    @classmethod
    def open(cls, file: str) -> IO:
        return open(file, 'rb')


def dummy_callback(filename: str, lines: List[Optional[str]]):  # pylint: disable=W0613
    """Logwatcher feeds a log display only, no need for line printing."""


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


def update_log_lines(
    fname: str, shorten: int = 0, num_lines: int = 10
) -> List[Optional[str]]:
    """
    Simpler version of ``get_log_lines()`` using LogWatcher instead of
    Pygtail.

    :param fname: path to log file as a string
    :param shorten: split lines on spaces and keep the remainder
    :param num_lines: number of lines in tail output
    :return: available log lines up to num_lines
    """
    lines: List = []
    if not Path(fname).exists():
        return lines
    log_path = Path(fname).parent.resolve()
    lw = TLogWatcher(str(log_path), dummy_callback)
    decoded_lines = [
        line.decode('utf-8')
        for line in lw.tail(str(fname), num_lines)
        if isinstance(line, bytes)
    ]
    for line in decoded_lines:
        if line:
            if shorten > 0 and isinstance(line, str):
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
