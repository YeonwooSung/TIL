#!/bin/bash

# Scan all ports that are used by running processes.
# By using this script, you could get a list of processes that are "LISTENING" to the specific port.
sudo lsof -i -P | grep LISTEN
