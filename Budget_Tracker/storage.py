import json

def loaddata():
    try:
        with open('haushalt.json', 'r') as f:
            json_object = json.load(f)
            return json_object
    except (ValueError, FileNotFoundError):
        return []

def savedata(data):
    with open('haushalt.json', 'w') as f:
        json.dump(data, f, indent=2)

