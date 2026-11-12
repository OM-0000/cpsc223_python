# Name: Ossama Mostafa
# Student ID: 871567681
# Section: 18254
# Assignment: Module 10 Assignment 2 Client

#-------------------------------------------
#               << CLIENT >>
#-------------------------------------------

#import the socket library
import socket

print("Welcome to the chatBOT 5000 client.")

# create a socket object
s = socket.socket()

# Define the port on which you want to connect
addr = input("What is the connecting IP address: ")
port = int(input("What is the connecting port: "))

# connect to the server on the local computer
s.connect((addr, port))

listen = False

while True:
    if not listen:
        # encode user input and send to the server, quitting if the user enters 'q'
        msg = input("Enter message (type 'q' to quit): ").encode()
        s.send(msg)        
        if msg == b'q':
            print("chatBOT 5000 client out.")
            # close the connection
            s.close()
            break
        else:
            listen = True
    elif listen:
        # receive data from the server and decode to get the string
        msg = s.recv(1024).decode()
        print(f"Server sent back: {msg}")
        listen = False



