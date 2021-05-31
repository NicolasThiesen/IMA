from pandas import DataFrame

def get_items_from_dic(dic, attributes):
    _list = []
    for l in dic["Reservations"]:
        _dic = {}
        for attribute in attributes:
            _dic[attribute] = l["Instances"][0][attribute]
        _list.append(_dic)
    return _list


def conversion(format, dic, path):
    _df = DataFrame.from_dict(dic, orient="index")
    if format == "csv":
        return _df.to_csv(path+"result")
    elif format == "excel":
        return _df.to_excel(path+"result")