import os

def client_handler(response, connection_socket):

    if response == "quit":
            print("Received 'quit' command. Closing connection.")
            exit(0)
    elif response == "send file":
        file_name = response.split(" ")[1]
        response (file_name, connection_socket)

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