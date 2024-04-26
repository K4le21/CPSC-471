import os

def handler(command, connection_socket):
    # Get the "arguments from the client and split them up"
    command_arguments = command.split()
    print (command)
    print (command_arguments)

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
    print ("this is the get command")
    pass

def handle_put_command (arguments, connection):
    # TODO: Uploads file <file name> to the server
    print ("this is the put command")
    pass

def handle_ls_command():
    # TODO: Lists files on the server
    print ("this is the ls command")
    pass

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