from socket import *
from library.serialização.serializador import deserializer, serializer
from library.user.user import userDefineSevice, userShowMessage


serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

# book = Book(title='o milagre da manhã', author='Juliana', pages=200)
message = userDefineSevice()

message_json = serializer(message=message)

clientSocket.sendto(message_json.encode(), (serverName, serverPort))
answerMessage, serverAddress = clientSocket.recvfrom(2048)
response = deserializer(message=answerMessage)

userShowMessage(message=response)
# print(f"\n{response}")

clientSocket.close()