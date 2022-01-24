from http import client
from socket import *
from urllib import request
from library.serialização.serializador import deserializer, serializer
from library.user.user import userDefineService, userShowMessage


serverName = 'localhost'
serverPort = 12000

def send(client:socket):
    try:
        message = userDefineService()
        message_json = serializer(message=message)
        client.sendto(message_json.encode(), (serverName, serverPort))
    except ValueError as erro:
        print("\nErro: o valor inserido é inválido")
    except Exception as erro:
        print(f"\nErro: {erro}")

def receive(client:socket):
    try:
        answerMessage, serverAddress = client.recvfrom(2048)
        response = deserializer(message=answerMessage)
        userShowMessage(message=response)
    except Exception as erro:
        print(f"Erro: {erro}")

def close(client:socket):
    client.close()

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(2)
send(client=clientSocket)
receive(client=clientSocket)