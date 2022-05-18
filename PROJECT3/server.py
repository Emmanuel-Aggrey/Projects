#server.py
import socket
import threading
import random

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 8003
ADDRESS = "0.0.0.0"

broadcast_list = []
connected_identifiers = {}
my_socket.bind((ADDRESS, PORT))
print('socket binded')

def accept_loop():
    while True:
        my_socket.listen()
        print('socket now listening')
        client, client_address = my_socket.accept()
        client_id = f'Your Unique ID:  {generated_address()}'
        client.send(client_id.encode())


        
        start_listenning_thread(client)
        broadcast_list.append(client)
        identifier = client.recv(1024).decode()

        connected_identifiers.update({unique_identifier(identifier):generated_address()})
        print(connected_identifiers)
        
       
def start_listenning_thread(client):
    client_thread = threading.Thread(
            target=listen_thread,
            args=(client,) #the list of argument for the function
        )

    client_thread.start()
    # print("client_thread",client_thread)s
    
def listen_thread(client):
    while True:
        message = client.recv(1024).decode()
        if message:
            
            print(f"Received message : {message}")
            broadcast(message)
            print(connected_identifiers)
        else:
            print(f"client has been disconnected : {client}")
            return
        
def broadcast(message):
    for client in  broadcast_list:
        try:
            # client= client.send(message.encode())
            print('Active clients listening: ',len(broadcast_list))

      
        except:
            del broadcast_list[client]
            broadcast_list.remove(client)
            print(f"Client removed : {client}")




def sendTextViaSocket(message, sock):
    # encode the text message
    encodedMessage = bytes(message, 'utf-8')

    # send the data via the socket to the server
    sock.sendall(encodedMessage)

    # receive acknowledgment from the server
    encodedAckText = sock.recv(1024)
    ackText = encodedAckText.decode('utf-8')
    return ackText



# end function

def unique_identifier(identifier):

    identifier = identifier.replace(' ','')
    identifier =identifier[ 0 : identifier.index(":")]
    return identifier

def generated_address():
    return random.randint(10**5, 10**6 - 1)




accept_loop()

