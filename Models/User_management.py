import sys

sys.path.append('../Controler')

from Controler.Data.Models import User_Model


class User_manager(object):
    def __init__(self):
        self.users = User_Model.User()

    def create_user(self, user: dict):
        print('Creating user', user)
        if len(user) != 0:
            user_info = self.users.select().where((User_Model.User.email == user['email']))
            if not user_info:
                User_Model.User(nom=user['nom'], prenom=user['prenom'], username=user['username'],
                                email=user['email'],
                                tel=user['tel'], password=user['password'], profile=user['profil_id']).save()
                print("Success")
                return
            else:
                print(user_info)
                print('User existed')
                return False
        pass

    def update_user(self, user: dict):
        if len(user) != 0:
            user_email = self.users.select().where((User_Model.User.email == user['email']))
            if not user_email:
                print('User does not exist')
                return False
            else:
                for i in user_email:
                    id = i.id
                    print(f"==> id: {id}")
                self.users.update(nom=user['nom'], prenom=user['prenom'], username=user['username'],
                                  email=user['email'],
                                  tel=user['tel'], password=user['password'], profile=user['profil_id']).where(
                    User_Model.User.id == id).execute()
                print('Successfully update')
                return
        pass

    def delete_user(self, user: dict):
        user_email = self.users.select().where((User_Model.User.email == (user['email'])))
        for i in user_email:
            id = i.id
            print(f"==> id: {id}")
        self.users.delete().where(
            User_Model.User.id == id).execute()
        print('Successfully delete')
        return
        pass

    def search_user(self, user: dict):
        user_search = self.users.select().where(
            (User_Model.User.email == (user['email'])) | (User_Model.User.email == (user['tel'])))
        for response in user_search:
            return response
        pass
