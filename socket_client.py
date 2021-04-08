import socket
import os
import sys


ip = socket.gethostname()
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(("192.168.0.148", 1234))

while True:
    data = server.recv(8)
    print(data)
