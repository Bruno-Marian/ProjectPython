import json
import os
from Class.conect import Conect


def load_config_database():
    conection = {}
    if os.path.exists('conection.json'):
        with open('conection.json') as f:
            conection = json.load(f)
    return conection


def set_conect():
    Conect.db_name = load_config_database()['db_name']
    Conect.host = load_config_database()['host']
    Conect.port = load_config_database()['port']
    Conect.user = load_config_database()['user']
    Conect.password = load_config_database()['password']


def json_create():
    conect = {'db_name': Conect.db_name,
              'host': Conect.host,
              'port': Conect.port,
              'user': Conect.user,
              'password': Conect.password}
    with open('conection.json', 'w', encoding='utf8') as js:
        json.dump(conect, js)
        js.close()
