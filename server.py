
from socket import *
from unittest import result
from library.despachante.despanchante import forwarding
# import library.book.bookBD as bookBD
from library.serialização.serializador import deserializer, serializer



serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('localhost', serverPort))
print('The server is ready to receive')

while 1:
    messageRecv, clientAddress = serverSocket.recvfrom(2048)
    message = deserializer(messageRecv)
    
    result = forwarding(message=message)

    response = serializer(message=result)
    serverSocket.sendto(response.encode(),clientAddress)