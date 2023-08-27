"""
Simple TFTP server for serving swupdate images or basic tasks in an engineering
development environment.
"""

import logging
import os
import sys

import tftpy

from .settings import DEBUG, DOCROOT

LVL_NAME = 'DEBUG' if DEBUG else 'INFO'
IFACE = os.getenv('IFACE', default='')
PORT = os.getenv('PORT', default='8069')


def tftpd_init(directory):
    """
    Init tftpd server for handoff; init logging.

    :param directory: server root directory
    :return tftpd_server: tftpd obj, eg, tftpd.listen()
    """
    logging.basicConfig(level=LVL_NAME)
    tftpd_server = tftpy.TftpServer(directory)
    return tftpd_server


def tftpd_run(iface='', port=8069, directory=DOCROOT):  # pragma: no cover
    """
    Run in foreground command wrapper for TFTP console entry point;
    init server listening, run the server, stop the server.

    :param app: WSGI app (defaults to ``demo_app`` if not provided)
    :param port: WSGI server listen port
    """
    tftpd = tftpd_init(directory)
    try:
        tftpd.listen(iface, port)
        logging.info('Serving %s on port %s', directory, port)
    except tftpy.TftpException as err:
        sys.stderr.write("%s\n" % str(err))
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nExiting ...")
        tftpd.stop()


def main(args=None):  # pragma: no cover
    """
    The serv entry point wrapper; both args are optional, but you must
    provide either IFACE or IFACE *and* PORT.

    Usage::

      tftpd [IFACE] [PORT]
    """
    if args is None:
        args = sys.argv[1:]

    if len(args) == 1:
        tftpd_run(iface=args[0])
    elif len(args) == 2:
        tftpd_run(iface=args[0], port=int(args[1]))
    else:
        tftpd_run()


if __name__ == '__main__':  # pragma: no cover
    sys.exit(main())
