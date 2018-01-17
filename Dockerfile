# Dockerfile for Python Radio Over IP Module.
#
# Source:: https://github.com/ampledata/roip
# Author:: Greg Albrecht W2GMD <oss@undef.net>
# Copyright:: Copyright 2018 Orion Labs, Inc.
# License:: Apache License, Version 2.0
#


FROM python:3-stretch

RUN apt-get update
RUN apt-get install -y \
  libusb-dev \
  libusb-1.0-0-dev \
  libudev1 \
  libudev-dev \
  autotools-dev \
  autoconf \
  automake \
  libtool

RUN git clone https://github.com/signal11/hidapi.git
RUN git clone https://github.com/NF6X/pyhidapi.git

WORKDIR /hidapi
RUN ./bootstrap
RUN ./configure
RUN make
RUN make install

WORKDIR /pyhidapi
RUN python setup.py install
