"""
Simple HTTP server with broken GET rewriting for serving FW upgrades or
other local files in an engineering development environment.
"""

import logging
import os
import sys
from pathlib import Path

from . import GetServer
from .settings import DEBUG, DOCROOT

LVL_NAME = 'DEBUG' if DEBUG else 'INFO'


def serv_init(iface, port, directory):
    """
    Init http server for handoff; init logging and server/handler classes.

    :param iface: initialized listen interface
    :param port: initialized listen port
    :param directory: server document root
    :return httpd_handler: threaded httpd handle, eg, httpd.start()
    """
    logging.basicConfig(level=LVL_NAME)
    httpd_handler = GetServer(iface, port, directory)
    return httpd_handler


def serv_run(iface='', port=8080, directory=DOCROOT):  # pragma: no cover
    """
    Run in foreground command wrapper for console entry point;
    init logging and server, run the server, stop the server.

    :param iface: server listen interface
    :param port: server listen port
    :param directory: server document root
    """
    if not Path(directory).exists():
        logging.error('DOCROOT directory %s does not exist', directory)
        sys.exit(1)
    start_dir = Path.cwd()
    path_diff = start_dir.name != Path(directory).name
    if sys.version_info < (3, 7) and path_diff:
        os.chdir(directory)
    httpd = serv_init(iface, port, directory)
    logging.info('Starting HTTP SERVER at %s:%s', iface, port)
    try:
        httpd.start()
        httpd.join()
    except KeyboardInterrupt:
        print("\nExiting ...")
        httpd.stop()
        os.chdir(start_dir)


def main(args=None):  # pragma: no cover
    """
    The serv entry point wrapper; both args are optional, but you must
    provide either PORT or PORT *and* IFACE.

    Usage::

      serv [PORT] [IFACE]
    """
    if args is None:
        args = sys.argv[1:]

    if len(args) == 1:
        serv_run(port=int(args[0]))
    elif len(args) == 2:
        serv_run(port=int(args[0]), iface=args[1])
    else:
        serv_run()


if __name__ == '__main__':  # pragma: no cover
    sys.exit(main())
