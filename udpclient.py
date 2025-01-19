from socket import *
serverPort=12000
serverName="192.168.1.236"
clientSocket=socket(AF_INET,SOCK_DGRAM)
clientSocket.connect((serverName,serverPort))
#sendValue="Testing 123"
sendValue= input("How are you doing today?: ")
clientSocket.send(sendValue.encode())

#recieving byteLength message from server
sentence = clientSocket.recv(32).decode()
byteLength = clientSocket.recv(32).decode()
print('From Server:', byteLength, '\n')

#experimenting with taking input from user to overflow buffer (assignment asks for this)
sendValue2= input("Enter a Message to Overflow the Buffer: ")

#trying to split message into three parts 
part1, part2, part3, part4, part5, part6 = sendValue2.split(" ")

clientSocket.send(part1.encode())
clientSocket.send(part2.encode())
clientSocket.send(part3.encode())
clientSocket.send(part4.encode())
clientSocket.send(part5.encode())
clientSocket.send(part6.encode())

byteLength2 = clientSocket.recv(1024).decode()
print('From Server:', byteLength2, '\n')

clientSocket.close()