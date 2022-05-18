#server.py
import socket
import threading
import random
import time
import socketserver
import select

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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

while True:
    # Wait for any of the listening servers to get a client
    # connection attempt
    readable,_,_ = select.select(servers, [], [])
    ready_server = readable[0]
    

    connection, address = ready_server.accept()
    identifier = connection.recv(1024).decode()
    print(identifier)
    
    connection.send(identifier.encode())

    # Might want to spawn thread here to handle connection,
    # if it is long-lived

# class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    
#     def handle(self):
#         # client, client_address = self.request.accept()
#         self.data = self.request.recv(1024)
#         print("%s wrote: " % self.client_address[0])
#         print(self.data)
#         self.request.send(self.data)
        
    
# class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
#     pass

# if __name__ == "__main__":

#     HOST = ''
#     PORT_A = 8001
#     PORT_B = 8000

#     server_A = ThreadedTCPServer((HOST, PORT_A), ThreadedTCPRequestHandler)
#     server_B = ThreadedTCPServer((HOST, PORT_B), ThreadedTCPRequestHandler)
    
   
#     # identifier = client.recv(1024).decode()                                    


#     server_A_thread = threading.Thread(target=server_A.serve_forever)
#     server_B_thread = threading.Thread(target=server_B.serve_forever)

#     server_A_thread.setDaemon(True)
#     server_B_thread.setDaemon(True)

#     server_A_thread.start()
#     server_B_thread.start()

#     while True:
#         time.sleep(1)



# PORT = 8004
# ADDRESS = "0.0.0.0"
# broadcast_list = [] 
# connected_identifiers = {}
# my_socket.bind((ADDRESS, PORT))
# print('socket binded')
# def accept_loop():
#     while True:
#         my_socket.listen()
#         # print('socket now listening')
        
#         client, client_address = my_socket.accept()
#         # identifier = client.recv(1024).decode()

#         broadcast_list.append(client)

#         client_id = f'Your Unique ID: {generated_address()}'

#         client.send(client_id.encode())

#         # identifier = client.recv(1024).decode()

#         start_listenning_thread(client)

#         #RECEIVE DATA FROM CLIENT
        
        
# def start_listenning_thread(client):
#     client_thread = threading.Thread(
#             target=listen_thread,
#             args=(client,) #the list of argument for the function
#         )
#     client_thread.start()
    
# def listen_thread(client):
#     while True:
#         message = client.recv(1024).decode()
#         # identifier = client.recv(1024).decode()
#         if message:
#             print(f"Received message : {message}")
#             broadcast(message)
#             print(connected_identifiers)
#         else:
#             print(f"client has been disconnected : {client}")
#             broadcast_list.remove(client)
#             return
        
# def broadcast(message):
#     for client in broadcast_list:
#         try:
#             client.send(message.encode())
#             print('Active clients listening: ',len(broadcast_list))
#             print('connected_identifiers',connected_identifiers)
#         except:
#             broadcast_list.remove(client)
#             print(f"Client removed : {client}")


# def unique_identifier(identifier):
    
#     identifier = identifier.replace(' ','')
#     identifier =identifier[ 0 : identifier.index(":")]
#     return identifier


def generated_address():
    return random.randint(10**5, 10**6 - 1)







# accept_loop()