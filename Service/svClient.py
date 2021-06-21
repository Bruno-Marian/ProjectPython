import datetime

import peewee
import requests as requests
from DataBase.conection import Client as tbClient
from Class.client import Client as clClient


def search_cep(cep) -> dict:
    try:
        result = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        if result.status_code == 200:
            data = result.json()
            localidade = (data['localidade'])
            bairro = (data['bairro'])
            uf = (data['uf'])
            logradouro = (data['logradouro'])

            return {'logradouro': logradouro, 'bairro': bairro, 'uf': uf, 'localidade': localidade}
    except requests.exceptions.ConnectionError as ex:
        create_log(name_log='error', log=f' {ex !r}')
    return {}


def new_table():
    tbClient.create_table()
    if not tbClient.select().where(tbClient.id == clClient.id).exists():

        new_client = tbClient.create(id=clClient.id,
                                     nome=clClient.nome,
                                     cpf=clClient.cpf,
                                     telefone=clClient.telefone,
                                     rg=clClient.rg,
                                     logradouro=clClient.logradouro,
                                     bairro=clClient.bairro,
                                     numero=clClient.numero,
                                     localidade=clClient.localidade,
                                     uf=clClient.uf,
                                     cep=clClient.cep)
        new_client.save()


    else:
        update_client = tbClient.update({tbClient.nome: clClient.nome,
                                         tbClient.cpf: clClient.cpf,
                                         tbClient.telefone: clClient.telefone,
                                         tbClient.rg: clClient.rg,
                                         tbClient.logradouro: clClient.logradouro,
                                         tbClient.bairro: clClient.bairro,
                                         tbClient.numero: clClient.numero,
                                         tbClient.uf: clClient.uf,
                                         tbClient.cep: clClient.cep}).where(tbClient.id == clClient.id)
        update_client.execute()
        create_log(name_log='update', log=str(update_client))


def count_client() -> int:
    client = tbClient.select(tbClient).count()
    return client


def last_insert_id():
    last = tbClient.select(tbClient.id).order_by(tbClient.id.desc())
    return last[0].id


def search_climate(cidade, uf):
    result = requests.get(f'https://api.hgbrasil.com/weather?key=4aa90ea7&city_name={cidade},{uf}')
    if result.status_code == 200:
        data = result.json()
        result = data['results']
        date = result['date']
        description = result['description']
        city = result['city']
        humidity = result['humidity']
        sunrise = result['sunrise']
        sunset = result['sunset']
        temp = result['temp']
        return {'date': date,
                'description': description,
                'city': city,
                'humidity': humidity,
                'sunrise': sunrise,
                'sunset': sunset,
                'temp': temp}


def create_log(name_log, log):
    try:
        archive = open(f'./log/{name_log}.txt', 'r+')
        text = archive.readlines()
        text.append(f'LOG: {datetime.datetime.now()}: {log}\n')
        archive.writelines(text)
        archive.close()
    except FileNotFoundError:
        archive = open(f'./log/{name_log}.txt', 'w+')
        archive.writelines(f'LOG: {datetime.datetime.now()}: {log}')
        archive.close()
