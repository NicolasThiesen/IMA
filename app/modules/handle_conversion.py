from pandas import DataFrame
from os import path as p

def get_items_from_dic(dic, attributes):
    _list = []
    for l in dic["Reservations"]:
        _dic = {}
        for attribute in attributes:
            _dic[attribute] = l["Instances"][0][attribute]
        _list.append(_dic)
    return _list


def conversion(format_file, dictionary, path, filename):
    _df = DataFrame.from_dict(dictionary, orient="columns")
    if format_file == "csv":
        _df.to_csv(p.join(path, filename+".csv"))
    elif format_file == "excel":
        _df.to_excel(p.join(path, filename+".xlsx"))