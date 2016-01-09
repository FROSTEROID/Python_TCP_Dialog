#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
import sys
import threading

TCP_IP = sys.argv[1]
TCP_PORT = int(sys.argv[2])

def lstnTh(sckt, header):
	print("started receiving!")
	while 1:
		Msg = b''
		while 1:
			Byte = sckt.recv(1)
			if(Byte == b'\n'):
				print(header + Msg.decode("utf-8"))
				#print(Msg.decode("utf-8"))
				#print(Msg)
				break
			elif(len(Byte) == 0):
				print("connection lost")
				exit()
			else:
				Msg += Byte
				#print(Byte)


S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if (S.connect((TCP_IP, TCP_PORT)) == None):
	print("connected!")
else:
	print("\nnot this time, bro!")
	exit()

threading.Thread(group=None, target=lstnTh, args=(S, "thatGuy: ")).start()

while 1:
	ToSend = input("msg: ")
	srzlt = S.send(bytes(ToSend+'\n', "utf-8"))
	print(str(srzlt))
