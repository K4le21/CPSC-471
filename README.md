# FTP File Transfer System

## Team Members
- Vivian Cao - vivicao@csu.fullerton.edu
- Kyle Chan - kchan21@csu.fullerton.edu
- Ryan Dencker - dencker@csu.fullerton.edu
- Alexander Zavaleta - A_zavaleta@csu.fullerton.edu

## Programming Language
Python

---

## Description
The FTP File Transfer System is a client-server application built in Python. It allows users to transfer files between a client machine and a server using FTP commands. The system consists of two main components:

1. **Server (`server.py`):**
   - Accepts incoming connections from FTP clients.
   - Listens for FTP commands such as `get`, `put`, `ls`, and `quit`.
   - Handles file transfer operations between clients and the server.

2. **Client (`client.py`):**
   - Connects to the FTP server using the server's IP address and port number.
   - Provides a command-line interface for users to execute FTP commands.
   - Supports commands such as `get`, `put`, `ls`, and `quit` for file transfer and interaction with the server.

---

## Instructions

### Running the Server
The server is invoked using the following command:
```bash
python client.py <server IP> <server port> 
```



- `<port number>` specifies the port at which the FTP server accepts connection requests.
- Example: `python server.py 1234`

- `<server IP>` is the IP address of the FTP server.
- `<server port>` is the port number on which the server is running.
- Example: `python client.py 127.0.0.1 1234`

### Available Commands
- `get <file name>`: Downloads the specified file from the server.
- `put <file name>`: Uploads the specified file to the server.
- `ls`: Lists files on the server.
- `quit`: Disconnects from the server and exits the client application.

---




