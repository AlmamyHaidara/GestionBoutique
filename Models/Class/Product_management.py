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
            if(product['nom_produit'] == '' or product['prix'] == '' or product['quantiter'] == '' or product['nom_produit'] == ' ' or product['prix'] == ' ' or product['quantiter'] == ' ' ):
                print('Veuillez remplire correctement des differente champs')
                return False
            else:
                try:
                    prod = Produit.get(nom_produit=product['nom_produit'])
                    this.quantiter = Quantiter.get(quantiter=product['quantiter'])
                except Quantiter.DoesNotExist:
                    print("La quantiter nexiste pas dans la base de donner!")
                    Quantiter.create(quantiter=product['quantiter']).save()
                    this.quantiter = Quantiter.get(quantiter=product['quantiter'])
                except Produit.DoesNotExist:
                    Quantiter.create(quantiter=product['quantiter']).save()
                    this.quantiter = Quantiter.get(quantiter=product['quantiter'])
                    print("La quantiter n'existe pas dans la base de donner")
                    print("==>> ", float(str(this.quantiter)))
                    montant_product = float(str(this.quantiter)) * float(product['prix'])
                    product_list = Produit.create(nom_produit=product['nom_produit'],categorie=product['categorie'], quantiter=this.quantiter,prix_produit=product['prix'],etat=product['etat'],montant = montant_product).save()
                    print('Succesfully')
                    pass
                else:
                    print("La quantiter ou le produit Le produit existe deja dans la base de donner!")
                    print("L'objet existe et peut être utilisé.")
                    return False

    @classmethod
    def update_product(this,product:dict):
        try:
            Produit.get(nom_produit=product['nom_produit']),
            this.quantiter = Quantiter.get(quantiter=product['quantiter'])
        except Produit.DoesNotExist:
            print("Le produit specifique ne se trouve pas dans la base de donner")
            return False
        except Quantiter.DoesNotExist:
            print("La quantiter nexiste pas dans la base de donner!")
            Quantiter.create(quantiter=product['quantiter']).save()
            this.quantiter = Quantiter.get(quantiter=product['quantiter'])
        else:
            Produit.update(nom_produit=product['nom_produit'], prix_produit=product['prix'],
                           categorie=product['categorie'],
                           quantiter=this.quantiter).execute()
            print("Successfully update Option")


    def delete_product(self,prod:str):
        try:
            Produit.get(nom_produit=prod)
        except Produit.DoesNotExist:
            print("Produit does not exist")
            return False
            pass
        else:
            Produit.delete().where(Produit.nom_produit == prod).execute()
            print("Successfully delete")
            return True
        pass

    def search_produit(self):
        product_search = Produit.select().where(
            (Produit.nom_produit == (product['nom_produit'])) | (Produit.categorie == (product['categorie'])))
        for response in product_search:
            return response
        pass

    pass

    def All_product_list(self):
        data = []

        product = Produit.select().execute()
        for prod in product:
            print('Product:: ',prod.nom_produit)

            qt = Quantiter.select().where(Quantiter.id == prod.quantiter_id).filter().execute()
            # data.append(prod.)
            data.append(prod.id)
            data.append(prod.nom_produit)
            data.append(prod.categorie)
            data.append(qt[0].quantiter)
            print('Product::',qt[0].quantiter)
            print('Product::',prod.quantiter_id)
            data.append(prod.prix_produit)
            data.append(prod.etat)
            data.append(prod.montant)
        # print("DATA: ", data)
        chunk_size = 7
        chunks = []

        for i in range(0, len(data), chunk_size):
            chunks.append(data[i:i + chunk_size])
        # Afficher les sous-tableaux
        print(chunks)
        return chunks

        pass

    def selectFiew(self):
        prods = Produit.select().execute()
        categorie = []
        for prod in prods:
            print('Produit:: ',prod.categorie)
            categorie.append(prod.categorie)
        print(f'Categorie::: {categorie}')

        return categorie
    pass
