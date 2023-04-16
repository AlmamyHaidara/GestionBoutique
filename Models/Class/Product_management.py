import sys

sys.path.append('../../Controler/Data/Models')

from Controler.Data.Models.Produit_Model import Produit
from Controler.Data.Models.Quantiter_Model import Quantiter


class Product_manager():
    @classmethod
    def __init__(this):
        quantiter = 0

    @classmethod
    def create_product(this, product: dict):
        if not product:
            return False
        else:
            try:
                prod = Produit.get(nom_produit=product['nom_produit'])
                this.quantier = Quantiter.get(quantiter=product['quantier'])
            except Quantiter.DoesNotExist:
                print("La quantiter nexiste pas dans la base de donner!")
                Quantiter.create(quantiter=product['quantier']).save()
                this.quantier = Quantiter.get(quantiter=product['quantier'])
            except Produit.DoesNotExist:
                Quantiter.create(quantiter=product['quantier']).save()
                this.quantier = Quantiter.get(quantiter=product['quantier'])
                print("La quantiter n'existe pas dans la base de donner")
                print("==>> ", this.quantier)
                product_list = Produit.create(nom_produit=product['nom_produit'], prix_produit=product['prix'],
                                              categorie=product['categorie'],
                                              quantiter=this.quantier).save()
                print('Succesfully')
                pass
            else:
                print("La quantiter ou le produit Le produit existe deja dans la base de donner!")
                print("L'objet existe et peut être utilisé.")
                return False

    @classmethod
    def update_product(this):
        try:
            Produit.get(nom_produit=product['nom_produit'])
            this.quantier = Quantiter.get(quantiter=product['quantier'])
        except Produit.DoesNotExist:
            print("Le produit specifique ne se trouve pas dans la base de donner")
            return False
        except Quantiter.DoesNotExist:
            print("La quantiter nexiste pas dans la base de donner!")
            Quantiter.create(quantiter=product['quantier']).save()
            this.quantier = Quantiter.get(quantiter=product['quantier'])
        else:
            Produit.update(nom_produit=product['nom_produit'], prix_produit=product['prix'],
                           categorie=product['categorie'],
                           quantiter=this.quantiter).execute()
            print("Successfully update Option")

    def delete_product(self):
        try:
            Produit.get(nom_produit='Nike')
            pass
        except Produit.DoesNotExist:
            print("Produit does not exist")
            return False
            pass
        else:
            Produit.delete().where(Produit.nom_produit == 'Nike').execute()
            print("Successfully delete")
        pass

    def search_user(self):
        product_search = Produit.select().where(
            (Produit.nom_produit == (product['nom_produit'])) | (Produit.categorie == (product['categorie'])))
        for response in product_search:
            return response
        pass

    pass
