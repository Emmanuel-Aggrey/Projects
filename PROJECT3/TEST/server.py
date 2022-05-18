#server.py
import socket
import threading
import random
import time
import socketserver
import select

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
broadcast_list = [] 
connected_identifiers = {}
servers = [] 
portlist = [8002,8003]
for port in portlist:
    ds = ("0.0.0.0", port)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(ds)
    server.listen(1)
    print('socket now listening')
    

    servers.append(server)

def accept_loop():
    server.listen(1)
    while True:
    # Wait for any of the listening servers to get a connection
    # connection attempt
        readable,_,_ = select.select(servers, [], [])
        ready_server = readable[0]
    

        connection, address = ready_server.accept()
        # identifier = connection.recv(1024).decode()
        
        # identifier= 'identifier'
        print('CONNECTED SERVER ',ready_server)
        # connection.send(identifier.encode())

    # Might want to spawn thread here to handle connection,
    # if it is long-lived


        broadcast_list.append(connection)

        client_id = f'Your Unique ID: {generated_address()}'

        connection.send(client_id.encode())

        # identifier = connection.recv(1024).decode()

        start_listenning_thread(connection)

#         #RECEIVE DATA FROM CLIENT
        
        
def start_listenning_thread(connection):
    client_thread = threading.Thread(
            target=listen_thread,
            args=(connection,) #the list of argument for the function
        )
    client_thread.start()
    
def listen_thread(connection):
    while True:
        message = connection.recv(1024).decode()
        if message:
            print(f"Received message : {message}")
            broadcast(message)
            # print(connected_identifiers)
        else:
            print(f"connection has been disconnected : {connection}")
            broadcast_list.remove(connection)
#             return
        
def broadcast(message):
    for connection in broadcast_list:
        try:
            connection.send(message.encode())
            print('Active clients listening: ',len(broadcast_list))
            # print('connected_identifiers',connected_identifiers)
        except:
            broadcast_list.remove(connection)
            print(f"Client removed : {connection}")

def generated_address():
    return random.randint(10**5, 10**6 - 1)



accept_loop()



