#Python Network Programming

#Sockets Vocabulary
#Domain : the set of protocols used for transport mechanisms like AF_INET, PF_INET, etc.
#Type : the type of communication between sockets
#Protocol : identifies the type of protocol used within domain and type. Usually zero.
#Port : the server listens for clients calling on one or more ports. It can be a string containing the port number, a name of the service, or a Fixnum port.
# Hostname : Identifies a network interface. It can be:
#   - a string containing the hostname, IPv6 address, or double-quad (i.e. 128 bits?) address
#   - an integer
#   - a zero-length string
#   - a string "<broadcast>"



# Socket Server Methods
# s.bind()              :       binds address to the socket. The address contains the pair of hostname and the port number
# s.listen()            :       starts the TCP listener
# s.accept()            :       passively accepts the TCP client connection and blocks until the connection arrives


# Socket Client Methods
# s.connect()           :       actively starts the TCP server connection

# Socket General Methods
# s.send()              :       sends the TCP message
# s.sendto()            :       sends the UDP message
# s.recv()              :       receives the TCP message
# s.recvfrom()          :       receives the UDP message
# s.close()             :       closes the socket
# socket.ghostname()    :       returns the host name

#import the socket library
import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket successfully created")

# reserve a port on your computer
port = 8000

# bind to the port
# by omitting ip argument in the ip field parameter,
# we make the server listen to requests coming from other computers on the network
s.bind(('', port))
print("socket binded to %s" %(port))

# put the socket into listening mode
s.listen(5)
print("socket is listening")

# an infinite loop until we interrupt it or an error occurs
while True:

    # Establish a connection with a client.
    c, addr = s.accept()
    print("Got connection from", addr)

    # send a thank you message to the client
    c.send(b'Thank you for connecting')

    # Close the connection with the client
    c.close()