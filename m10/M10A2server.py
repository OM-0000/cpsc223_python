# Name: Ossama Mostafa
# Student ID: 871567681
# Section: 18254
# Assignment: Module 10 Assignment 2 Server

#-------------------------------------------
#               << SERVER >>
#-------------------------------------------

import socket

print("Welcome to the chatBOT 5000 server.")

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# reserve a port on your computer
port = int(input("What is the listening port: "))

# bind to the port
# by omitting ip argument in the ip field parameter,
# we make the server listen to requests coming from other computers on the network
s.bind(('', port))
# put the socket into listening mode
s.listen(5)
# Establish a connection with a client.
c, addr = s.accept()

#
listen = True

# an infinite loop until we interrupt it or an error occurs
while True:
    if listen:
        # receive messages from client
        msg = c.recv(1024).decode()
        if msg != 'q':
            print(f"The client said: {msg}")
            listen = False
        else:
            print("chatBOT 5000 server out.")
            # Close the connection with the client
            c.close()
            # Break once the connection is closed
            break
    elif not listen:
        # encode user input and send to the client
        msg = input("Enter message: ").encode()
        c.send(msg)
        listen = True      
                