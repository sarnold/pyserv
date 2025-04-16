"""Server console UI for pyserv daemon scripts"""

import os
import pprint
import sys
from collections import deque
from pprint import pprint

from picotui.context import Context
from picotui.menu import *
from picotui.widgets import *

# Dialog on the screen
d = None
denv = {}
httpd_env = {
    "DEBUG": "0",
    "PORT": "8080",
    "IDEV": "eth0",
    "IFACE": "0.0.0.0",
    "LPNAME": "httpd",
    "DOCROOT": ".",
}
tftpd_env = {
    "DEBUG": "0",
    "PORT": "9069",
    "IDEV": "eth0",
    "IFACE": "0.0.0.0",
    "LPNAME": "tftpd",
    "DOCROOT": ".",
    "SOCK_TIMEOUT": "5",
}


def update_env(src, dest):
    """
    Update UI env settings.
    """


def get_w_env(env):
    """
    Get UI widget settings from env values.
    """
    w_list = ["DEBUG", "PORT", "IDEV", "IFACE", "SOCK_TIMEOUT"]
    w_env = {k: v for k, v in env.items() if k in w_list}
    return w_env


def get_env(name):
    """
    Get environment data from selected name.
    """
    env = {}
    if name.startswith('httpd'):
        env.update(httpd_env)
    elif name.startswith('tftpd'):
        env.update(tftpd_env)
    else:
        tftpd_env["LPNAME"] = 'atftpd'
        env.update(tftpd_env)
    return env


def tail(iterable, N):
    """
    Queue for tailing log ouput.
    """
    tailq = deque()
    for thing in iterable:
        if len(tailq) >= N:
            tailq.popleft()
        tailq.append(thing)
    yield from tailq


def get_log_tail(log_file, num_lines=10):
    """
    Get lines from tail queue for display.
    """
    with open(log_file, 'r') as f_log:
        lines = []
        for line in tail(f_log, num_lines):
            lines.append(line)
        return lines


def screen_resize(s):
    """This routine is called on screen resize"""
    global d
    # Widgets in dialog store absolute screen coordinates, so
    # we need to recreate it from scratch for new dimensions.
    d = create_dialog()
    screen_redraw(s)


# This routine is called to redraw screen
def screen_redraw(s):
    """This routine is called to redraw screen"""
    global d
    s.attr_color(C_WHITE, C_BLUE)
    s.cls()
    s.attr_reset()
    d.redraw()


# init starting values
T_EXIT = False
DAEMON_NAME = 'tftpdaemon'
DAEMON_ENV = get_env(DAEMON_NAME)
# PORT_ENTRY = DAEMON_ENV["PORT"]
# IFACE_ENTRY = DAEMON_ENV["IFACE"]
# IDEV_ENTRY = DAEMON_ENV["IDEV"]


def create_dialog():
    """Creates base settings dialog with usage and navigation buttons."""
    width, height = Screen.screen_size()

    d = Dialog((width - 70) // 2, (height - 22) // 2, 70, 22)

    d.add(20, 1, WLabel("Server console UI", w=20))
    d.add(40, 1, WLabel("v0.0.1", w=10))

    d.add(2, 3, "Use <TAB> to move between fields and arrow keys to select from")
    d.add(2, 4, "multiple options. Use <SPACE> for checkbox, <ENTER> for buttons.")

    b = WButton(8, "Next")
    d.add(10, 20, b)
    b.finish_dialog = ACTION_OK

    b = WButton(8, "Cancel")
    d.add(52, 20, b)
    b.finish_dialog = ACTION_CANCEL

    return d


def create_run_dialog():
    """Creates base settings dialog with just title and navigation buttons."""
    width, height = Screen.screen_size()

    d = Dialog((width - 70) // 2, (height - 22) // 2, 70, 22)

    d.add(20, 1, WLabel("Server operations UI", w=20))

    b = WButton(8, "Back")
    d.add(10, 20, b)
    b.finish_dialog = ACTION_OK

    b = WButton(8, "Exit")
    d.add(52, 20, b)
    b.finish_dialog = ACTION_CANCEL

    return d


while not T_EXIT:
    # init UI
    with Context():
        d = create_dialog()

        d.add(3, 6, WFrame(30, 6, "Server type"))
        d.add(4, 7, "Select daemon name")
        w_radio = WRadioButton(["tftpdaemon", "atftpdaemon", "httpdaemon"])
        d.add(5, 8, w_radio)

        d.add(35, 6, WFrame(32, 9, "Env settings"))
        d.add(36, 7, "Update daemon defaults")
        w_checkbox = WCheckbox("Debug")
        d.add(37, 8, w_checkbox)

        d.add(37, 9, "Port: ")
        w_port_entry = WTextEntry(5, DAEMON_ENV["PORT"])
        d.add(45, 9, w_port_entry)

        d.add(37, 10, "Device: ")
        w_idev_entry = WTextEntry(15, DAEMON_ENV["IDEV"])
        d.add(45, 10, w_idev_entry)

        d.add(37, 11, "Listen: ")
        w_iface_entry = WTextEntry(15, DAEMON_ENV["IFACE"])
        d.add(45, 11, w_iface_entry)

        def checkbox_changed(w):
            """Update holding env on checkbox change"""
            denv["DEBUG"] = '1' if w.get() else '0'

        def radio_changed(w):
            """Update env and entry widgets on radio button change"""
            dname = w.items[w.choice]
            val = '8080' if dname.startswith('http') else '9069'
            w_port_entry.set(val)
            w_port_entry.redraw()
            denv["PORT"] = val
            denv["LPNAME"] = dname.split('a')[0]

        w_checkbox.on("changed", checkbox_changed)
        w_radio.on("changed", radio_changed)

        screen_redraw(Screen)
        Screen.set_screen_redraw(screen_redraw)
        Screen.set_screen_resize(screen_resize)

        # somewhat silly hack to both move the first widget *and* avoid
        # a TypeError in widget move_focus
        d.move_focus(1 or None)
        d.move_focus(1 or None)
        res = d.loop()

        # without a changed(w) func, updates happen *after* the loop call
        DAEMON_NAME = w_radio.items[w_radio.choice]
        # we need to pass the name from the selection widget
        DAEMON_ENV = get_env(DAEMON_NAME)
        if denv:
            DAEMON_ENV.update(denv)

    if res == ACTION_CANCEL:
        print("Canceled...")
        pprint(denv)
        sys.exit(1)

    os.environ.update(DAEMON_ENV)
    denv.clear()

    with Context():
        d = create_run_dialog()

        d.add(2, 3, "Use the <Start> <Stop> <Status> buttons to operate the server")
        d.add(2, 5, WFrame(66, 11, "Logs:"))

        b = WButton(8, "Start")
        d.add(15, 17, b)

        b = WButton(8, "Stop", color=C_MAGENTA)
        d.add(31, 17, b)

        b = WButton(8, "Status", color=C_YELLOW)
        d.add(47, 17, b)

        screen_redraw(Screen)
        Screen.set_screen_redraw(screen_redraw)
        Screen.set_screen_resize(screen_resize)

        res = d.loop()

        if res == ACTION_CANCEL:
            break

print("Exiting...")
pprint(DAEMON_ENV)

sys.exit(0)
