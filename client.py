import socket
import os
import sys
from client_commands import client_handler


def start_client(server_name, server_port):
    # The client's socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Attempt to connect to the server
    client_socket.connect((server_name, server_port))

    welcome_message = client_socket.recv(1024).decode()
    print (welcome_message)

    while True:
        
        # Get user input
        user_input = input("ftp> ")

        # Send user_input to the server
        client_socket.send(user_input.encode())

        server_response = client_socket.recv(1024).decode()
        print (server_response)
        
        client_handler (server_response, client_socket)



if __name__ == "__main__":
    # Check if both server_name and server_port are provided as command-line arguments
    if len(sys.argv) != 3:
        print ("Usage: python client.py <serverMachine> <serverPort>")
        print ("Use 127.0.0.1 as <serverMachine> when testing")
        sys.exit(1)

    # Get server_name and server_port from command-line arguments
    server_name = sys.argv[1]

    try:
        # Convert the provided port argument to an integer
        server_port = int(sys.argv[2])
    except ValueError:
        print("Invalid port number. Please provide a valid integer.")
        sys.exit(1)

    start_client(server_name, server_port)
