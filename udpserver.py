"""
server.py: Is a simple server that receives a request on a predefined socket
Usage: python3 server.py
Class: CS4310
Author: Glen Mullen
Email: gmullen@txstate.edu
"""
from socket import *
serverPort=12000
serverSocket=socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print("The Server is ready to receive")
serverResponse="Message received by server"
while True:
	message, clientAddress = serverSocket.recvfrom(32)
	print('Message to  Server: ' + message.decode() +" From: " + str(clientAddress))
	serverSocket.sendto(serverResponse.encode(), clientAddress)
	
	#this gets the length of the message sent from client in bytes
	byteLength = len(message)
	
	#for testing
	#print(byteLength)
	
	s = "Message of " + str(byteLength) + " bytes received"
	serverSocket.sendto(s.encode('utf-8'), clientAddress)

	#trying to receive buffer overflow message from client
	#bufferMessage = message.decode()
	#bufferMessage2 = message.decode()
	#bufferMessage3 = message.decode()
	#print('From Client:',bufferMessage, '\n')

	bufferMessage = message
	bufferMessage2 = message
	bufferMessage3 = message
	bufferMessage4 = message
	bufferMessage5 = message
	bufferMessage6 = message

	s1 = "Message of " + str(len(bufferMessage) + len(bufferMessage2) + len(bufferMessage3) + len(bufferMessage4) + len(bufferMessage5)+ len(bufferMessage6)) + " bytes received"
	serverSocket.sendto(s1.encode('utf-8'), clientAddress)