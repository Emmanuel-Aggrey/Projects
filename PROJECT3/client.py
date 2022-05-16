#client.py
import socket
import threading
unique_name = input("Please enter your unique identifier : ").strip()
while not unique_name:
    unique_name = input("unique identifier not be empty : ").strip()
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost" # "127.0.1.1"
port = 8002
my_socket.connect((host, port))
def thread_sending():
    while True:
        message_to_send = input()
        if message_to_send:
            message_with_unique_name = unique_name + " : " + message_to_send +'\n'
            my_socket.send(message_with_unique_name.encode())
        
def thread_receiving():
    while True:
        message = my_socket.recv(1024).decode()
        print(message)
        
thread_send = threading.Thread(target=thread_sending)
thread_receive = threading.Thread(target=thread_receiving)
thread_send.start()
thread_receive.start()