#!/usr/bin/python3
"""
Module that allows simple parsing of OS commands from python

AUTHOR: Simone Brazioli
"""

import subprocess
import os
# import logger

def exec_command(command):
    # init log 
    """
    Function that executes a CLI commands and returns a list of output
    """
    output = []
    try:
        process = subprocess.Popen(command, shell=True, executable='/bin/bash', stdout=subprocess.PIPE, env=None, universal_newlines=True)
        while True:
            outline = process.stdout.readline()
            if not outline:
                break
            if outline.strip() != "":
                output.append(outline.strip())
    except Exception as inst:
        print("Call process error:", str(inst))  # add to log
    return output

def compress(source, destination=None):
    if destination is None:
        destination = source + ".tar.gz"
    root, filename = os.path.split(source)
    filename_tarball = str(filename) + ".tar"
    # 2 issues with the following commands:
    #   1) we are assuming that we are sufficient space available to store all the copies
    #   2) we can implement the string check at the beginning...
    exec_command("cd " + str(root) + " ; tar cvf " + str(filename_tarball) + " " + str(source))