import json


def set_initial_structure():
    json_file = open(".cache/cache.json", "w+")
    json_structure = {
        "profile": "",
        "region": "",
        "service": ""
    }
    json_file.write(json.dumps(json_structure, sort_keys=True, indent=4))
    json_file.close()

def set_item(key,value):
    json_file = open(".cache/cache.json")
    data = json.load(json_file)
    data[key] = value
    json_file.close()
    json_file = open(".cache/cache.json", "w")
    json_file.write(json.dumps(data, sort_keys=True, indent=4))
    json_file.close()
