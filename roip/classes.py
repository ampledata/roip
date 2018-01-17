#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Python Radio Over IP Module Class Definitions."""

from typing import List, Set, Dict, Tuple, Text, Optional, AnyStr

import hidapi  # type: ignore

import roip  # pylint: disable=R0801

__author__ = 'Greg Albrecht W2GMD <oss@undef.net>'  # NOQA pylint: disable=R0801
__copyright__ = 'Copyright 2018 Orion Labs, Inc.'  # NOQA pylint: disable=R0801
__license__ = 'Apache License, Version 2.0'  # NOQA pylint: disable=R0801


class RoIP(object):

    """Class for Radio Over IP interfaces."""

    def __init__(self, device: tuple) -> None:
        self.device: tuple = device
        self.hid_device = None

    def __del__(self):
        if self.hid_device is not None:
            self.close()

    def open(self) -> None:
        """Opens the connection to the RoIP device."""
        self.hid_device = hidapi.hid_open(self.device[0], self.device[1])

    def close(self) -> None:
        """Closes the connection to the RoIP device."""
        self.hid_device = hidapi.hid_close(self.device[0], self.device[1])

    def ptt(self, callback=None) -> None:
        """
        [TX] Initiates a Transmission cycle on the Radio.

        Calls a callback (if specified) between Start and Stop of PTT.

        :param callback: Callback function to call (if specified).
        :type callback: def
        """
        self.ptt_start()
        callback()
        self.ptt_stop()

    def ptt_start(self) -> int:
        """[TX] Triggers Transmit on the Radio."""
        wrote = hidapi.hid_write(self.hid_device, roip.PTT_START)
        return wrote

    def ptt_stop(self) -> int:
        """[TX] Stops Transmit on the Radio."""
        wrote = hidapi.hid_write(self.hid_device, roip.PTT_START)
        return wrote

    def cor(self) -> bool:
        """
        [RX] Detects if there's a signal from the Radio.

        Blocks until a signal is received from the Radio.
        """
        hid_read = hidapi.hid_read(self.hid_device, roip.READ_SIZE)

        cor_status: bool = False
        if roip.COR_START in hid_read:
            cor_status = True
        elif roip.COR_STOP in hid_read:
            cor_status = False

        return cor_status

    # TODO: finish this:
    def cor_nb(self, timeout=0.01) -> bool:
        """
        [RX] Detects if there's a signal from the Radio.

        Non-blocking, returns after a timeout even if there's no signal from
        the Radio.
        """
        hid_read = hidapi.hid_read(self.hid_device, roip.READ_SIZE)

        cor_status: bool = False
        if roip.COR_START in hid_read:
            cor_status = True
        elif roip.COR_STOP in hid_read:
            cor_status = False

        return cor_status
