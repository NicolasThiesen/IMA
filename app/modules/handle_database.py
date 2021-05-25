import sqlite3

conn = sqlite3.connect("./database/database.db")


def get_regions():
    regions_list = []
    _regions = conn.execute("SELECT region FROM regions;")
    for _region in _regions:
        regions_list.append(_region[0])
    return regions_list


def get_services():
    services_list = []
    _services = conn.execute("SELECT service FROM services;")
    for service in _services:
        services_list.append(service[0])
    return services_list
