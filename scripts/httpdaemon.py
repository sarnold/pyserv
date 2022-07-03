#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import logging
import sys
import threading
from datetime import timezone
from http.server import ThreadingHTTPServer

from daemon import Daemon
from daemon.parent_logger import setup_logging

from pyserv.server import GetHandler
from pyserv.settings import (
    DEBUG,
    HOMEDIR,
    IFACE,
    LOGDIR,
    LOGFILE,
    PIDDIR,
    PIDFILE,
    PORT,
    init_dirs,
)

user_dirs = [LOGDIR, PIDDIR]
logger = logging.getLogger(__name__)
timestamp = datetime.datetime.now(timezone.utc)  # use local time for console


class GetServer(threading.Thread):
    """
    Threaded wrapper class for custom ThreadingHTTPServer instance.
    Usage:
        s = GetServer('', 8080)
        s.start()
        s.stop()
    """

    def __init__(self, iface, port):
        """Setup iface and port"""
        super().__init__()
        self.iface = iface
        self.port = int(port)
        self.server = ThreadingHTTPServer((self.iface, self.port), GetHandler)

    def run(self):
        """Start the server thread"""
        self.server.serve_forever()

    def stop(self):
        """Stop the server thread"""
        self.server.shutdown()
        self.server.socket.close()


class servDaemon(Daemon):
    def run(self):
        """Daemon needs a run method"""
        servd = GetServer(IFACE, PORT)
        servd.start()

    def cleanup(self):
        """Cleanup is optional"""
        servd.stop()


if __name__ == "__main__":
    init_dirs(user_dirs)
    setup_logging(DEBUG, LOGFILE, 'servd')

    if len(sys.argv) == 2:
        arg = sys.argv[1]
        if arg in ('start', 'stop', 'restart', 'status'):
            d = servDaemon(PIDFILE, home_dir=HOMEDIR, verbose=0, use_cleanup=True)
            getattr(d, arg)()
    else:
        print("usage: %s start|stop|restart|status" % sys.argv[0])
        sys.exit(2)
