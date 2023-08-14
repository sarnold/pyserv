"""
Simple WSGI server for serving swagger or basic flask apps in an engineering
development environment.
"""

import logging
import sys
from wsgiref.simple_server import demo_app

from . import GetServerWSGI
from .settings import DEBUG, DOCROOT, PORT

LVL_NAME = 'DEBUG' if DEBUG else 'INFO'


def wsgi_init(port, wapp, validate=True):
    """
    Init wsgi server for handoff; init logging and simple_server classes.

    :param iface: initialized listen interface
    :param port: initialized listen port
    :return wsgi_handler: wsgi handle, eg, wsgid.serve_forever()
    """
    logging.basicConfig(level=LVL_NAME)
    wsgi_handler = GetServerWSGI(port, wapp, validate=validate)
    return wsgi_handler


def wsgi_run(app=demo_app, port=PORT):  # pragma: no cover
    """
    Run in foreground command wrapper for console entry point;
    init logging and server, run the server, stop the server.

    :param iface: server listen interface
    :param port: server listen port
    """
    wsgid = wsgi_init(port, app, True)
    logging.info('Serving %s on port %s', DOCROOT, port)
    try:
        wsgid.start()
        wsgid.join()
    except KeyboardInterrupt:
        print("\nExiting ...")
        wsgid.stop()


def main(args=None):  # pragma: no cover
    """
    The serv entry point wrapper; both args are optional, but you must
    provide either APP or APP *and* PORT.

    Usage::

      wsgi [APP] [PORT]
    """
    if args is None:
        args = sys.argv[1:]

    app = sys.argv[1] if len(sys.argv) > 1 else demo_app
    wport = sys.argv[2] if len(sys.argv) > 2 else PORT

    wsgi_run(app, int(wport))


if __name__ == '__main__':  # pragma: no cover
    sys.exit(main())
