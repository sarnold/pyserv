#!/usr/bin/env python3

import logging
import sys

from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
from pathlib import Path
from urllib.parse import urlparse


class GetHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        # self.send_response(200, self.headers)
        # for h in self.headers:
            # self.send_header(h, self.headers[h])
        # self.end_headers()
        logging.info(self.headers)
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)


def parse_url(ota_url):
    """
    Parse the url sent by OTA command for file path and netloc.
    """
    get_data = urlparse(str(ota_url))
    file_path = get_data.path
    host_str = get_data.netloc
    print("request file was {}\n".format(file_path.lstrip("/")))
    print("request host was {}\n".format(host_str))
    return host_str, file_path


def run(server_class=TCPServer, handler_class=GetHandler, port=8080):

    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info(f'Starting HTTP SERVER at PORT {port}')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()
    logging.info('Stopping httpd...\n')


def main(args=None):
    """The main wrapper."""
    if args is None:
        args = sys.argv[1:]

    if len(args) == 1:
        run(port=int(args[0]))
    else:
        run()


if __name__ == '__main__':
    sys.exit(main())
