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

.. highlight:: python
    :linenothreshold: 5

    import os

    import roip

    # 0x0D8C:0X013A is our C-Media CM1xx Soundcard
    usb_dev: tuple = (0x0D8C, 0x013A)

    roip_dev: roip.RoIP = roip.RoIP(usb_dev)
    roip_dev.open()

    # Trigger a PTT and play an audio file (via SoX's `aplay`):
    roip_dev.ptt(callback=lambda: os.system('aplay cw_id.wav'))

    # Start a loop and record 10 seconds every time there's an incoming signal:
    started = False
    while 1:
        cor = roip_dev.cor()
        if cor:
            if started:
                print('Incoming signal, continuing recording...')
            elif not started:
                print('Incoming signal, beginning recording.')
                started = True
                os.system('rec signal.wav trim 0 10')
        elif not cor:
            if started:
            print('Incoming signal stopped, stopping recording.')
            started = False

    roip_dev.close()


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
