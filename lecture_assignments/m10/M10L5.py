# Network Programming Python - HTTP Server

import http.server
import socketserver

# Define port number
PORT = 8080

# Create handle
Handler = http.server.SimpleHTTPRequestHandler

# Create TCPServer
http = socketserver.TCPServer(("", PORT), Handler)

# Getting logs
print("serving at port", PORT)
http.serve_forever()