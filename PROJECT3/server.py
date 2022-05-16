#server.py
import socket
import threading

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 8001
ADDRESS = "0.0.0.0"

broadcast_list = []
my_socket.bind((ADDRESS, PORT))
print('socket binded')

def main():
    while True:
        my_socket.listen()
        print('socket now listening')
        client, client_address = my_socket.accept()
        print('socket accepted, got connection object')

        client_id = f'Your Unique ID {client_address[1]}'
        sendTextViaSocket(client_id, client)

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
        if message:
            print(f"Received message : {message}")
            broadcast(message)
        else:
            print(f"client has been disconnected : {client}")
            return
        
def broadcast(message):
    for client in broadcast_list:
        try:
            client.send(message.encode())
        except:
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


# end function

if __name__ == '__main__':
    main()
    # accept_loop()

