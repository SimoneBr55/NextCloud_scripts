#!/usr/bin/python
import time

import lib.transfer as transfer
import lib.os_control as osctl
import os
import time
import lib.private_functions as private
import lib.logger as log

from pathlib import Path
from os import remove  # can be discarded in favour of the following command
from shutil import rmtree

ident = log.begin("Periodic Download")

DEBUG = True
RSYNC = True
MANAGED = True

check = open('/tmp/check_upload', 'w')

# style of creds:
# [0] -> username
# [1] -> hostname
# [2] -> location of key
# [3] -> SSH Port


username = private.creds[0]
hostname = private.creds[1]
loc_key = private.creds[2]
port = private.creds[3]

if MANAGED:
    server_status = private.ping(hostname)
    if not server_status:
        status = private.wakeonlan(hostname)
        if status != 1:
            log.error(ident, status)
            exit(SystemError)
        iter = 0
        server_status = private.ping(hostname)
        while server_status != True and iter <= 6:
            server_status = private.ping(hostname)
            iter += 1
            time.sleep(10)
        if iter > 6:
            log.error(ident, "Server has not booted up")
            exit(SystemError)
        time.sleep(10)


if DEBUG:
    print(private.dirs)
    print(private.creds)

# now in dirs, I have `source,destination` as each entry of the list

# now I have to iterate through dirs, to separate source and destination and work on those

for operation in private.dirs:
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
    # osctl.exec_command("chown -R www-data:www-data " + destination + "/" + os.path.basename(source))  # temp
    check.write(source)

check.close()

if MANAGED:
    status = private.halt(hostname)
    if status != 1:
        log.error(ident, status)

# osctl.exec_command("nc-scan simone")

#transfer.send_file_sftp('/tmp/check_upload', '/tmp', username, hostname, loc_key, port)

os.remove('/tmp/check_upload')

