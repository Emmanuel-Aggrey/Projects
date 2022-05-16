#server.py
import socket
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        my_socket.bind(ADDRESS)
except print(0):
    pass

# ADDRESS = "0.0.0.0"
broadcast_list = []

# my_socket.bind((ADDRESS, PORT))
def accept_loop():
    while True:
        my_socket.listen(1)
        client, client_address = my_socket.accept()
        broadcast_list.append(client)
        start_listenning_thread(client)
        
def start_listenning_thread(client):
    client_thread = threading.Thread(
            target=listen_thread,
            args=(client,) #the list of argument for the function
        )
    client_thread.start()
    
def listen_thread(client):
    while True:
        message = client.recv(1024).decode()
        print(f"Received message : {message}")
        broadcast(message)
        
def broadcast(message):
    for client in broadcast_list:
        client.send(message.encode())
accept_loop()