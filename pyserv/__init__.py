"""
Simple HTTP server classes with GET path rewriting and request/header logging.
"""

import logging
import sys
import threading
from functools import partial
from http.server import HTTPServer, SimpleHTTPRequestHandler
from socketserver import ThreadingMixIn
from urllib.parse import urlparse
from wsgiref.simple_server import make_server
from wsgiref.validate import validator

from ._version import __version__

VERSION = __version__

__all__ = ["__version__", "VERSION", "GetHandler", "GetServer"]


def munge_url(ota_url):
    """
    Parse the url sent by OTA command for file path and host string.

    :param ota_url: (possibly) broken GET path
    :return tuple: netloc and path from ``urlparse``
    """
    url_data = urlparse(str(ota_url))
    file_path = url_data.path
    host_str = url_data.netloc
    logging.debug('request file: %s', file_path.lstrip("/"))
    logging.debug('request host: %s', host_str if host_str else 'None')
    return host_str, file_path


class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    """
    Backwards-compatible server class for Python <3.7 on older distros,
    eg, Ubuntu bionic LTS.
    """


class GetHandler(SimpleHTTPRequestHandler):
    """
    Munge the incoming request path from Dialog OTA. Runs `urlparse` on
    the url and updates the GET handler path. We also log the result.

    :param SimpleHTTPRequestHandler: imported from `http.server`
    """

    def do_GET(self):
        logging.debug('Thread name: %s', threading.current_thread().name)
        logging.debug('Thread count: %s', threading.active_count())
        logging.info('Path in: %s', self.path)
        _, file_path = munge_url(self.path)
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


class GetServer(threading.Thread):
    """
    Threaded wrapper class for custom ThreadingHTTPServer instance.

    Usage::

        s = GetServer('', 8080)
        s.start()
        s.stop()
    """

    def __init__(self, iface, port, directory):
        """Setup server, iface, and port"""
        super().__init__()
        self.iface = iface
        self.port = int(port)
        self.directory = directory
        if sys.version_info < (3, 7):
            self.handler = GetHandler
        else:
            self.handler = partial(GetHandler, directory=self.directory)
        self.server = ThreadingHTTPServer((self.iface, self.port), self.handler)

    def run(self):
        """Start main server thread"""
        self.server.serve_forever()

    def stop(self):
        """Stop main server thread"""
        self.server.shutdown()
        self.server.socket.close()


class GetServerWSGI(threading.Thread):
    """
    Threaded wrapper class for custom flask WSGIServer instance.

    Usage::

        s = GetServerWSGI(my_app, 8080, is_flask=True, validate=False)
        s.start()
        s.stop()
    """

    def __init__(self, port, flask_app, is_flask=False, validate=False):
        super().__init__()
        self.port = int(port)
        self.app = flask_app
        if validate:
            self.app = validator(flask_app)
        self.server = make_server('', self.port, self.app)
        if is_flask:
            self.context = flask_app.app_context()
            self.context.push()

    def run(self):
        """Start main server thread"""
        self.server.serve_forever()

    def stop(self):
        """Stop main server thread"""
        self.server.shutdown()
