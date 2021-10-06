# coding: utf-8

import socket

hote = "localhost"
port = 15555

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))
print ("Connection on {}".format(port))

with open("data/1.mp4", "rb") as video:
    buffer = video.read()
    print(buffer)
    socket.sendall(buffer)

print("Done sending..")
socket.close()