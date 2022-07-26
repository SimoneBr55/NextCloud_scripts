#!/usr/bin/python3
"""
Module that allows simple parsing of OS commands from python

AUTHOR: Simone Brazioli
"""

import subprocess
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
            outline = p.stdout.readline()
            if not outline:
                break
            if outline.strip() != "":
                output.appen(outline.strip())
    except Exception as inst:
        print("Call process error:", str(inst))  # add to log
    return output

