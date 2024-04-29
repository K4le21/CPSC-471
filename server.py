import socket
import os
import sys
from server_commands import command_handler

def server_handler (client_socket):
    welcome_msg = "You have successfully connected to the FTP server. Please enter your commands."
    client_socket.send(welcome_msg.encode())

    while True:

        # Get user command
        client_command = client_socket.recv(1024)

        # If client disconnects
        if not client_command:
            print ("Client disconnected.")
            return

        # Print what command client sent
        print ("Client sent " + str(client_command.decode()) + ".")

        # Handle the client command
        response = command_handler(client_command, client_socket)

        # If the reponse is in bytes just send it
        if isinstance(response, bytes):
            client_socket.send(response)
        else:
            # Otherwise encode it
            client_socket.send(response.encode())

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
        print ("Waiting for clients to connect...")
	
        # Accept a waiting connection
        client_socket, client_info = server_socket.accept()
        
        print ("Client connected from: " + str(client_info))
        
        server_handler (client_socket)
    
            




if __name__ == "__main__":
    # Check if a port number is provided as a command-line argument
    if len(sys.argv) != 2:
        print ("Usage: python3 server.py <port>")
        sys.exit(1)

    try:
        # Convert the provided argument to an integer (the port number)
        port = int(sys.argv[1])
    except ValueError:
        print ("Invalid port number. Please provide a valid integer.")
        sys.exit(1)

    start_server(port)