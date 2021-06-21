import datetime

from peewee import PostgresqlDatabase, DateTimeField, Model, CharField, AutoField

from Class.conect import Conect

database = PostgresqlDatabase(None)


class Client(Model):
    id = AutoField()
    nome = CharField()
    cpf = CharField(unique=True)
    telefone = CharField()
    rg = CharField(unique=True)
    logradouro = CharField()
    bairro = CharField()
    numero = CharField()
    localidade = CharField()
    uf = CharField()
    cep = CharField()
    created_date = DateTimeField(default=datetime.datetime.today())

    class Meta:
        database = database
        db_table = "client"


def run_conection():
    database.init(Conect.db_name,
                  host=Conect.host,
                  port=Conect.port,
                  user=Conect.user,
                  password=Conect.password)
    database.connect(True)
