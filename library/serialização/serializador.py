import json as js

def serializer(message):
    try:
        return js.dumps(message)
    except Exception as erro:
        print(f"erro: {erro}")

def deserializer(message):
    try:
        return js.loads(message)
    except Exception as erro:
        print(f"erro: {erro}")