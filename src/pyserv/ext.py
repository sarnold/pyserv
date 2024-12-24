"""
Pyserv default args for async tftp daemon.
"""
import argparse

from pyserv import __version__

EPILOG = """
Copyright 2016 Matt O. <matt@mattscodecave.com>
"""


def parse_cli_arguments():
    """
    Daemon needs a less closely-coupled bit of args.
    """
    daemon_args = ['start', 'stop', 'restart', 'status']

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description='Async TFTP server daemon',
    )
    parser.add_argument(
        "--version", action="version", version=f"atftpdaemon {__version__}"
    )
    parser.add_argument(
        '--host',
        default='',
        help=('IP of the interface the server will listen on. ' 'Default: 0.0.0.0'),
    )
    parser.add_argument(
        '-p',
        '--port',
        default=9069,
        type=int,
        help=(
            'Port the server will listen on. '
            'Default: 9069. TFTP standard-compliant port: 69 - '
            'requires additional privileges.'
        ),
    )
    parser.add_argument(
        '--ack-timeout',
        dest="timeout",
        default=0.5,
        type=float,
        help='Timeout for each ACK of the lock-step. Default: 0.5.',
    )
    parser.add_argument(
        '--conn-timeout',
        default=5.0,
        type=float,
        help=(
            'Timeout before the server gives up on a transfer and closes '
            'the connection. Default: 3.'
        ),
    )
    parser.add_argument(
        '-v', '--verbose', action='store_true', help='Enable debug-level logging.'
    )
    parser.add_argument(
        '-q', '--quiet', action='store_true', help='Inhibit extra console output.'
    )
    parser.add_argument('run', choices=daemon_args, nargs=1)

    args = parser.parse_args()

    return args
