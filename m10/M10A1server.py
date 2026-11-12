# Name: Ossama Mostafa
# Student ID: 871567681
# Section: 18254
# Assignment: Module 10 Assignment 1 Server

#-------------------------------------------
#               << SERVER >>
#-------------------------------------------

import socket

print("Welcome to the chatBOT 3000 server.")

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# reserve a port on your computer
port = int(input("What is the listening port: "))

# bind to the port
# by omitting ip argument in the ip field parameter,
# we make the server listen to requests coming from other computers on the network
s.bind(('', port))
print("socket binded to %s" %(port))

# put the socket into listening mode
s.listen(5)
print("socket is listening")


# Establish a connection with a client.
c, addr = s.accept()
# an infinite loop until we interrupt it or an error occurs
while True:
    # receive messages from client
    msg = c.recv(1024).decode()
    if msg != b'q':
        print(f"The client said: {msg}")
    else:
        print("chatBOT 3000 server out.")
        # Close the connection with the client
        c.close()
        # Break once the connection is closed
        break