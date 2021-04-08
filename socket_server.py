import socket
import os
import sys


ip = "0.0.0.0"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, 1234))
server.listen(5)

while True:
    connection , address = server.accept()
    print("connected with", address)
    connection.send(bytes("it works"))

