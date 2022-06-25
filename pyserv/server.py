#!/usr/bin/env python3

"""
Simple HTTP server with broken GET rewriting for serving FW upgrades.
"""

import logging
import sys
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
from urllib.parse import urlparse


class GetHandler(SimpleHTTPRequestHandler):
    """
    Wrapper class to munge the incoming request path from Dialog OTA.
    Runs `urlparse` on the url and updates the GET handler path.
    """
    def do_GET(self):
        logging.info('Path in: %s', self.path)
        _, file_path = parse_url(self.path)
        self.path = file_path  # pylint: disable=W0201
        logging.info('Path out: %s', self.path)
        logging.info('Headers:\n%s\n', self.headers)
        SimpleHTTPRequestHandler.do_GET(self)


def parse_url(ota_url):
    """
    Parse the url sent by OTA command for file path and netloc.
    :param ota_url: broken GET path if full url
    :return tuple: netloc and path from ``urlparse``
    """
    get_data = urlparse(str(ota_url))
    file_path = get_data.path
    host_str = get_data.netloc
    logging.debug('request file: %s', file_path.lstrip("/"))
    logging.debug('request host: %s', host_str)
    return host_str, file_path


def run(server_class=TCPServer, handler_class=GetHandler, port=8080):
    """
    Run command wrapper for console entry point; init logging and server,
    run the server, stop the server.
    :param server_class: should be TCPServer
    :param handler_class: the GetHandler wrapper
    :param port: server listen port
    """
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting HTTP SERVER at PORT %s', port)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()
    logging.info('Stopping httpd...\n')


def main(args=None):
    """The entry point wrapper."""
    if args is None:
        args = sys.argv[1:]

    if len(args) == 1:
        run(port=int(args[0]))
    else:
        run()


if __name__ == '__main__':
    sys.exit(main())
