#!/bin/python3

import socket

HOST = '192.168.1.108'
PORT = 9090

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.bind((HOST, PORT))

print("Initiating server.")
socket.listen(1)

print("Waiting for a connection...")

# Accept a single connection
client_socket, client_address = socket.accept()
print(f"Connected to {client_address}")

while True:
    # Receive and display messages from the client
    message = client_socket.recv(1024).decode('utf-8')
    if not message:
        break
    print(f"Friend: {message}")

    # Send a reply back to the client
    reply = input("You: ")
    client_socket.send(reply.encode('utf-8'))

# Close the connection
client_socket.close()