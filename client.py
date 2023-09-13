#!/bin/python3

import socket

HOST = '192.168.1.108'
PORT = 9090

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.connect((HOST, PORT))

print("Connected to the server.")

while True:
    message = input("You: ")
    socket.send(message.encode('utf-8'))
    reply = socket.recv(1024).decode('utf-8')
    print(f"Friend: {reply}")

socket.close()