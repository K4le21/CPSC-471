import os

def command_handler(client_command, connection_socket):
    # Get the "arguments from the client and split them up"
    print (client_command)
    temp_list = client_command.split()
    command_arguments = []
    
    for i in temp_list:
        command_arguments.append(i.decode())
    print (command_arguments)

    command = command_arguments[0]
    print (command)

    # See what command the user inputted
    if command == "get":
        return handle_get_command(command_arguments)
    elif command == "put":
        return handle_put_command(command_arguments, connection_socket)
    elif command == "ls":
        return handle_ls_command()
    elif command == "quit":
        return "quit"
    else:
        return "Invalid command. Please enter a valid command."
    
def handle_get_command (arguments):
    # TODO: Downloads file <file name> from the server

    if len(arguments) != 2:
         return "Invalid 'get' command. Please do 'get <filename>'"
    
    file_name = str(arguments[1])
    
    #file_path = os.path.join(os.path.dirname(__file__), "", file_name)
    return "get command"

def handle_put_command (arguments, connection):
    # TODO: Uploads file <file name> to the server

    if len(arguments) != 2:
         return "Invalid 'put' command. Please do 'put <filename>'"
    
    # Extract file name from arguments
    file_name = str(arguments[1])
    
    # Create the file path
    file_path = os.path.join("server_files", file_name)

    if os.path.exists(file_path):
        return f"Error: File '{file_name}' already exists on the server."

    connection.send(("send_file " + file_name).encode())
    
    # Request user file
    fileData = ""

    # The temporary buffer to store the received data.
    recvBuff = ""

    # The size of the incoming file
    fileSize = 0

    # The buffer containing the file size
    fileSizeBuff = ""

    # Receive the first 10 bytes indicating the size of the file.
    fileSizeBuff = recvAll(connection, 10)

    # Get the file size
    fileSize = int(eval(fileSizeBuff))

    print ("The file size is ", fileSize)
    # Get the file data

    fileData = recvAll(connection, fileSize)
    

    with open(file_path, "w") as file:
        file.write(fileData)

    # Print a success message and return it to the client
    print(f"File '{file_name}' successfully uploaded to the server.")
    return f"File '{file_name}' successfully uploaded to the server."

def handle_ls_command():
    # Store the directory in file_list
    file_list = os.listdir("server_files")

    # Join the list of files into a string with newline separators
    file_list_str = "\n".join(file_list)

    return file_list_str

def recvAll(sock, numBytes):

	# The buffer
	recvBuff = ""
	
	# The temporary buffer
	tmpBuff = ""
	
	# Keep receiving till all is received
	while len(recvBuff) < numBytes:
		
		# Attempt to receive bytes
		tmpBuff = sock.recv(numBytes)
		
		# The other side has closed the socket
		if not tmpBuff:
			break
		
		# Add the received bytes to the buffer
		recvBuff += str(tmpBuff)
	
	return recvBuff