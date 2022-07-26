#!/usr/bin/python

import lib.transfer as transfer
import lib.os_control as osctl

dirs = []  # list of folders to send over
with open("./list_sync.txt") as file:
    for line in file:
        line = line.strip()
        dirs.append(line)

# i now have a dirs list of folders to backup

# to simplify (and speed up) the process i am going to tarball and gzip them

for folder in dirs:
    osctl.compress(folder)