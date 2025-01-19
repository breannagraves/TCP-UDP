from socket import *
serverPort=12000
serverName="127.0.0.1"
clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
#sendValue="Testing 123"
sendValue= input("How are you doing today?: ")
clientSocket.send(sendValue.encode())


#recieving byteLength message from server
sentence = clientSocket.recv(32).decode()
print('From Server:',sentence, '\n')

#experimenting with sending a hardcoded list and splitting it to send 
#stringList = ['I am doing great', ' how are you doi', 'ng today?']

#experimenting with taking input from user to overflow buffer (assignment asks for this)
sendValue2= input("Enter a Message to Overflow the Buffer: ")
#clientSocket.send(sendValue2.encode())

#trying to split message into three parts 
part1, part2, part3 = sendValue2.split(",")

clientSocket.send(part1.encode())


clientSocket.send(part2.encode())
clientSocket.send(part3.encode())

sentence1 = clientSocket.recv(32).decode()
print('From Server:',sentence1, '\n')

clientSocket.close()