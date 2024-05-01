# Names:
Vivian Cao         Email: vivicao@csu.fullerton.edu 
Kyle Chan          Email: kchan21@csu.fullerton.edu
Ryan Dencker       Email: dencker@csu.fullerton.edu
Alexander Zavaleta Email: A_zavaleta@csu.fullerton.edu
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Programing Language: Python
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# In structions on running the code:
Specifications
The server shall be invoked as:
pythonserv.py<PORTNUMBER>
< PORT NUMBER ›specifiestheport atwhichftp serveraccepts connection requests.
For example: python serv.py 1234
The ftp client is invoked as:
cli <server machine> <server port>
<server machine> is the domain name of the server (ecs.fullerton.edu). This will be converted into 32 bit IP address using DNS lookup. For example: python cli.py ecs.fullerton.edu 1234
Upon connecting to the server, the client prints out ftp>, which allows the user to execute the following commands.
ftp> get <file name > (downloads file < file name > from the server) ftp> put < filename> (uploads file < file name> to the server)
ftp> Is(lists files on theserver)
ftp> quit (disconnects from the server and exits)
<img width="1139" alt="image" src="https://github.com/K4le21/CPSC-471/assets/70111655/14623cf4-ab84-49e2-a450-688b3e686cdb">
<img width="1435" alt="image" src="https://github.com/K4le21/CPSC-471/assets/70111655/521f7c9e-d2e1-4927-901f-9393e85ece25">
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Things to take note:


