import sys

sys.path.append('../../Controler')
from Controler.Data.Models.Command_Model import Command
from Controler.Data.Models.Quantiter_Model import Quantiter
from Controler.Data.Models.Produit_Model import Produit
from Controler.Data.Models.Client_Model import Client
from datetime import datetime


class Command_manager():
    def __init__(self):

        self.qt = ''

    def create_command(self, data):
        print(data)
        for i in range(len(data[1])):
            print(i)
            if data[1][i] == '' or data[1][i] == ' ':
                return False
        print(data)

        try:
            produit = Produit.get(nom_produit=data[0][0])
            print("==> ? ",produit.nom_produit)
            self.qt = Quantiter.get(id=produit.quantiter)
            print(self.qt.quantiter)
            qte = int(str(self.qt.quantiter)) - int(data[0][3])
            if (qte < 0):
                print("==> QTE ", qte)
                print('Quantiter inssufisans')
                return False
            else:
                print("1==> QTE ",int(qte))
                # self.qt=Quantiter.get(quantiter=qte)
                self.qt = Quantiter.get(quantiter=int(qte))
                print( self.qt)
                Produit.update(quantiter_id=self.qt).where(Produit.nom_produit == data[0][0]).execute()
                # prod_id = Produit.get(nom_produit=data[0][0])
                # client_id = Client.get(telephone=data[1][2])
                # Command.create(nom_command=data[0][0], produit=prod_id, quantiter=self.qt, montant_command=data[0][4],
                #                client=client_id).save()
                print('Update insucces full')

        except Quantiter.DoesNotExist:
            print('Quantiter does not exist')
            print('Update insucces full',int( data[0][3]))
            # t =  data[0][3]
            Quantiter.create(quantiter=data[0][3])
            print('Update')
            self.qt = Quantiter.get(quantiter=data[0][3])

        except Client.DoesNotExist:
            Client.create(nom=data[1][0], prenom=data[1][1], telephone=data[1][2], quartier=data[1][3]).save()
            client_id = Client.get(telephone=data[1][2])
            Command.create(nom_command=data[0][0], produit=prod_id, quantiter=self.qt, montant_command=data[0][4],
                           client=client_id).save()

        except Produit.DoesNotExist:
            tab = []
            print('Cette produit nexiste pas dans la base de donner')
            return False

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
            Command.update(nom_command='Nike', produit=12, quantier=quantier, montant_command=100000.0, user=6,
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

    def All_command_list(self):
        tab = []
        command_list = Command.select().execute()
        print(command_list)
        for command in command_list:
            print('=====================================================')
            print("Listing command: ", command.nom_command)
            produit = Produit.get(id=command.produit_id).nom_produit
            client = Client.get(id=command.client_id)
            tab.append(command.id)
            tab.append(command.nom_command)
            tab.append(produit)
            tab.append(client.nom)
            tab.append(client.prenom)
            tab.append(client.telephone)
            tab.append(command.debut_date.strftime("%d/%m/%Y"))
            tab.append(command.eta_livraison)
        print(tab)
        chunk_size = 8
        chunks = []

        for i in range(0, len(tab), chunk_size):
            chunks.append(tab[i:i + chunk_size])
        # Afficher les sous-tableaux
        print(chunks)
        return chunks

        pass
