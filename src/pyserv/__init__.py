"""
Simple HTTP server classes with GET path rewriting and request/header logging.
Now includes a reference WSGI server and tftpdaemon script.
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

if sys.version_info < (3, 8):
    from importlib_metadata import version
else:
    from importlib.metadata import version

__version__ = version('pyserv')
__all__ = [
    "__description__",
    "__version__",
    "GetHandler",
    "GetServer",
    "GetServerWSGI",
    "RepeatTimer",
    "munge_url",
]
__description__ = "A collection of simple servers for HTTP, WSGI, and TFTP"


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

    def __init__(self, iface, port, directory="."):
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

    def __init__(self, flask_app, port, is_flask=False, validate=False):
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


class RepeatTimer:
    """
    A non-blocking threaded timer to execute a user func repeatedly.
    Usage::

        def hello(name):
            print(f"Hello {name}")

        rt = RepeatTimer(1, hello, "World")  # it auto-starts
        try:
            sleep(5)  # run other stuff
        finally:
            rt.stop()  # best in a try/finally block

    Author: https://stackoverflow.com/a/38317060/14874218
    """

    def __init__(self, interval, function, *args, **kwargs):
        self._timer = None
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        """
        Safely (re)start thread timer.
        """
        if not self.is_running:
            self._timer = threading.Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        """
        Safely stop thread timer.
        """
        self._timer.cancel()
        self.is_running = False
