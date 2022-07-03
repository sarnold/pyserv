#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Simple HTTP server with broken GET rewriting for serving FW upgrades or
other local files in an engineering development environment.
"""

import logging
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse


class GetHandler(SimpleHTTPRequestHandler):
    """
    Munge the incoming request path from Dialog OTA. Runs `urlparse` on
    the url and updates the GET handler path.

    :param SimpleHTTPRequestHandler: imported from `http.server`
    """

    def do_GET(self):
        logging.info('Path in: %s', self.path)
        _, file_path = parse_url(self.path)
        self.path = file_path  # pylint: disable=W0201
        logging.info('Path out: %s', self.path)
        logging.info('Headers:')
        for key, val in self.headers.items():
            logging.info('  %s: %s', key, val)
        SimpleHTTPRequestHandler.do_GET(self)


def parse_url(ota_url):
    """
    Parse the url sent by OTA command for file path and netloc.

    :param ota_url: broken GET path if full url
    :return tuple: netloc and path from `urlparse`
    """
    get_data = urlparse(str(ota_url))
    file_path = get_data.path
    host_str = get_data.netloc
    logging.debug('request file: %s', file_path.lstrip("/"))
    logging.debug('request host: %s', host_str if host_str else 'None')
    return host_str, file_path


def serv_init(iface, port, server_class=ThreadingHTTPServer, handler_class=GetHandler):
    """
    Init http server for handoff; init logging and server/handler classes.

    :param iface: server listen interface
    :param port: server listen port
    :param server_class: imported from `http.server` or `socketserver`
    :param handler_class: the `GetHandler` wrapper
    :return httpd_handler: httpd handle, eg, httpd.serve_forever()
    """
    logging.basicConfig(level=logging.INFO)
    server_address = (iface, port)
    httpd_handler = server_class(server_address, handler_class)
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
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Exiting ...")
        httpd.shutdown()
        httpd.socket.close()


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
