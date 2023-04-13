import sys
sys.path.append('../')
from peewee import *

from Controler.Data.mysql_connexion import connect

conn = connect()


class Quantiter(Model):
    quantiter = IntegerField()

    class Meta:
        database = conn
        table_name = 'Quantiter'

conn.connect()
conn.create_tables([Quantiter])