FROM python:3-stretch
ARG github_token
ENV github_token=$github_token

RUN apt-get update
#RUN apt-get install -y libopus-dev flite flite-dev sox python-pip lame libyaml-dev git
RUN apt-get install -y libusb-dev libusb-1.0-0-dev libudev1 libudev-dev

RUN pip install hidapi
