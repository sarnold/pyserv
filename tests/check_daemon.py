"""
Tiny client to make a web request to port 8080.
"""

import logging
import os
import time

import requests

from pyserv.settings import PORT

iface = '0.0.0.0'


def get_request(iface, port):
    """Test serv client"""
    URL = f'http://{iface}:{port}/'
    r = requests.get(URL)
    print(f'Got request status {r.reason,} from {r.url}')
    print(r.text.splitlines()[0])
    return r


if __name__ == '__main__':
    res = get_request(iface, port=PORT)
