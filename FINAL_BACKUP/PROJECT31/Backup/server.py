#server.py
import socket
import threading
import random
import time
import socketserver


my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT = 8004
ADDRESS = "0.0.0.0"
broadcast_list = [] 
connected_identifiers = {}
my_socket.bind((ADDRESS, PORT))
print('socket binded')
def accept_loop():
    while True:
        my_socket.listen()
        # print('socket now listening')
        
        client, client_address = my_socket.accept()
        # identifier = client.recv(1024).decode()

        broadcast_list.append(client)

        client_id = f'Your Unique ID: {generated_address()}'

        client.send(client_id.encode())

        # identifier = client.recv(1024).decode()

        start_listenning_thread(client)

        #RECEIVE DATA FROM CLIENT
        
        
def start_listenning_thread(client):
    client_thread = threading.Thread(
            target=listen_thread,
            args=(client,) #the list of argument for the function
        )
    client_thread.start()
    
def listen_thread(client):
    while True:
        message = client.recv(1024).decode()
        # identifier = client.recv(1024).decode()
        if message:
            print(f"Received message : {message}")
            broadcast(message)
            print(connected_identifiers)
        else:
            print(f"client has been disconnected : {client}")
            broadcast_list.remove(client)
            return
        
def broadcast(message):
    for client in broadcast_list:
        try:
            client.send(message.encode())
            print('Active clients listening: ',len(broadcast_list))
            print('connected_identifiers',connected_identifiers)
        except:
            broadcast_list.remove(client)
            print(f"Client removed : {client}")


def unique_identifier(identifier):
    
    identifier = identifier.replace(' ','')
    identifier =identifier[ 0 : identifier.index(":")]
    return identifier


def generated_address():
    return random.randint(10**5, 10**6 - 1)







accept_loop()