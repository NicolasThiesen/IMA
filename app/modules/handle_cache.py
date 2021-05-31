from json import dumps, load


def set_initial_structure():
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
    return data[key]