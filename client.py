import socket
import os
import sys

def start_client(server_name, server_port):
    # Server IP
    server_ip = "127.0.0.1"
    # The client's socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Attempt to connect to the server
    client_socket.connect((server_ip, server_port))




if __name__ == "__main__":
    # Check if both server_name and server_port are provided as command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python3 client.py <serverName> <serverPort>")
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
