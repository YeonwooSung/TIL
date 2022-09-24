#!/bin/bash

# make new service -> /lib/systemd/system/myservice.service

# reload daemon
systemctl daemon-reload

# enable myservice
systemctl enable myservice
# start myservice
systemctl start myservice
# stop myservice
systemctl stop myservice
# disable myservice
systemctl disable myservice

