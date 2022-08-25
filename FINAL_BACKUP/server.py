import socket
import threading
import random
import socketserver
import select
import partials


my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
broadcast_list = [] 
connected_identifiers = {}
servers = [] 
portlist = [8000,8001]
for port in portlist:
    ds = ("0.0.0.0", port)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # print('connection binded')
    server.bind(ds)
    server.listen(1)
    
    

    servers.append(server)
    print('socket now listening')

def accept_loop():
    server.listen(1)
    while True:
    # Wait for any of the listening servers to get a clients
    # clients attempt
        readable,_,_ = select.select(servers, [], [])
        ready_server = readable[0]
    

        clients, address = ready_server.accept()
        # identifier = clients.recv(1024).decode()
        
        client_address = generated_address()
        CONNECTED_CLIENT = f'YOUR UNIQUE IDENTIFIER : {client_address}'
        print('CONNECTED CLIENT: ',address)

        clients.send(CONNECTED_CLIENT.encode())


        broadcast_list.append(clients)
        print('Active clients listening: ',len(broadcast_list))

    


        start_listenning_thread(clients)

#         #RECEIVE DATA FROM CLIENT
def start_listenning_thread(clients):
    client_thread = threading.Thread(
            target=listen_thread,
            args=(clients,) #the list of argument for the function
        )
    client_thread.start()
    



def listen_thread(clients):
    while True:
        message = clients.recv(1024).decode()
        if message:
            print(f"Received message : {message}")
            broadcast(message)
        else:
        
            print(f"client has been disconnected : {clients}")
            # broadcast_list.remove(clients)
            return
        
def broadcast(message):
    for clients in broadcast_list:
        try:
            clients.send(message.encode())
            # print('Active clients listening: ',len(broadcast_list))
            # print('connected_identifiers',connected_identifiers)
        except:
            
            broadcast_list.remove(clients)
            # print(f"Client removed : {clients}")

def generated_address():
    return random.randint(10**5, 10**6 - 1)



accept_loop()



