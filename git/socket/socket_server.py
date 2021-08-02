import socket
import os
import sys
import threading
from time import sleep
import base64


 
data = ""
clients = []

def connect():
    global clients
    while True:
        
        ip = "0.0.0.0"

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((ip, 1268))
        server.listen(5)

        connection , address = server.accept()
        clients.append({"connection":connection,"address":address})

        print("connected with", address)


def send_data():
    global data
    while True:

        data = bytes(input(""), "utf-8")
        for index, client in enumerate(clients):
            try:
                client["connection"].send(data)
            except:
                print(client["address"], "diconnected \n")
                clients.pop(index)



def recv_data():
    global client
    while True:
   
        for index, client in enumerate(clients):
            try:
                data = client["connection"].recv(1024).decode("ISO-8859-1")
                data = data.replace("ÿ", " ")
                if len(data) > 0:
                    print(client["address"]," : ", data)
            except:
                print(client["address"], "disconnected \n")
                clients.pop(index)




thread_connect = threading.Thread(target=connect)
thread_send = threading.Thread(target=send_data)
thread_recv = threading.Thread(target=recv_data)

thread_connect.start()
thread_send.start()
thread_recv.start()

thread_connect.join()
thread_send.join()
thread_recv.join()

    
    


