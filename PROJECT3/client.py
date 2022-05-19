import socket
import threading
import partials
import time

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


identifier = input("Choose your unique identifier : ").strip()
while not identifier.isdigit():
    #AVOID SPACES IN USER INPUT
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
    
    print('------------------------------------------------------')
    print(f'\n WELCOME CLIENT {partials.get_client_unique_id(identifier)} \n')
    print('------------------------------------------------------ \n')

# DONT SAVE TO FILE IF IDENTIFIER EXISTS
generated_address = partials.get_client_unique_id(identifier)
message_re=str(message_re[-6:])
identified_client = partials.check_client_availability(identifier)
if not identified_client:
    partials.save_clients(identifier,message_re)

# print("identified_client",identified_client,"client_id",client_id)
# CONTINUE SENDING REQUESTS
def thread_sending():
    if identified_client:
        verify_client_id = input('Enter your client ID:\n').strip()

    while True:

        message_to_send = input('Enter Your Message :\n')
        # print("identified_client",identified_client)
        # identified_client = True
        identified = "TRUE" if identified_client else "" 
        # print("identified_client",identified)
        if message_to_send:
            message_with_identifier = identifier + " : " + message_to_send+ ""+identified
            my_socket.send(message_with_identifier.encode())
            

# CONTINUE RECEIVING NEW REQUESTS
def thread_receiving():
   

    while True:
       
        
        message = my_socket.recv(1024).decode()
        print(message)
        

        
thread_send = threading.Thread(target=thread_sending)
thread_receive = threading.Thread(target=thread_receiving)
thread_send.start()
thread_receive.start()

