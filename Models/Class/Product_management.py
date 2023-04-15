import sys

sys.path.append('../../Controler/Data/Models')

from Controler.Data.Models.Produit_Model import Produit


class Product_manager():

    def create_product(self):
        # if not product:
        #     return False
        # else:
        """
         nom_produit
         prix_produit
         #categorie
         #quantiter
        """
        product_list = Produit(nom_produit='Nike', prix_produit=20000.0, categorie='Chassure', quantiter=1).save()
        print('Successfully insertion')

    # pass

    pass
