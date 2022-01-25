from socket import *
# from server.despanchante import invoke
from server.despanchante import invoke
from serializador.serializador import deserializer, serializer

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('localhost', serverPort))
print('The server is ready to receive')

while 1:
    messageRecv, clientAddress = serverSocket.recvfrom(2048)
    message = deserializer(messageRecv)
    result = invoke(message=message)
    
    response = serializer(message=result)
    serverSocket.sendto(response.encode(),clientAddress)