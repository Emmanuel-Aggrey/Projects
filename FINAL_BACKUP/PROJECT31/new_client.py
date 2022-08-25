#client.py
import socket
import threading
import json
import partials
connected_identifiers = {}


my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost" # "127.0.1.1"
port = int(input('Enter PORT Number : '))
my_socket.connect((host, port))
while True:
    message_to_send = input("Enter your message : ")
    my_socket.send(message_to_send.encode())




# identifier = input("Choose your unique identifier : ").strip()
# while not identifier.isdigit():
#     #avoid spaces in user input
#     identifier = input("Your unique identifier must be a digit : ").strip() 
# my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# host = "localhost" # "127.0.1.1"
# port = int(input('Enter Port'))
# my_socket.connect((host, port))
# def thread_sending():
#     while True:
#         message_to_send = input('Enter Your Message :\n')
#         if message_to_send:
#             #message_with_identifier = identifier + " : " + message_to_send
#             my_socket.send(message_to_send.encode())
        
# def thread_receiving():
#     while True:
#         message = my_socket.recv(1024).decode()


#         # GET THE LAST SIX CLIENT ID FROM SERVER
#         message =message[-6:]
    
#         # DONT SAVE TO FILE IF CLIENT EXISTS
#         if  not partials.check_client_availability(identifier):
#             # print("identifier",identifier)
#             partials.save_clients(identifier,message)


        
# thread_send = threading.Thread(target=thread_sending)
# thread_receive = threading.Thread(target=thread_receiving)
# thread_send.start()
# thread_receive.start()

