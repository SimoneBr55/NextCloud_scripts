#!/usr/bin/python3
from os.path import exists
from os import remove
from time import sleep


FILE = '/tmp/check_upload'
while not exists(FILE):
    sleep(5)

# if I am here, it means that the python uploader has created the check file
# let's wait some more time
sleep(5)

# remove the check file, so long as I am now working on it
remove(FILE)

os.rename()


# sposto file

# cambio permessi

# aggiungo file check per segnalare ad altri script, che il processo è concluso
touch /tmp/done_upload