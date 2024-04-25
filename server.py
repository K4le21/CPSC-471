import socket
import os
import sys
from commands import 

def start_server(port):
    # Server IP
    server_ip = "127.0.0.1"
    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    # Associate the socket with the port
    server_socket.bind((server_ip, port))
    #Start listening for incoming connections (we can have 1 connection in queue before reject new connections)
    server_socket.listen(1)
    
    while True:
        print("Waiting for clients to connect...")
	
        # Accept a waiting connection
        client_socket, client_info = server_socket.accept()
        
        print("Client connected from: " + str(client_info))
        
        # Receive the data the client has to send.
        # This will receive at most 1024 bytes
        client_command = client_socket.recv(1024)

        print("Client sent " + str(client_command.decode()))





if __name__ == "__main__":
    # Check if a port number is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python3 server.py <port>")
        sys.exit(1)

    try:
        # Convert the provided argument to an integer (the port number)
        port = int(sys.argv[1])
    except ValueError:
        print("Invalid port number. Please provide a valid integer.")
        sys.exit(1)

    start_server(port)