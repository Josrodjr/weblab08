from django.core.management.base import BaseCommand

from models.models import Users, Posts, PostUserLike

from models.models import Users, Posts, PostUserLike
import models.instagramactions as function

class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        menu_value = function.menu()
        logged_in_user = 0
        
        while menu_value != 4:
          
          #test for the first case
          if menu_value == 1:
            function.create_user()
          if menu_value == 2:
            function.list_users()
          if menu_value == 3:
            id_query = input("Id de usuario")
            logged_in_user = function.login_user(id_query)
            if logged_in_user != 0:
              print("ACTUAL USER: " + str(logged_in_user.name) + " USERNAME: " + str(logged_in_user.username)) 
          if menu_value == 0:
            print("El numero ingresado no es valido, porfavor reingrese la opcion")
          #check for the menu again and ask for the option value
          menu_value = function.menu()