import logging
import secrets
import datetime as dt
import time as tm

log_file = '/var/log/nc_scripts.log'
debug = False

if debug:
    logging.basicConfig(filename=log_file, level=logging.DEBUG)
else:
    logging.basicConfig(filename=log_file, level=logging.INFO)


def time():
    now = dt.datetime.now()
    return now.strftime("%Y/%m/%d %H:%M:%S")


def time_string(ident):
    return " " + str(time()) + " ** " + ident + " ** : "


def begin(description):
    """
    Function that creates an identification number
    """
    ident = secrets.token_hex(4)
    msg = time_string() + description
    logging.info(msg)
    return ident


def debug(ident, msg):
    """
    Print debug level messages
    """
    logging.debug(time_string(ident) + str(msg))


def info(ident, msg):
    """
    Print info level messages
    """
    logging.info(time_string(ident) + str(msg))


def warning(ident, msg):
    """
    Print warning level messages
    """
    logging.warning(time_string() + str(msg))


def error(ident, msg):
    """
    Print error level messages
    """
    logging.error(time_string() + str(msg))