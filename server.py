# -*- coding: utf-8 -*-

import socket
import sys
import threading

TCP_PORT = int(sys.argv[1])

def lstnTh(sckt, header):
	print("Started receiving messages!")
	while 1:
		Msg = b''
		while 1:
			Byte = sckt.recv(1)
			if(Byte ==b'\n'):
				print(Msg.decode("utf-8"))
				break
			if(len(Byte)==0):
				print("connection lost")
				exit()
			else:
				Msg += Byte
				#print(str(Byte))
			

S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
S.bind(('', TCP_PORT))
S.listen(5)

print("started accepting...")
Client = S.accept()
print("Got a client! " + str(Client[1]))

threading.Thread(group=None, target=lstnTh, args=(Client[0], str(Client[1]))).start()

while 1:
	ToSend=input("msg: ")
	srzlt = Client[0].send((ToSend+'\n').encode("utf-8"))
	#print(str(srzlt))
