#!/bin/bash

FILE=/tmp/check_upload
while [ ! -f "$FILE"]
do
  sleep 5;
done

# if I am here, it means that the python uploader has created the check file
sleep 5
rm -r "$FILE"

# sposto file

# cambio permessi

# aggiungo file check per segnalare ad altri script, che il processo è concluso
touch /tmp/done_upload