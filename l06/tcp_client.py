#!/usr/bin/python
 
import socket

host="127.0.0.1"
port = 9998

try:
	mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # dia chi IPv4, giao thuc TCP cho socket
	mysocket.connect((host, port))
	print('Connected to host '+str(host)+' in port: '+str(port))
	message = mysocket.recv(1024)	# nhận dữ liệu qua giao thức TCP
	print("Message received from the server", message)
	while True:
		message = input("Enter your message > ")
		mysocket.send(bytes(message.encode('utf-8')))	# gửi dữ liệu qua TCP
		if message== "quit":
			break
except socket.errno as error:
	print("Socket error ", error)
finally:
	mysocket.close()