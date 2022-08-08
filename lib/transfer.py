#!/usr/bin/python
"""
Module that performs low level functions to transfer files. It contains both the server and client code.

AUTHOR: Simone Brazioli
"""


import pysftp
import lib.os_control as osctl
from os import remove



def send_file_sftp(source, destination, username, hostname, key_path=None, port=None):
    """
    This function allows to send file to remote host.
    :source: String path
    :destination: String path
    :username: String dest username
    :hostname: String FQDN to connect
    :key_path: local SSH key used to connect
    """

    if key_path is None:
        key_path = "/root/.ssh/id_rsa"
    if port is None:
        port = 22

    # start the connection
    sftp = pysftp.Connection(host=hostname, username=username, private_key=key_path, port=port)

    with sftp.cd(destination):
        sftp.put(source)


def send_file_rsync(source, destination, username, hostname, key_path=None, port=None):
    """
    This function allows to rsync two remote folders. For now, you have to specify a destination without last folder.
    In the future, a check will be added to remove the last folder (maybe, if it is the same as the last folder of source).
    This is the subroutine to send FROM local TO remote
    """
    base_command = "rsync"
    if key_path is None:
        key_path = '/root/.ssh/id_rsa'
    if port is None:
        port = 22
    subcommand = " -e 'ssh -i " + key_path + " -p " + str(port) + " ' "
    options = "-aP"
    folder = source
    dest = username + "@" + hostname + ":" + destination
    full_command = base_command + subcommand + options + " " + folder + " " + dest
    output = osctl.exec_command(full_command)
    return output


def get_file_rsync(source, destination, username, hostname, key_path=None, port=None):
    """
    This function allows to rsync two remote folders. For now, you have to specify a destination without last folder.
    In the future, a check will be added to remove the last folder (maybe, if it is the same as the last folder of source).
    This is the subroutine to send FROM remote TO local
    """
    base_command = "rsync"
    if key_path is None:
        key_path = '/root/.ssh/id_rsa'
    if port is None:
        port = 22
    subcommand = " -e 'ssh -i " + key_path + " -p " + str(port) + " ' "
    options = "-aP"
    folder = username + "@" + hostname + ":" + source
    dest = destination
    full_command = base_command + subcommand + options + " " + folder + " " + dest
    print(full_command)
    output = osctl.exec_command(full_command)
    return output


def get_file_sftp(source, destination, username, hostname, key_path=None, port=None):
    """
    This function allows to get file from remote host.
    :source: String path
    :destination: String path
    :username: String dest username
    :hostname: String FQDN to connect
    :key_path: local SSH key used to connect
    """

    # sftp = pysftp.Connection(host=hostname, username=username, private_key=key_path)

    # with sftp.cd(destination):
    #    sftp.get(source)
    return None
