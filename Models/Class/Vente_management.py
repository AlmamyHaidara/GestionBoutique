import sys

sys.path.append('../../Controler')
from Controler.Data.Models.Vente_Model import Vente
from Controler.Data.Models.Quantiter_Model import Quantiter


class Vente_manager():
    @classmethod
    def create_Vente(this):
        Vente.create(produit='Nike', quantiter=12, user=6, debut_date=datetime.today()).save()
        print('Succesfully')
        pass

    @classmethod
    def update_Vente(this):
        try:
            Vente.get(produit=12)
            this.quantier = Quantiter.get(quantiter=10)
        except Vente.DoesNotExist:
            print("Le Vente specifique ne se trouve pas dans la base de donner")
            return False
        except Quantiter.DoesNotExist:
            print("La quantiter nexiste pas dans la base de donner!")
            Quantiter.create(quantiter=10).save()
            this.quantier = Quantiter.get(quantiter=10)
        else:
            Vente.update(produit='Nike', quantiter=1, user=6, debut_date=datetime.today()).execute()
            print("Successfully update Option")

    def delete_Vente(self):
        try:
            Vente.get(produit='12')
            pass
        except Vente.DoesNotExist:
            print("Vente does not exist")
            return False
            pass
        else:
            Vente.delete().where(Vente.id == 1).execute()
            print("Successfully delete")
        pass

    def search_Vente(self):
        Vente_search = Vente.select().where(
            (Vente.id == 1) | (Vente.debut_date == '2023-04-18'))
        for response in Vente_search:
            return response
        pass

    pass
