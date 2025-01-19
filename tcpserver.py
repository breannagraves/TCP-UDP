from socket import *
serverPort=12000
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print("The server is ready to receive")
while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(16).decode()
    print('From Client:',sentence, '\n')
    
    #this gets the length of the message sent from client in bytes
    byteLength = len(sentence.encode('utf-8'))
    #serverSocket.send(byteLength)
    
    #outputs to server console currently, but needs to be sent to client instead
    #print("Message of ", byteLength, " bytes received")
    
    s = "Message of " + str(byteLength) + " bytes received"
    connectionSocket.send(bytes(s, 'utf-8'))
    
    #trying to receive buffer overflow message from client
    bufferMessage = connectionSocket.recv(16).decode()
    print('From Client:',bufferMessage, '\n')

    bufferMessage2 = connectionSocket.recv(16).decode()
    print('From Client:',bufferMessage2, '\n')
    
    bufferMessage3 = connectionSocket.recv(16).decode()
    print('From Client:',bufferMessage3, '\n')

    s1 = "Message of " + str(len(bufferMessage) + len(bufferMessage2) + len(bufferMessage3)) + " bytes received"
    connectionSocket.send(bytes(s1, 'utf-8'))
    
    connectionSocket.close()
serverSocket.close()