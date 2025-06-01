from time import sleep

import pytest

from pyserv import RepeatTimer


def rt_target():
    """
    Small test func for timer test.
    """
    print("Yay")


def test_repeat_timer():
    """
    Test timer thread can start and stop; partially verifies TUI_005.
    """
    test_rt = RepeatTimer(1.0, rt_target)
    assert test_rt.is_running
    test_rt.stop()
    assert not test_rt.is_running
    test_rt.start()
    sleep(0.1)
    assert test_rt.is_running
    test_rt.stop()
    assert test_rt.is_running is False
    test_rt._run()
    assert test_rt.is_running
    test_rt.stop()
