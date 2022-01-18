from email import message
from socket import *
import json as js
from unittest import result
from urllib import response
import library.book.bookBD as bookBD
from library.serialização.serializador import deserializer, serializer



serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('localhost', serverPort))
print('The server is ready to receive')
while 1:
    messageRecv, clientAddress = serverSocket.recvfrom(2048)
    message = deserializer(messageRecv)
    if message['service'] == 1:
        result = {
            "result": bookBD.addBook(
                title=message['objeto']['title'],
                author=message['objeto']['author'],
                pages=message['objeto']['pages'],
                checkinBook=message['objeto']['checkinBook']
            ),
            "title": message['objeto']['title']
        }
    elif message['service'] == 2:
        result = {
            "result": bookBD.leaveReading(
                title=message['title']
            ),
            "title": message['title']
        }
    # print(result)

    response = serializer(message=result)
    serverSocket.sendto(response.encode(),clientAddress)