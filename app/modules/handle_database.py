import sqlite3

conn = sqlite3.connect("./database/database.db")


def command_return_one(command, attributes):
    _command = conn.execute(command, attributes)
    _execute = _command.fetchall()
    return _execute[0][0]


def command_return_list(command, attributes={}):
    _list = []
    if len(attributes)>0:
        _command = conn.execute(command, attributes)
    else:
        _command = conn.execute(command)
    for i in _command:
        _list.append(i[0])
    return _list


def get_regions():
    return command_return_list("SELECT region FROM regions;")


def get_services():
    return command_return_list("SELECT service FROM services;")


def get_command(service):
    return command_return_one("SELECT command FROM services WHERE service=:service;", {"service": service})


def get_service_id(service):
    return command_return_one("SELECT id FROM services WHERE service=:service;", {"service": service})


def get_attributes(service_id):
    return command_return_list("SELECT attribute FROM attributes WHERE service_id=:id", {"id": service_id})
