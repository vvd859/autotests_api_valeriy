from jsonschema import validate

def isValidJSON(jsonData, schema):
    
    try:
        validate(jsonData, schema)
        return True
    except:
        return False