import os
import threading
import time

import requests

import pyserv
from pyserv import GetHandler, GetServer, munge_url
from pyserv.server import *

directory = '.'
iface = '127.0.0.1'
port = 8000


def get_request(port, iface):
    """Test serv client"""
    URL = f'http://{iface}:{port}'
    r = requests.get(URL)
    return r


def test_get_handler_attrs():
    """Test GetHandler attrs """

    handler = GetHandler
    assert hasattr(handler, 'do_GET')
    assert hasattr(handler, 'log_message')


def test_get_server_attrs():
    """Test GetServer attrs """

    serv_thread = GetServer(iface, port, directory)
    assert isinstance(serv_thread, GetServer)
    assert hasattr(serv_thread, 'start')
    assert hasattr(serv_thread, 'stop')


def test_serv_init():
    """Test serv_init wrapper"""

    serv_thread = serv_init(iface, port, directory)
    assert isinstance(serv_thread, GetServer)
    assert hasattr(serv_thread, 'start')
    assert hasattr(serv_thread, 'stop')


def test_munge_url():
    """Make sure URLs are properly munged"""

    paths = [
        "/my_fw_update1.img",
        "http://127.0.0.1:8000/my_fw_update1.img",
    ]

    for ota_url in paths:
        _, get_path = munge_url(ota_url)
        assert get_path == "/my_fw_update1.img"
