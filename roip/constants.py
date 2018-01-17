#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Python Radio Over IP Module Constants."""

import logging
import os

__author__ = 'Greg Albrecht W2GMD <oss@undef.net>'  # NOQA pylint: disable=R0801
__copyright__ = 'Copyright 2018 Orion Labs, Inc.'  # NOQA pylint: disable=R0801
__license__ = 'Apache License, Version 2.0'  # NOQA pylint: disable=R0801


if bool(os.environ.get('DEBUG')):
    LOG_LEVEL = logging.DEBUG
    logging.debug('Debugging Enabled via DEBUG Environment Variable.')
else:
    LOG_LEVEL = logging.INFO

LOG_FORMAT = logging.Formatter(
    ('%(asctime)s roip %(levelname)s %(name)s.%(funcName)s:%(lineno)d - '
     '%(message)s'))

READ_SIZE = 5

PTT_START = bytearray(b'\x00\x00\x04\x04\x00')
PTT_STOP = bytearray(b'\x00\x00\x00\x00\x00')

COR_START = bytearray(b'\x02\x00\x00\x00')
COR_STOP = bytearray(b'\x00\x00\x00\x00')
