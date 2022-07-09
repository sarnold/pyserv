# -*- coding: utf-8 -*-
import os
import threading
import time

import requests

from pyserv import GetServer, munge_url
from pyserv import settings as cfg
from pyserv.server import *

iface = '127.0.0.1'
port = 8000


def get_request(port, iface):
    """Test serv client"""
    URL = f'http://{iface}:{port}'
    r = requests.get(URL)
    return r


def test_get_server_attrs():
    """Test GetServer attrs """

    serv_thread = GetServer(iface, port)
    assert isinstance(serv_thread, GetServer)
    assert hasattr(serv_thread, 'start')
    assert hasattr(serv_thread, 'stop')


def test_serv_init():
    """Test serv_init wrapper"""

    serv_thread = serv_init(iface, port)
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
