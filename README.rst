=====================
 HTTPD Python Server
=====================

|ci| |wheels| |release| |badge|

|pylint|

|tag| |license| |python|

A Python HTTP server to handle simple GET requests for local files that
also provides logging of requests/headers and an extra "feature" to handle
(broken) clients that send the full URL instead of the GET file path.

Quick Start
===========

Install with pip
----------------

This updated fork of pyserv is *not* published on PyPI, thus use one of
the following commands to install the latest pyserv in a Python virtual
environment on any platform.

From source::

  $ python3 -m venv env
  $ source env/bin/activate
  $ pip install git+https://github.com/sarnold/pyserv.git
  $ serv 8080

The output should be::

  INFO:root:Starting HTTP SERVER at PORT 8080

To install the latest release use this::

  $ pip install -U -f https://github.com/sarnold/pyserv/releases/ pyserv

The alternative to python venv is the ``tox`` test driver.  If you have it
installed already, clone this repository and try the following commands
from the pyserv source directory.

To install in dev mode::

  $ tox -e py

To run pylint::

  $ tox -e lint


.. note:: After installing in dev mode, use the environment created by
          Tox just like any other Python virtual environment.  The dev
          install mode of Pip allows you to edit the script and run it
          again while inside the virtual environment. By default Tox
          environments are created under ``.tox/`` and named after the
          env argument (eg, py).


GET request example
-------------------

Open a new terminal and try out sending a GET request::

  $ python
  >>> import requests
  >>> URL = 'http://0.0.0.0:8080'
  >>> r = requests.get(URL)
  >>> print(r.text)
  GET request for /

On the server side, ie, inside your virtual environment, you should see:

::

  INFO:root:Path: /
  INFO:root:Headers:
  Host: 0.0.0.0:8080
  User-Agent: python-requests/2.25.1
  Accept-Encoding: gzip, deflate
  Accept: */*
  Connection: keep-alive



  127.0.0.1 - - [24/Jun/2022 21:23:07] "GET / HTTP/1.1" 200 -


If no port is provided the server attempts to run on port 8080.

If the given port (or the default port 8080) is already in use, you will
need to pass a different port number, eg, 8088.

Motivation:

Small device firmware with non-compliant HTTP client implementations.

Original project from gist: https://pypi.org/project/pyserv/

Original gist: https://gist.github.com/mdonkers/63e115cc0c79b4f6b8b3a6b797e485c7


.. |ci| image:: https://github.com/sarnold/pyserv/actions/workflows/ci.yml/badge.svg
    :target: https://github.com/sarnold/pyserv/actions/workflows/ci.yml
    :alt: CI Status

.. |wheels| image:: https://github.com/sarnold/pyserv/actions/workflows/wheels.yml/badge.svg
    :target: https://github.com/sarnold/pyserv/actions/workflows/wheels.yml
    :alt: Wheel Status

.. |badge| image:: https://github.com/sarnold/pyserv/actions/workflows/pylint.yml/badge.svg
    :target: https://github.com/sarnold/pyserv/actions/workflows/pylint.yml
    :alt: Pylint Status

.. |release| image:: https://github.com/sarnold/pyserv/actions/workflows/release.yml/badge.svg
    :target: https://github.com/sarnold/pyserv/actions/workflows/release.yml
    :alt: Release Status

.. |pylint| image:: https://raw.githubusercontent.com/sarnold/pyserv/badges/main/pylint-score.svg
    :target: https://github.com/sarnold/pyserv/actions/workflows/pylint.yml
    :alt: Pylint score

.. |license| image:: https://img.shields.io/github/license/sarnold/pyserv
    :target: https://github.com/sarnold/pyserv/blob/master/LICENSE
    :alt: License

.. |tag| image:: https://img.shields.io/github/v/tag/sarnold/pyserv?color=green&include_prereleases&label=latest%20release
    :target: https://github.com/sarnold/pyserv/releases
    :alt: GitHub tag

.. |python| image:: https://img.shields.io/badge/python-3.6+-blue.svg
    :target: https://www.python.org/downloads/
    :alt: Python

.. |pre| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit
