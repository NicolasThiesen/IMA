from pandas import DataFrame
from os import path as p


def get_items_from_dic(dic, attributes, command, key):
    _list = []
    if command == "ec2":
        return get_dic_ec2(dic, attributes, key)
    for l in dic[key]:
        _dic = {}
        for attribute in attributes:
            if attribute not in l:
                print(attribute)
            _dic[attribute] = l[attribute]
        _list.append(_dic)
    return _list


def get_dic_ec2(dic, attributes,key):
    _list = []
    for l in dic[key]:
        _dic = {}
        for attribute in attributes:
            if attribute in l["Instances"][0]:
                _dic[attribute] = l["Instances"][0][attribute]
        _list.append(_dic)
    return _list


def conversion(format_file, dictionary, path, filename):
    _df = DataFrame.from_dict(dictionary, orient="columns")
    if format_file == "csv":
        _df.to_csv(p.join(path, filename+".csv"))
    elif format_file == "excel":
        _df.to_excel(p.join(path, filename+".xlsx"))