=====================
 HTTPD Python Server
=====================

|ci| |wheels| |release| |badge|

|pre| |pylint|

|tag| |license| |python|

A Python_ HTTP server to handle simple GET requests for local files that
also provides logging of requests/headers and an extra "feature" to handle
(broken) clients that send the full URL instead of the GET file path.

.. important:: This is **not** intended for Internet/intranet use and
              has absolutely **no** security. This is intended *only*
              for personal use on a local subnet, eg, a local WIFI
              network *you* control. You have been warned.

.. _Python: https://docs.python.org/3/library/http.server.html

Quick Start
===========

The primary reason this version of the "project" exists is serving OTA_
firmware images to a small device over wifi, eg, an Android device or
similar that requires an HTTP URL for firmware img/zip files. If that
is what you need, then make sure the FW update files you want are in
a directory in your virtual environment and run the server from that
directory.  The simple way to do that is:

* follow the steps below to create a virtual env (either venv or tox)
* connect your dev host to the same wifi network as the device
* copy your FW files into the source dir, then start the server

Then run your update command and provide a URL something like::

  http://<dev_host_wifi_IP>:PORT/fw_update.img

where ``PORT`` is the port used below and ``fw_update.img`` is the name
of your OTA update file.

.. _OTA: https://en.wikipedia.org/wiki/Over-the-air_programming

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

The alternative to python venv is the Tox_ test driver.  If you have it
installed already, clone this repository and try the following commands
from the pyserv source directory.

To install in dev mode::

  $ tox -e py

To run pylint::

  $ tox -e lint


.. note:: After installing in dev mode, use the environment created by
          Tox just like any other Python virtual environment.  The dev
          install mode of Pip allows you to edit the code and run it
          again while inside the virtual environment. By default Tox
          environments are created under ``.tox/`` and named after the
          env argument (eg, py).


To install the latest release, eg with your own ``tox.ini`` file in
another project, use something like this::

  $ pip install -U -f https://github.com/sarnold/pyserv/releases/ pyserv


.. _Tox: https://github.com/tox-dev/tox


GET request example
-------------------

Open a new terminal and try out sending a GET request::

  $ python
  >>> import requests
  >>> URL = 'http://0.0.0.0:8080'
  >>> r = requests.get(URL)
  >>> print(r.text)
  <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">

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


Pre-commit
----------

This repo is now pre-commit_ enabled for python/rst source and file-type
linting. The checks run automatically on commit and will fail the commit
(if not clean) and perform simple file corrections.  For example, if the
mypy check fails on commit, you must first fix any fatal errors for the
commit to succeed. That said, pre-commit does nothing if you don't install
it first (both the program itself and the hooks in your local repository
copy).

You will need to install pre-commit before contributing any changes;
installing it using your system's package manager is recommended,
otherwise install with pip into your usual virtual environment using
something like::

  $ sudo emerge pre-commit  --or--
  $ pip install pre-commit

then install it into the repo you just cloned::

  $ git clone https://github.com/sarnold/pyserv
  $ cd pyserv/
  $ pre-commit install

It's usually a good idea to update the hooks to the latest version::

    $ pre-commit autoupdate

Most (but not all) of the pre-commit checks will make corrections for you,
however, some will only report errors, so these you will need to correct
manually.

Automatic-fix checks include ffffff, isort, autoflake, and miscellaneous
file fixers. If any of these fail, you can review the changes with
``git diff`` and just add them to your commit and continue.

If any of the mypy, bandit, or rst source checks fail, you will get a report,
and you must fix any errors before you can continue adding/committing.

To see a "replay" of any ``rst`` check errors, run::

  $ pre-commit run rst-backticks -a
  $ pre-commit run rst-directive-colons -a
  $ pre-commit run rst-inline-touching-normal -a

To run all ``pre-commit`` checks manually, try::

  $ pre-commit run -a

.. _pre-commit: https://pre-commit.com/index.html


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

.. |pylint| image:: https://raw.githubusercontent.com/sarnold/pyserv/badges/master/pylint-score.svg
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
