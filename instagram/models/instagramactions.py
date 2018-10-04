from models.models import Users, Posts, PostUserLike

def fib():
  print("success")

def menu():
  print("------------------------------------------------\n")
  print("Crear Usuarios: 1 \nListar Usuarios: 2 \nAcceder: 3 \nSalir: 4")
  try:
    menu_value = int(input("Opcion:"))
  except:
    menu_value = 0
  return menu_value


def create_user():
  print("------------------------------------------------\n")
  print("Cantidad de Usuarios antes:", Users.objects.all().count())
  username = input("Ingrese el usuario: ")
  name = input("Ingrese el nombre: ")
  password = input("Ingrese el password: ")
  introduced_user = Users(username=username, name=name, password=password)
  introduced_user.save()
  print("Cantidad de Usuarios despues:", Users.objects.all().count())
  return 1

def list_users():
  print("------------------------------------------------\n")
  all_users = Users.objects.all()
  for user in all_users:
    print("ID: " + str(user.id) + " - Username: " + str(user.username) + " - Name: " + str(user.name) + "-")
  return 1

def login_user(provided_id):
  print("------------------------------------------------\n")
  user_object = 0
  try:
    user_object = Users.objects.get(id=provided_id)
  except Users.DoesNotExist:
    print("No hay usuario en la db con ese ID")
  return user_object