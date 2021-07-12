from json import dumps, load
from os import mkdir

def set_initial_structure():
    try:
        mkdir(".cache")
    except:
        print("Directory .cache already installed")
    json_file = open(".cache/cache.json", "w+")
    json_structure = {
        "profile": "",
        "region": "",
        "service": "",
        "attributes": []
    }
    json_file.write(dumps(json_structure, sort_keys=True, indent=4))
    json_file.close()


def set_item(key, value):
    json_file = open(".cache/cache.json")
    data = load(json_file)
    data[key] = value
    json_file.close()
    json_file = open(".cache/cache.json", "w")
    json_file.write(dumps(data, sort_keys=True, indent=4, default=str))
    json_file.close()


def get_item(key):
    json_file = open(".cache/cache.json")
    data = load(json_file)
    json_file.close()
    if key in data:
        return data[key]
    else:
        return False
