#!/usr/bin/python

import lib.transfer as transfer
import lib.os_control as osctl
import os
from pathlib import Path
from os import remove  # can be discarded in favour of the following command
from shutil import rmtree


DEBUG = True
RSYNC = True

check = open('/tmp/check_upload', 'w')

# style of creds:
# [0] -> username
# [1] -> hostname
# [2] -> location of key
# [3] -> SSH Port
creds = []  # in second version implement a dictionary, to prevent wrong order
with open("./list_creds.txt", "r") as file:
    for line in file:
        line = line.strip()
        creds.append(line)

username = creds[0]
hostname = creds[1]
loc_key = creds[2]
port = creds[3]

dirs = []  # init list of folders to send over
with open("./list_sync.txt", "r") as file:
    for line in file:
        line = line.strip()
        dirs.append(line)

if DEBUG:
    print(dirs)
    print(creds)

# now in dirs, I have `source,destination` as each entry of the list

# now I have to iterate through dirs, to separate source and destination and work on those

for operation in dirs:
    source, destination = operation.split(',')

    # I now have a source and a destination strings

    if os.path.basename(source) == os.path.basename(destination):
        # maybe there's a bug hidden here
        destination = os.path.dirname(destination)
    if RSYNC:
        transfer.get_file_rsync(source, destination, username, hostname, loc_key, port)
        # we will not delete these, since we are using rsync here, the folder will be kept in sync
    else:
        # to simplify (and speed up) the process i am going to tarball and gzip them
        new_location = osctl.compress(source)
        transfer.send_file_sftp(new_location, destination, username, hostname, loc_key, port)
        # now we have to delete the `.tar.gz`
        remove(new_location)
        # still undecided if removing the original folder/file is something wise
        # rmtree(source)
    if DEBUG:
        print("SRC: " + source + " - DEST: " + destination)
        print("SRC: " + os.path.basename(source) + " - DEST: " + os.path.basename(destination))
        print("SRC: " + os.path.dirname(source) + " - DEST: " + os.path.dirname(destination))
    osctl.exec_command("chown -R www-data:www-data " + destination + "/" + os.path.basename(source))
    check.write(source)

check.close()
# osctl.exec_command("nc-scan simone")

#transfer.send_file_sftp('/tmp/check_upload', '/tmp', username, hostname, loc_key, port)

os.remove('/tmp/check_upload')

