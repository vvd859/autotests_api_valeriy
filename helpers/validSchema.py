from jsonschema import validate

def isValidJSON(jsonData, schema):
    
    if validate(jsonData, schema):
        return False
    else:
        return True