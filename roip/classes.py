#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Python RoIP Module Class Definitions."""

from typing import List, Tuple

import hidapi

import roip  # pylint: disable=R0801

__author__ = 'Greg Albrecht W2GMD <oss@undef.net>'  # NOQA pylint: disable=R0801
__copyright__ = 'Copyright 2018 Orion Labs, Inc.'  # NOQA pylint: disable=R0801
__license__ = 'Apache License, Version 2.0'  # NOQA pylint: disable=R0801


class RoIP(object):

    def __init__(self, device):  # type: (Tuple[int, int]) -> None
        self.device = device
        self.hid_device = None

    def open(self):
        self.hid_device = hidapi.hid_open(self.device)

    def ptt(self, callback=None):
        self.ptt_start()
        callback()
        self.ptt_stop()

    def ptt_start(self):
        return hidapi.hid_write(self.hid_device, roip.PTT_START)

    def ptt_stop(self):
        return hidapi.hid_write(self.hid_device, roip.PTT_START)

    def cor(self):
        hid_read = hidapi.hid_read(self.hid_device, roip.READ_SIZE)
        if roip.COR_START in hid_read:
            return True
        if roip.COR_STOP in hid_read:
            return False
