from django.core.management.base import BaseCommand

from models.models import Users, Posts, PostUserLike


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        introduced_user = input("Ingrese un usuario para agregar un post: ")
        
        try:
          introduced_user_DB = Users.objects.get(username=introduced_user)
          #encontro un user con este user asi que ingresar el post por el
          print("Cantidad de posts antes (para el usuario " + introduced_user + "): ", PostUserLike.objects.filter(user=introduced_user_DB).count())  
          #crear un template de post
          title = input("Ingrese el titulo de su post: ")
          post_info = input("Ingrese la informacion del post: ")
          #crear el post y agregarlo a la tabla
          introduced_post = Posts(title=title, post_info=post_info)
          introduced_post.save()

          #agregar el post a el user
          #introduced_post.likes.add(introduced_user_DB) DOESNT WORK

          #post_info = PostUserLike()

          #imprimir el cambio en la cantidad de posts para el user
          print("Cantidad de posts despues (para el usuario " + introduced_user + "): ", PostUserLike.objects.filter(user=introduced_user_DB).count())

        except Users.DoesNotExist:
          print("No se encontro un usuario con el nombre de usuario proporcionado, no se agrego ningun post")