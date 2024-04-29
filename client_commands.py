import os

def client_handler(response, connection_socket):
    command_arguments = response.split()
    
    command = command_arguments[0]
    print (command_arguments)

    if command == "quit":
        print("Received 'quit' command. Closing connection.")
        exit(0)
    elif command == "send_file":
        file_name = command_arguments[1]
        print (file_name)
        send_file (file_name, connection_socket)
    elif command == "get_file":
        file_name = command_arguments[1]
        print (file_name)
        get_file (file_name, connection_socket)
         
def get_file (file_name, connSock):
    # TODO: Fix this. I copy pasted from server_commands.py.
    file_path = os.path.join("server_files", file_name)

    # Request user file
    fileData = ""

    # The size of the incoming file
    fileSize = 0

    # The buffer containing the file size
    fileSizeBuff = ""

    # Receive the first 10 bytes indicating the size of the file.
    fileSizeBuff = connSock.recv(10)
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
        dataChunk = connSock.recv(min(1024, fileSize - bytes_received))
        if not dataChunk:
            break
        fileData += dataChunk
        bytes_received += len(dataChunk)
        print(f"Received {bytes_received} bytes")
    print (fileData)

    with open(file_path, "wb") as file:
        file.write(fileData)

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
        
        # The number of bytes sent
        numSent = 0
        
        # Send the data!
        while len(fileData) > numSent:
            numSent += connSock.send(fileData.encode())
    
        # The file has been read. We are done


    success_msg = connSock.recv(1024).decode()
    print (success_msg)
