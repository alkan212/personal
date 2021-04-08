import socket
import os
import sys



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 1234))
server.listen(5)

while True:
    connection , address = server.accept()
    print("connected with", address)

