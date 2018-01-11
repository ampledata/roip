#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python Radio Over IP Module.

"""
Python Radio Over IP Module.
~~~~


:author: Greg Albrecht W2GMD <oss@undef.net>
:copyright: Copyright 2018 Orion Labs, Inc.
:license: Apache License, Version 2.0
:source: <https://github.com/ampledata/roip>

"""

from .constants import (LOG_FORMAT, LOG_LEVEL, READ_SIZE, PTT_START,  # NOQA
                        PTT_STOP, COR_START, COR_STOP)

from .classes import RoIP  # NOQA

__author__ = 'Greg Albrecht W2GMD <oss@undef.net>'  # NOQA pylint: disable=R0801
__copyright__ = 'Copyright 2018 Orion Labs, Inc.'  # NOQA pylint: disable=R0801
__license__ = 'Apache License, Version 2.0'  # NOQA pylint: disable=R0801
