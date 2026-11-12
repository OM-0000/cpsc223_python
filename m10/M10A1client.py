# Name: Ossama Mostafa
# Student ID: 871567681
# Section: 18254
# Assignment: Module 10 Assignment 1 Client


#-------------------------------------------
#               << CLIENT >>
#-------------------------------------------

#import the socket library
import socket

print("Welcome to the chatBOT 3000 client.")

# create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = int(input("What is the connecting port: "))

# connect to the server on the local computer
s.connect(('127.0.0.1', port))

# receive data from the server and decode to get the string
msg = input("Enter message (type 'q' to quit): ").encode()
if msg != 'q':
    s.send(msg)
else:
    # close the connection
    s.close()


