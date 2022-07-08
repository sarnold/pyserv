# -*- coding: utf-8 -*-
import pathlib
import unittest
import urllib.request

import httptest

from pyserv import GetHandler

FILE_PATH = pathlib.Path(__file__)

class TestHTTPTestMethods(unittest.TestCase):

    @httptest.Server(
        lambda *args: GetHandler(
            *args, directory=FILE_PATH.parent
        )
    )
    def test_call_response(self, ts=httptest.NoServer()):
        with urllib.request.urlopen(ts.url() + FILE_PATH.name) as f:
            self.assertEqual(f.read().decode('utf-8'), FILE_PATH.read_text())

if __name__ == '__main__':
    unittest.main()
