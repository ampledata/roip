FROM python:3-stretch
ARG github_token
ENV github_token=$github_token

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
