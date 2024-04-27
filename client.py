import socket
import os
import sys

def start_client(server_name, server_port):
    # The client's socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Attempt to connect to the server
    client_socket.connect((server_name, server_port))

    welcome_message = client_socket.recv(1024).decode()
    print (welcome_message)

    while True:
        user_input = input("ftp> ")
        client_socket.send(user_input.encode())

        server_response = client_socket.recv(1024).decode()

        if server_response == "send file":
            file_name = user_input.split(" ")[1]
            send_file (file_name, client_socket)
        
        server_response = client_socket.recv(1024).decode()
        



def send_file (fileName, connSock):
    fileObj = open(fileName, "r")

    # Read 65536 bytes of data
    fileData = fileObj.read(65536)
        
        # Make sure we did not hit EOF
    if fileData:
        
            
        # Get the size of the data read
        # and convert it to string
        dataSizeStr = str(len(fileData))
        
        # Prepend 0's to the size string
        # until the size is 10 bytes
        while len(dataSizeStr) < 10:
            dataSizeStr = "0" + dataSizeStr
        print (dataSizeStr)
    
        # Prepend the size of the data to the
        # file data.
        fileData = dataSizeStr + fileData
        print (fileData.encode())
        
        # The number of bytes sent
        numSent = 0
        
        # Send the data!
        while len(fileData) > numSent:
            numSent += connSock.send(fileData.encode())
    
        # The file has been read. We are done


    print ("Sent ", numSent, " bytes.")




if __name__ == "__main__":
    # Check if both server_name and server_port are provided as command-line arguments
    if len(sys.argv) != 3:
        print ("Usage: python3 client.py <serverMachine> <serverPort>")
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
