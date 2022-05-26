#!/bin/bash

cat /etc/issue
# Ubuntu 16.04.1 LTS \n \l

cat /etc/*release
# DISTRIB_ID=Ubuntu
# DISTRIB_RELEASE=16.04
# ...
# PRETTY_NAME="Ubuntu 16.04.1 LTS"
# VERSION_ID="16.04"
# ...
# UBUNTU_CODENAME=xenial

lsb_release -a
# No LSB modules are available.
# Distributor ID:	Ubuntu
# Description:	Ubuntu 16.04.1 LTS
# Release:	16.04
# Codename:	xenial