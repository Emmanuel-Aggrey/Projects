#client.py
import socket
import threading
import json
import partials
connected_identifiers = {}


my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# host = "localhost" # "127.0.1.1"
# port = int(input('Enter PORT Number : '))
# my_socket.connect((host, port))
# while True:
    
#     message_to_send = input("Enter your message : ")

    
#     my_socket.send(message_to_send.encode())




identifier = input("Choose your unique identifier : ").strip()
while not identifier.isdigit():
    #avoid spaces in user input
    identifier = input("Your unique identifier must be a digit : ").strip() 
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost" # "127.0.1.1"
port = int(input('Enter Port : '))
my_socket.connect((host, port))


message_re = my_socket.recv(1024).decode()
# ASSIGN NEW IDENTIFIER TO NEW CLIENT
if not partials.check_client_availability(identifier):
    
    print(message_re)
else:
    # WELCOME ALREADY CONNECTED CLIENT WITH IDENTIFIER
    print('Welcome ',partials.get_client_unique_id(identifier))

# DONT SAVE TO FILE IF IDENTIFIER EXISTS
message_re=str(message_re[-6:])
if not partials.check_client_availability(identifier):
    partials.save_clients(identifier,message_re)



# CONTINUE SENDING REQUESTS
def thread_sending():
    while True:
        message_to_send = input('Enter Your Message :\n')
        if message_to_send:
            message_with_identifier = identifier + " : " + message_to_send
            my_socket.send(message_with_identifier.encode())
            

# CONTINUE RECEIVING NEW REQUESTS
def thread_receiving():
   

    while True:
       
        
        message = my_socket.recv(1024).decode()
        print("message_new",message)
        

        
thread_send = threading.Thread(target=thread_sending)
thread_receive = threading.Thread(target=thread_receiving)
thread_send.start()
thread_receive.start()

