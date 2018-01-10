#!/usr/bin/env bash

for x in $(egrep -vi '(^#|^$)' requirements.txt); do
  pip install -e $(echo $x|sed s{+ssh://git@{+https://$(github_token){g);
done
