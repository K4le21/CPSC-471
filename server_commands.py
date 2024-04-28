import os

def command_handler(client_command, connection_socket):
    # Get the "arguments from the client and split them up"
    print ("test")
    command_arguments = client_command.split()
    
    command = command_arguments[0].decode()
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
    file_name = arguments[1]
    
    # Create the file path
    file_path = os.path.join("server_files", file_name)
    
    
    ## Request user file
    #fileData = ""
#
    ## The temporary buffer to store the received
    ## data.
    #recvBuff = ""
#
    ## The size of the incoming file
    #fileSize = 0
#
    ## The buffer containing the file size
    #fileSizeBuff = ""
#
    ## Receive the first 10 bytes indicating the
    ## size of the file
    #fileSizeBuff = recvAll(connection, 10)
#
    ## Get the file size
    #fileSize = int(eval(fileSizeBuff))
#
    #print ("The file size is ", fileSize)
#
    ## Get the file data
    #fileData = recvAll(connection, fileSize)
#
    #print ("The file data is: ")
    #print (eval(fileData))
    #print ("this is the put command")
    return "put command"

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
		tmpBuff =  sock.recv(numBytes)
		
		# The other side has closed the socket
		if not tmpBuff:
			break
		
		# Add the received bytes to the buffer
		recvBuff += str(tmpBuff)
	
	return recvBuff