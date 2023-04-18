import sys

sys.path.append('../../Controler')
from Controler.Data.Models.Command_Model import Command
from Controler.Data.Models.Quantiter_Model import Quantiter
from datetime import datetime


class Command_manager(Command):
    '''
    nom_command = CharField()
        montant_command = DoubleField()
        produit = ForeignKeyField(Produit, backref='produit')
        user = ForeignKeyField(User, backref='users')
         debut_date = DateTimeField(auto_now_add=True)
        fin_date = DateTimeField()
    '''

    def create_command(self):
        Command.create(nom_command='Nike', produit=12, montant_command=100000.0, user=6,
                       debut_date=datetime.today(), fin_date=datetime.fromisoformat('2023-05-18')).save()
        print('Created command is successfully')
        pass

    def update_command(self):
        try:
            Command.get(id=3)
            quantier = Quantiter.get(quantiter=10)
        except Command.DoesNotExist:
            print("Le command specifique ne se trouve pas dans la base de donner")
            return False
        except Quantiter.DoesNotExist:
            print("La command nexiste pas dans la base de donner!")
            Quantiter.create(quantiter=2).save()
            quantier = Quantiter.get(quantiter='Nike')
        else:
            Command.update(nom_command='Nike', produit=12, montant_command=100000.0, user=6,
                           debut_date=datetime.today(), fin_date=datetime.fromisoformat('2023-05-14')).execute()

            print("Successfully update Option")

    pass

    def delete_command(self):
        try:
            Command.get(id=3)
            pass
        except Command.DoesNotExist:
            print("Command does not exist")
            return False
            pass
        else:
            Command.delete().where(Command.id == 3).execute()
            print("Successfully delete")
        pass

    def search_command(self):
        command_search = Command.select().where((Command.id == 3) | (Command.debut_date == '2023-05-14'))
        for response in command_search:
            print("Searching command: ", response.nom_command)
            return response
            pass

    pass
