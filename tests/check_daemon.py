"""
Tiny client to make a web request to port 8080.
"""

import logging
import os
import time

import requests

iface = '0.0.0.0'
port = 8080


def get_request(port, iface):
    """Test serv client"""
    URL = f'http://{iface}:{port}/'
    r = requests.get(URL)
    print(f'Got request status {r.reason,} from {r.url}')
    return r

if __name__ == '__main__':
    res = get_request(port, iface)
