"""
FTP Server

Student ID: p2227168
Name:       Andrew Poh
Class:      DISM/FT/1B/01
Assessment: CA1-2

Script Name:
    ftp_server.py

Purpose:
    Runs FTP server for ftp_client.py to access

Usage syntax:
    Run via main menu

Input file:
    None

Output file:
    None

Python ver:
    Python 3

Reference:
    None

Library/Module:
    Install pyftpdlib package - pip install pyftpdlib
"""

# Ref: 
# https://pyftpdlib.readthedocs.io/en/latest/tutorial.html
# https://pyftpdlib.readthedocs.io/en/latest/api.html

# Need to pip install pyftpdlib
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

import pathlib
pwd = str(pathlib.Path(__file__).parent.resolve()) + '\\'

# Instantiate a dummy authorizer for managing 'virtual' users
authorizer = DummyAuthorizer() # handle permission and user

# Define an anonymous user and home directory having read permissions
authorizer.add_anonymous(pwd + 'ftpServerData\\', perm='lrw')

# Instantiate FTP handler class
handler = FTPHandler #  understand FTP protocol
handler.authorizer = authorizer

# Instantiate FTP server class and listen on 127.0.0.1:2121
address = ('127.0.0.1', 2121)
server = FTPServer(address, handler)

# start ftp server
server.serve_forever()