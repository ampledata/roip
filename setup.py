#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Setup for the Python Radio Over IP Module.

:author: Greg Albrecht W2GMD <oss@undef.net>
:copyright: Copyright 2018 Orion Labs, Inc.
:license: Apache License, Version 2.0
:source: <https://github.com/ampledata/roip>
"""

import os
import sys

import setuptools  # type: ignore

__title__ = 'roip'
__version__ = '0.0.1b3'
__author__ = 'Greg Albrecht W2GMD <oss@undef.net>'  # NOQA pylint: disable=R0801
__copyright__ = 'Copyright 2018 Orion Labs, Inc.'  # NOQA pylint: disable=R0801
__license__ = 'Apache License, Version 2.0'  # NOQA pylint: disable=R0801


def publish():
    """Function for publishing package to pypi."""
    if sys.argv[-1] == 'publish':
        os.system('python setup.py sdist')
        os.system('twine upload dist/*')
        sys.exit()


publish()


setuptools.setup(
    name=__title__,
    version=__version__,
    description='Python Radio Over IP Module.',
    author='Greg Albrecht',
    author_email='oss@undef.net',
    packages=['roip'],
    package_data={'': ['LICENSE']},
    package_dir={'roip': 'roip'},
    license=open('LICENSE').read(),
    long_description=open('README.rst').read(),
    url='https://github.com/ampledata/roip',
    zip_safe=False,
    include_package_data=True,
    tests_require=[
        'coverage >= 4.4.1',
        'nose >= 1.3.7'
    ],
    install_requires=['pyhidapi'],
    classifiers=[
        'Topic :: Communications :: Ham Radio',
        'Programming Language :: Python',
        'License :: OSI Approved :: Apache Software License'
    ],
    keywords=[
        'Ham Radio', 'APRS', 'KISS', 'RoIP'
    ]
)
