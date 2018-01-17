roip - Python Radio Over IP (RoIP) Module
*****************************************

For use with Radio Over IP (RoIP) interfaces for sending and receiving
transmissions from a Land Mobile Radio (LMR).

Compatible with **most** C-Media CM108 and CM119 chipset-based boards, such as:

* Master Communications RA-40 [tested!] - http://www.masterscommunications.com/products/radio-adapter/ra40.html
* USHAM ARiUSB [tested!] - http://usham.net/
* DMK Engineering URIx - http://dmkeng.com/URI_Order_Page.htm
* Repeater Builder RB-USB RIM - http://www.repeater-builder.com/products/usb-rim.html
* Repeater Builder RB-USB Lite - http://www.repeater-builder.com/products/usb-rim-lite.html

Usage
=====

>>> import os
>>> import roip
>>> usb_dev: tuple = (0x0d8c, 0x013a)
>>> roip_dev = roip.RoIP(usb_dev)
>>> roip_dev.open()
>>> roip_dev.ptt(callback=lambda: os.system('aplay cw_id.wav'))
>>> started: bool = False
>>> while 1:
...     if roip_dev.cor():
...         if started:
...             print('Incoming signal, continuing recording.')
...         elif not started:
...             print('Incoming signal, beginning recording.')
...             os.system('rec signal.wav trim 0 10')
...             started = True
...     elif not roip_dev.cor():
...         if started:
...             print('Incoming signal stopped, stopping recording.')
...             started = False
>>>

Build Status
============

Master:

.. image:: https://travis-ci.org/ampledata/roip.svg?branch=master
    :target: https://travis-ci.org/ampledata/roip

Develop:

.. image:: https://travis-ci.org/ampledata/roip.svg?branch=develop
    :target: https://travis-ci.org/ampledata/roip


Source
======
Github: https://github.com/ampledata/roip

Author
======
Greg Albrecht W2GMD oss@undef.net

http://ampledata.org/

Copyright
=========
Copyright 2018 Orion Labs, Inc.

License
=======
Apache License, Version 2.0. See LICENSE for details.
