#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Python Radio Over IP Module Class Definitions."""

import logging

from typing import List, Set, Dict, Tuple, Text, Optional, AnyStr

import hidapi  # type: ignore

import roip  # pylint: disable=R0801

__author__ = 'Greg Albrecht W2GMD <oss@undef.net>'  # NOQA pylint: disable=R0801
__copyright__ = 'Copyright 2018 Orion Labs, Inc.'  # NOQA pylint: disable=R0801
__license__ = 'Apache License, Version 2.0'  # NOQA pylint: disable=R0801


class RoIP(object):

    """Class for Radio Over IP interfaces."""

    _logger = logging.getLogger(__name__)
    if not _logger.handlers:
        _logger.setLevel(roip.LOG_LEVEL)
        _console_handler = logging.StreamHandler()
        _console_handler.setLevel(roip.LOG_LEVEL)
        _console_handler.setFormatter(roip.LOG_FORMAT)
        _logger.addHandler(_console_handler)
        _logger.propagate = False

    def __init__(self, device: tuple) -> None:
        self._logger.debug('device="%s"', device)
        self.device: tuple = device
        self.hid_device = None

    def __del__(self):
        if self.hid_device is not None:
            self.close()

    def open(self) -> None:
        """Opens the connection to the RoIP device."""
        hidapi.hid_init()
        self.hid_device = hidapi.hid_open(self.device[0], self.device[1])
        self._logger.info('Opened hid_device="%s"', self.hid_device)

    def close(self) -> None:
        """Closes the connection to the RoIP device."""
        self.hid_device = hidapi.hid_close(self.hid_device)

    def ptt(self, callback=None) -> None:
        """
        [TX] Initiates a Transmission cycle on the Radio.

        Calls a callback (if specified) between Start and Stop of PTT.

        :param callback: Callback function to call (if specified).
        :type callback: def
        """
        self._logger.info('Transmitting...')
        self._logger.debug('callback="%s"', callback)
        wrote_start = self.ptt_start()
        if not wrote_start:
            raise 'Unable to Stop PTT. '

        callback()

        wrote_stop = self.ptt_stop()
        if not wrote_stop:
            raise 'Unable to Stop PTT. '

    def ptt_start(self) -> int:
        """[TX] Triggers Transmit on the Radio."""
        start = roip.PTT_START
        wrote = hidapi.hid_write(self.hid_device, start)
        self._logger.debug('start="%s" wrote="%s"', start, wrote)
        assert len(start) == wrote
        return wrote

    def ptt_stop(self) -> int:
        """[TX] Stops Transmit on the Radio."""
        stop = roip.PTT_STOP
        wrote = hidapi.hid_write(self.hid_device, stop)
        self._logger.debug('stop="%s" wrote="%s"', stop, wrote)
        assert len(stop) == wrote
        return wrote


    def cor(self) -> bool:
        """
        [RX] Detects if there's a signal from the Radio.

        Blocks until a signal is received from the Radio.
        """
        cor_status: bool = False

        hid_read = hidapi.hid_read(self.hid_device, roip.READ_SIZE)
        self._logger.debug('read="%s"', hid_read)

        if roip.COR_START in hid_read:
            cor_status = True
        elif roip.COR_STOP in hid_read:
            cor_status = False

        self._logger.debug('cor_status="%s"', cor_status)
        return cor_status

    # TODO: finish this:
    def cor_nb(self, timeout=100) -> bool:
        """
        [RX] Detects if there's a signal from the Radio.

        Non-blocking, returns after a timeout even if there's no signal from
        the Radio.
        """
        cor_status: bool = False

        hid_read = hidapi.hid_read_timeout(
            self.hid_device, roip.READ_SIZE, timeout)
        self._logger.debug('read="%s"', hid_read)

        if roip.COR_START in hid_read:
            cor_status = True
        elif roip.COR_STOP in hid_read:
            cor_status = False

        self._logger.debug('cor_status="%s"', cor_status)
        return cor_status
