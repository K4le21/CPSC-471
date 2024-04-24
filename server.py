# CODE FROM CPSC 352

import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

####### A SIMPLE ILLUSTRATION OF THE TCP SERVER #######

# The port number on which to listen for incoming
# connections.
PORT_NUMBER = 1235
KEY = input("Enter 16-byte key: ").encode('utf-8')

# Create a socket
serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# Associate the socket with the port
serverSock.bind(('127.0.0.1', PORT_NUMBER))

# Start listening for incoming connections (we can have
# at most 100 connections waiting to be accepted before
# the server starts rejecting new connections)
serverSock.listen(100)

# Keep accepting connections forever
while True:

	print("Waiting for clients to connect...")
	
	# Accept a waiting connection
	cliSock, cliInfo = serverSock.accept()
	
	print("Client connected from: " + str(cliInfo))
	
	# Receive the data the client has to send.
	# This will receive at most 1024 bytes
	cliMsg = cliSock.recv(1024)
	print("recieved: " + str(cliMsg))
	#decrypt the message 
	cipher = AES.new(KEY, AES.MODE_ECB)
	#decryptedMsg = unpad(cipher.decrypt(cliMsg), AES.block_size).decode('utf-8')
	decryptedMsg = cipher.decrypt(cliMsg)
	print("decrypted: " + str(decryptedMsg))
	#unpad msg
	unpaddedMsg = unpad(decryptedMsg, AES.block_size)
	print("unpadded: " + str(unpaddedMsg))
	#decode msg
	finalMsg = unpaddedMsg.decode('utf-8')
		
	print("Final Decrypted Message: " + str(finalMsg))


	# Hang up the client's connection
	cliSock.close()
