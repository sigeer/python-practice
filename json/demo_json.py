
import json

def serialize(model):
    return json.dumps(model)
    
def deserialize(str):
    return json.loads(str)


print(serialize({"a": 1}))