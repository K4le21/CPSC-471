import os

def command_handler(client_command, connection_socket):
    # Get the "arguments from the client and split them up"
    temp_list = client_command.split()
    command_arguments = []
    
    for i in temp_list:
        command_arguments.append(i.decode())
    
    command = command_arguments[0]

    # See what command the user inputted
    if command == "get":
        return handle_get_command(command_arguments, connection_socket)
    elif command == "put":
        return handle_put_command(command_arguments, connection_socket)
    elif command == "ls":
        return handle_ls_command()
    elif command == "quit":
        return "quit"
    else:
        return "Invalid command. Please enter a valid command."
    

def handle_get_command(arguments, connection):
    # Downloads file <file name> from the server
    if len(arguments) != 2:
        return "Invalid 'get' command. Please use 'get <filename>'"
    
    # Get file name
    file_name = str(arguments[1])

    # Get file path
    file_path = os.path.join("server_files", file_name)

    # Check if file exists
    if not os.path.exists(file_path):
        connection.send("File not found".encode())
        return f"'{file_name}' not found"
    
    connection.send(("get_file " + file_name).encode())
    
    # Open the file in binary mode
    with open(file_path, "rb") as file_obj:
        # Read and send file data in chunks
        while True:
            # Read chunk of data
            file_data = file_obj.read(65536)
            # Check if EOF
            if not file_data:
                break
            # Get size of data chunk and prepend to data
            data_size = len(file_data)
            data_size_str = str(data_size).zfill(10)
            # Send size and data
            connection.sendall(data_size_str.encode() + file_data)

    print(f"File '{file_name}' successfully sent to client.")
    return f"File '{file_name}' successfully sent to client."

def handle_put_command (arguments, connection):

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

    # The size of the incoming file
    fileSize = 0

    # The buffer containing the file size
    fileSizeBuff = ""

    # Receive the first 10 bytes indicating the size of the file.
    fileSizeBuff = connection.recv(10)

    if not fileSizeBuff:
            return "Error receiving file size header"
    else:
        print("Client received 'send_file' and is now sending file.")

    # Get the file size
    fileSize = int((fileSizeBuff.decode()))

    print ("The file size is ", fileSize)

    # Get the file data
    fileData = b""
    bytes_received = 0
    while bytes_received < fileSize:
        dataChunk = connection.recv(min(1024, fileSize - bytes_received))
        if not dataChunk:
            break
        fileData += dataChunk
        bytes_received += len(dataChunk)
        print(f"Received {bytes_received} bytes")
    print (fileData)

    with open(file_path, "wb") as file:
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
