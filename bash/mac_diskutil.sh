#!/bin/bash

# list all disks
diskutil list

# erase everything in disk2
diskutil eraseDisk JHFS+ MacOS /dev/disk2
