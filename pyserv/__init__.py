# -*- coding: utf-8 -*-
import http.server
import logging
import threading
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse

from pyserv._version import __version__

VERSION = __version__

__description__ = "Simple HTTP server with GET rewriting and request/header logging."

__all__ = ["__description__", "__version__", "VERSION", "GetHandler", "GetServer"]


class GetHandler(SimpleHTTPRequestHandler):
    """
    Munge the incoming request path from Dialog OTA. Runs `urlparse` on
    the url and updates the GET handler path.

    :param SimpleHTTPRequestHandler: imported from `http.server`
    """

    def do_GET(self):
        logging.info('Path in: %s', self.path)
        _, file_path = self.parse_url(self.path)
        self.path = file_path  # pylint: disable=W0201
        logging.info('Path out: %s', self.path)
        logging.info('Headers:')
        for key, val in self.headers.items():
            logging.info('  %s: %s', key, val)
        SimpleHTTPRequestHandler.do_GET(self)

    def log_message(self, format, *args):  # pylint: disable=W0622
        """
        We need a custom log handler, otherwise Get message goes to
        `sys.stdout` only.
        """
        logging.info(
            "%s - - [%s] %s",
            self.address_string(),
            self.log_date_time_string(),
            format % args,
        )

    def parse_url(self, ota_url):
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


class GetServer(threading.Thread):
    """
    Threaded wrapper class for custom ThreadingHTTPServer instance.
    Usage::

        s = GetServer('', 8080)
        s.start()
        s.stop()
    """

    def __init__(self, iface, port):
        """Setup server, iface, and port"""
        super().__init__()
        self.iface = iface
        self.port = int(port)
        self.server = ThreadingHTTPServer((self.iface, self.port), GetHandler)

    def run(self):
        """Start main server thread"""
        self.server.serve_forever()

    def stop(self):
        """Stop main server thread"""
        self.server.shutdown()
        self.server.socket.close()
