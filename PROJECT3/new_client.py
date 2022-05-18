#client.py
import socket
import threading
import json
import partials
connected_identifiers = {}

identifier = input("Choose your unique identifier : ").strip()
while not identifier.isdigit():
    identifier = input("Your unique identifier must be a digit : ").strip()
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost" # "127.0.1.1"
port = 8001
my_socket.connect((host, port))
def thread_sending():
    while True:
        message_to_send = input('Enter Your Message :\n')
        if message_to_send:
            message_with_identifier = identifier + " : " + message_to_send
            my_socket.send(message_with_identifier.encode())
        
def thread_receiving():
    while True:
        message = my_socket.recv(1024).decode()


        
        message =message[-6:]
        print(message,': identifier',identifier)

        # with open ('clients_ids.json','a') as clients_ids:
            # clients_ids.write(json.dumps({'id':message,'identifier':identifier},indent=4,))
        
        partials.save_clients(identifier,message)


        
thread_send = threading.Thread(target=thread_sending)
thread_receive = threading.Thread(target=thread_receiving)
thread_send.start()
thread_receive.start()




def unique_identifier(identifier):
    
    identifier = identifier.replace(' ','')
    identifier =identifier[ -1 : identifier.index(":")]
    return identifier


        
        # clients_ids.write(json.dumps(clients))
