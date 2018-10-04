from django.core.management.base import BaseCommand

from models.models import Users


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        print("Cantidad de Usuarios antes:", Users.objects.all().count())

        username = input("Ingrese el usuario: ")
        name = input("Ingrese el nombre: ")
        password = input("Ingrese el password: ")
        introduced_user = Users(username=username, name=name, password=password)
        introduced_user.save()

        print("Cantidad de Usuarios despues:", Users.objects.all().count())
