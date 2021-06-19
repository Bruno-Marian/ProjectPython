import datetime

import requests as requests
from DataBase.conection import Client as tbClient
from Class.client import Client as clClient


def search_cep(cep) -> dict:
    result = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    if result.status_code == 200:
        data = result.json()
        localidade = (data['localidade'])
        bairro = (data['bairro'])
        uf = (data['uf'])
        logradouro = (data['logradouro'])

        return {'logradouro': logradouro, 'bairro': bairro, 'uf': uf, 'localidade': localidade}


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
        create_log(str(update_client))


def count_client() -> int:
    client = tbClient.select(tbClient).count()
    return client


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


def create_log(log_update):
    try:
        archive = open('./log/update.txt', 'r+')
        text = archive.readlines()
        text.append(f'AVISO DE UPDATE {datetime.datetime.now()}: {log_update}\n')
        archive.writelines(text)
        archive.close()
    except FileNotFoundError:
        archive = open('./log/update.txt', 'w+')
        archive.writelines(f'AVISO DE UPDATE {datetime.datetime.now()}: {log_update}')
        archive.close()
