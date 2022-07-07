# -*- coding: utf-8 -*-

"""
Simple HTTP server with broken GET rewriting for serving FW upgrades or
other local files in an engineering development environment.
"""

import logging
import sys

from . import GetServer


def serv_init(iface, port):
    """
    Init http server for handoff; init logging and server/handler classes.

    :param iface: server listen interface
    :param port: server listen port
    :return httpd_handler: threaded httpd handle, eg, httpd.start()
    """
    logging.basicConfig(level=logging.INFO)
    httpd_handler = GetServer(iface, port)
    return httpd_handler


def serv_run(iface='', port=8080):
    """
    Run in foreground command wrapper for console entry point;
    init logging and server, run the server, stop the server.

    :param port: server listen port
    """
    httpd = serv_init(iface, port)
    logging.info('Starting HTTP SERVER at %s:%s', iface, port)
    try:
        httpd.start()
    except KeyboardInterrupt:
        print("")
        print("Exiting ...")
        httpd.stop()


def main(args=None):
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


if __name__ == '__main__':
    sys.exit(main())
