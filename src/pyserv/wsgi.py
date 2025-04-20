"""
Simple WSGI server for serving swagger or basic flask apps in an engineering
development environment.
"""

import logging
import os
import sys
from wsgiref.simple_server import demo_app

from . import GetServerWSGI
from .settings import DEBUG, DOCROOT, PORT

LVL_NAME = 'DEBUG' if DEBUG else 'INFO'
LOG = os.getenv('LOG', default='')
logger = logging.getLogger(__name__)


def wsgi_init(wapp, port, validate=True):
    """
    Init wsgi server for handler handoff; init logging and simple_server
    classes.

    :param wapp: initialized WSGI app to run
    :param port: initialized listen port
    :return wsgi_handler: wsgi handle, eg, wsgid.serve_forever()
    """
    wsgi_handler = GetServerWSGI(wapp, port, validate=validate)
    return wsgi_handler


def wsgi_run(app=demo_app, port=PORT):  # pragma: no cover
    """
    Run in foreground command wrapper for WSGI console entry point;
    init logging and server, run the server, stop the server.

    :param app: WSGI app (defaults to ``demo_app`` if not provided)
    :param port: WSGI server listen port
    """
    wsgid = wsgi_init(app, port, True)
    logger.info('Serving %s on port %s', DOCROOT, port)
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
    if LOG:
        logging.basicConfig(filename=LOG, level=LVL_NAME)
    else:
        logging.basicConfig(level=LVL_NAME)

    if args is None:
        args = sys.argv[1:]

    app = sys.argv[1] if len(sys.argv) > 1 else demo_app
    wport = sys.argv[2] if len(sys.argv) > 2 else PORT

    wsgi_run(app, int(wport))


if __name__ == '__main__':  # pragma: no cover
    sys.exit(main())
