#!/usr/bin/python
"""
Module that performs low level functions to transfer files. It contains both the server and client code.

AUTHOR: Simone Brazioli
"""


import pysftp


def send_file(source, destination, username, hostname, key_path):
    """
    This function allows to send file to remote host.
    :source: String path
    :destination: String path
    :username: String dest username
    :hostname: String FQDN to connect
    :key_path: local SSH key used to connect
    """

    # start the connection
    sftp = pysftp.Connection(host=hostname, username=username, private_key=key_path)

    with sftp.cd(destination):
        sftp.put(source)


def get_file(source, destination, username, hostname, key_path):
    """
    This function allows to get file from remote host.
    :source: String path
    :destination: String path
    :username: String dest username
    :hostname: String FQDN to connect
    :key_path: local SSH key used to connect
    """

    sftp = pysftp.Connection(host=hostname, username=username, private_key=key_path)

    with sftp.cd(destination):
        sftp.get(source)
