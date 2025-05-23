"""
Simple TFTP server for serving kernels or swupdate images in an engineering
development environment.
"""

import logging
import os
import sys

import tftpy

from .settings import DEBUG, DOCROOT, IFACE

LOG = os.getenv('LOG', default='')
PORT = os.getenv('PORT', default='9069')
LVL_NAME = 'DEBUG' if DEBUG == '1' else 'INFO'
logger = logging.getLogger(__name__)


# disable these globally:Similar lines
#
# pylint: disable=R0801


def tftpd_init(directory):
    """
    Init tftpd server for handoff; init logging.

    :param directory: server root directory
    :return tftpd_server: tftpd server obj
    """
    tftpd_server = tftpy.TftpServer(directory)
    return tftpd_server


def tftpd_run(iface=IFACE, port=PORT, directory=DOCROOT):  # pragma: no cover
    """
    Run in foreground command wrapper for TFTP console entry point;
    init server listening, run the server, stop the server.

    :param iface: server listen interface (default: all)
    :param port: server listen port (default: 8069)
    :param directory: server root directory  (default: DOCROOT)
    """
    tftpd = tftpd_init(directory)
    try:
        tftpd.listen(iface, int(port))
        logger.info('Serving %s on port %d', directory, int(port))
    except tftpy.TftpException as err:
        logger.critical("Server listen error: %s", str(err))
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
    if LOG:
        logging.basicConfig(filename=LOG, level=LVL_NAME)
    else:
        logging.basicConfig(level=LVL_NAME)

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
