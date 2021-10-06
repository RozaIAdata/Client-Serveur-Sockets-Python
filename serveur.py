# coding: utf-8

import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 15555))

while True:
        socket.listen(5)
        client, address = socket.accept()
        print ("{} connected".format( address ))
        n=0

        try:
                print("Starting to read bytes..")
                buffer = client.recv(1024)  
        
                with open('video_'+str(n)+'.mp4', "wb") as video: 
                        n += 1
                        i = 0
                        while buffer:
                                video.write(buffer)
                                print("buffer {0}".format(i))
                                i += 1
                                buffer = client.recv(1024)

                print("Done reading bytes..")
                client.close()
        except KeyboardInterrupt:
                if client:
                        client.close()
                break


print ("Close")
client.close()
stock.close()