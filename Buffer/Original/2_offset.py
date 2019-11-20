#!/usr/bin/python
import sys, socket

offset = ""

while True:
        try:
		s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect(('192.168.0.149',80))

                s.send(('TRun' + offset 'r\n'))
                s.close()
                sleep(1)

        except:
                print "error connecting to server"
                sys.exit()
