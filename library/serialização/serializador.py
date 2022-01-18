import json as js

def serializer(message):
    return js.dumps(message)

def deserializer(message):
    return js.loads(message)