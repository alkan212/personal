import socket
import os
import sys


ip = socket.gethostname()
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((ip, 1234))

