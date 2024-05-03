# Names:
Vivian Cao - vivicao@csu.fullerton.edu

Kyle Chan - kchan21@csu.fullerton.edu

Ryan Dencker - dencker@csu.fullerton.edu

Alexander Zavaleta - A_zavaleta@csu.fullerton.edu

# Programing Language: Python

# In structions on running the code:
The server shall be invoked as: server.py <port number>

<port number› specifies the port at which ftp server accepts connection requests.

For example: python server.py 1234

The ftp client is invoked as: client.py <server ip> <server port> 

Upon connecting to the server, the client prints out ftp>, which allows the user to execute the following commands.

ftp> get <file name> (downloads file <file name> from the server)

ftp> put <filename> (uploads file <file name> to the server)

ftp> ls (lists files on the server)

ftp> quit (disconnects from the server and exits)
