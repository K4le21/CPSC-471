import os

def client_handler(response, connection_socket):
    # Get the "arguments from the server and split them up"
    command_arguments = response.split()
    
    command = command_arguments[0]

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

     
def get_file (file_name, connection):
    # Downloads file <file name> from the server
    fileData = ""

    fileSize = 0

    fileSizeBuff = ""

    fileSizeBuff = connection.recv(10)

    if not fileSizeBuff:
            return "Error receiving file size header"
    else:
        print("Client received 'get_file' and is now sending file.")

    #get the file size
    fileSize = int((fileSizeBuff.decode()))

    fileData = b""

    bytes_received = 0

    while bytes_received < fileSize:
        dataChunk = connection.recv(min(1024, fileSize - bytes_received))
        if not dataChunk:
            break
        fileData += dataChunk
        bytes_received += len(dataChunk)
        print(f"Received {bytes_received} bytes")

    with open(file_name, "wb") as file:
        file.write(fileData)

    success_msg = connection.recv(1024).decode()
    print (success_msg)

def send_file (fileName, connection):
    # Uploads file <file name> to the server
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
            numSent += connection.send(fileData.encode())
    
        # The file has been read. We are done


    success_msg = connection.recv(1024).decode()
    print (success_msg)
