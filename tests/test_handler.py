import pathlib
import sys
import unittest
import urllib.request

import httptest
import pytest

from pyserv import GetHandler

FILE_PATH = pathlib.Path(__file__)
REAL_PATH = pathlib.Path('requirements.txt')


class TestHTTPHandler(unittest.TestCase):

    @pytest.mark.skipif(sys.version_info < (3, 7), reason="requires python3.7 or higher")
    @httptest.Server(
        lambda *args: GetHandler(
            *args, directory=FILE_PATH.parent
        )
    )
    def test_call_response_dir(self, ts=httptest.NoServer()):
        with urllib.request.urlopen(ts.url() + FILE_PATH.name) as f:
            self.assertEqual(f.read().decode('utf-8'), FILE_PATH.read_text())

    @httptest.Server(GetHandler)
    def test_url(self, ts=httptest.NoServer()):
        '''
        Make sure the Server.url() method works.
        '''
        url = ts.url()
        self.assertIn(':', url)
        self.assertEqual(':'.join(url.split(':')[:-1]), 'http://localhost')

    @httptest.Server(GetHandler)
    def test_call_response_no_dir(self, ts=httptest.NoServer()):
        with urllib.request.urlopen(ts.url() + REAL_PATH.name) as f:
            self.assertEqual(f.read().decode('utf-8'), REAL_PATH.read_text())


if __name__ == '__main__':
    unittest.main()
