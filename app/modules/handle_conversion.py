def get_items_from_dic(dic, attributes):
    _list = []
    for l in dic["Reservations"]:
        _dic = {}
        for attribute in attributes:
            _dic[attribute] = l["Instances"][0][attribute]
        _list.append(_dic)
    return _list


def conversion(format, dic):
    pass