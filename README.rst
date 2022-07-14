===========================
 Pyserv Simple HTTP Server
===========================

|ci| |wheels| |release| |badge| |coverage|

|pre| |cov| |pylint|

|tag| |license| |python|

A `Python HTTP server`_ to handle simple GET requests for local files that
provides logging of requests/headers and an extra "feature" to handle
(broken) clients that send the full URL instead of the GET file path.

.. important:: This is **not** intended for Internet/intranet use and
  has absolutely **no** security. This is intended mainly for personal
  use on a local subnet, eg, a local WIFI network *you* control. You
  have been warned.

.. _Python HTTP server: https://docs.python.org/3/library/http.server.html

Quick Start
===========

The primary reason this version of the "project" exists is serving OTA_
firmware images to a small device over wifi, eg, an Android device or
similar that requires an HTTP URL for firmware img/zip files. If that
is what you need, then make sure the FW update files you want are in
a directory in your virtual environment and run the ``serv`` command
from that directory.  The simple way to do that is:

* follow the steps below to create a virtual env (either venv or tox)
* connect your dev host to the same wifi network as the device
* copy your FW files into the source directory, then start the server

In another terminal, run your update command and provide a URL like this::

  http://<dev_host_wifi_IP>:PORT/fw_update.img

where ``PORT`` is the port used below and ``fw_update.img`` is the name
of your OTA update file.

.. _OTA: https://en.wikipedia.org/wiki/Over-the-air_programming

Console command options
-----------------------

This package now installs two different command line interfaces;
the ``serv`` command mentioned above, and a second  command
called ``httpdaemon``.  The ``serv`` command is the standard Python
console entry point, and has these minimal "features":

* the document root is always the current directory
* with no args, the default port is ``8080`` and the "server" listens
  on *all* active interfaces
* the *only* allowed args are either port, or port *and* interface

The ``httpdaemon`` command is a stand-alone `Python daemon`_ with the same
core server code, as well as a default user configuration adjustable via
environment variables, and the following "extra" features:

* allowed command-line args are ``start | stop | restart | status``
* default port is ``8080`` and listen interface is ``127.0.0.1``
* default XDG user paths are set for pid and log files
* environment values are checked first; if not set, fallback to defaults
* clean logging using daemon package logger config

Sample environment display with tox overrides, ie, inside a Tox_ venv::

  Python version: 3.9.7 (default, Mar 19 2022, 18:11:11)
  [GCC 11.1.0]
  ----------------------------------------------------------------------
  pyserv 1.2.2.dev5

  Pyserv default settings for daemon mode.

  Default user vars:
    log_dir: /home/user/.cache/pyserv/1.2.2.dev5/log
    pid_dir: /home/user/.cache/pyserv/1.2.2.dev5/run
    doc_dir: /home/user/src/pyserv

  Current environment values:
    DEBUG: 1
    PORT: 8080
    IFACE: 127.0.0.1
    LOG: /home/user/src/pyserv/.tox/dev/log/httpd.log
    PID: /home/user/src/pyserv/.tox/dev/tmp/httpd.pid
    DOCROOT: /home/user/src/pyserv
  ----------------------------------------------------------------------

Use any of the variables under "Current environment values" to set your
own custom environment.

Daemon usage
------------

Once installed in a virtual environment, check the ``help`` output::

  $ httpdaemon -h
  usage: httpdaemon [-h] [--version] {start,stop,restart,status}

  Threaded HTTP server daemon

  positional arguments:
    {start,stop,restart,status}

  optional arguments:
    -h, --help            show this help message and exit
    --version             show program's version number and exit


**One small wrinkle**

* the ``httpdaemon`` script *will not* run on Windows, however,
  the ``serv`` command should work fine

.. _Python daemon: https://github.com/sarnold/python-daemonizer


Install with pip
----------------

This refactored fork of pyserv is *not* published on PyPI, thus use one of
the following commands to install the latest pyserv in a Python virtual
environment on any platform.

From source::

  $ python3 -m venv env
  $ source env/bin/activate
  $ pip install git+https://github.com/sarnold/pyserv.git
  $ serv 8000

The output should be::

  INFO:root:Starting HTTP SERVER at PORT :8000

The alternative to python venv is the Tox_ test driver.  If you have it
installed already, clone this repository and try the following commands
from the pyserv source directory.

To install in dev mode::

  $ tox -e dev

To run tests using default system Python::

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

In the repo, use the tox env and start the server::

  $ tox -e py
  $ source .tox/py/bin/activate
  (py) $ serv
  INFO:root:Starting HTTP SERVER at :8080

Open a new terminal and try out sending a GET request::

  $ python
  >>> import requests
  >>> URL = 'http://0.0.0.0:8080'
  >>> r = requests.get(URL)
  >>> print(r.text)
  <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">

On the server side, ie, inside your virtual environment, you should see:

::

  INFO:root:Starting HTTP SERVER at :8080
  INFO:root:Path in: /
  INFO:root:Path out: /
  INFO:root:Headers:
  INFO:root:  Host: 0.0.0.0:8080
  INFO:root:  User-Agent: python-requests/2.25.1
  INFO:root:  Accept-Encoding: gzip, deflate
  INFO:root:  Accept: */*
  INFO:root:  Connection: keep-alive
  INFO:root:127.0.0.1 - - [13/Jul/2022 20:52:22] "GET / HTTP/1.1" 200 -


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

.. |coverage| image:: https://github.com/sarnold/pyserv/actions/workflows/coverage.yml/badge.svg
    :target: https://github.com/sarnold/pyserv/actions/workflows/coverage.yml
    :alt: Coverage workflow

.. |badge| image:: https://github.com/sarnold/pyserv/actions/workflows/pylint.yml/badge.svg
    :target: https://github.com/sarnold/pyserv/actions/workflows/pylint.yml
    :alt: Pylint Status

.. |release| image:: https://github.com/sarnold/pyserv/actions/workflows/release.yml/badge.svg
    :target: https://github.com/sarnold/pyserv/actions/workflows/release.yml
    :alt: Release Status

.. |cov| image:: https://raw.githubusercontent.com/sarnold/pyserv/badges/master/test-coverage.svg
    :target: https://github.com/sarnold/pyserv/
    :alt: Test coverage

.. |pylint| image:: https://raw.githubusercontent.com/sarnold/pyserv/badges/master/pylint-score.svg
    :target: https://github.com/sarnold/pyserv/actions/workflows/pylint.yml
    :alt: Pylint score

.. |license| image:: https://img.shields.io/github/license/sarnold/pyserv
    :target: https://github.com/sarnold/pyserv/blob/master/LICENSE
    :alt: License

.. |tag| image:: https://img.shields.io/github/v/tag/sarnold/pyserv?color=green&include_prereleases&label=latest%20release
    :target: https://github.com/sarnold/pyserv/releases
    :alt: GitHub tag

.. |python| image:: https://img.shields.io/badge/python-3.7+-blue.svg
    :target: https://www.python.org/downloads/
    :alt: Python

.. |pre| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit
