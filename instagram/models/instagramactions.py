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

def menu_user():
  print("------------------------------------------------\n")
  print("Crear Post: 1 \nLike de Post: 2\nDelete Post: 3\nMenu Principal: 4")
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
  email = input("Ingrese el email: ")
  introduced_user = Users(username=username, name=name, password=password, email=email)
  introduced_user.save()
  print("Cantidad de Usuarios despues:", Users.objects.all().count())
  return 1

def list_users():
  print("------------------------------------------------\n")
  all_users = Users.objects.all()
  for user in all_users:
    print("ID: " + str(user.id) + " - Username: " + str(user.username) + " - Name: " + str(user.name) + " - Email: " + str(user.email) + "-")
  return 1

def login_user(username, password):
  print("------------------------------------------------\n")
  user_object = 0
  try:
    user_object = Users.objects.get(username=username, password=password)
  except Users.DoesNotExist:
    print("No hay usuario en la db con ese ID")
  return user_object

def create_post(user):
  title = input("Ingrese un titulo para su post: ")
  post_info = input("Ingrese un cuerpo para su post: ")
  
  introduced_post = Posts(title=title, post_info=post_info, iduser=user)
  introduced_post.save()

  print("Success, se ingreso el post")
  return 1

def like_post(user, selecteduser):
  all_posts_user = Posts.objects.filter(iduser = selecteduser)
  print("------------------------------------------------\n")
  for post in all_posts_user:
    likes = PostUserLike.objects.filter(post = post).count()
    print("ID: " + str(post.id) + " Titulo: " + str(post.title) + " Post Info: " + str(post.post_info) + " LIKES: " + str(likes))
  print("------------------------------------------------\n")
  post_for_like = input("ID del post al que le quiere dar like: ")

  try:
    post_object = Posts.objects.get(id = post_for_like)
    postlike = PostUserLike(user = user, post = post_object)
    postlike.save()
  except Posts.DoesNotExist:
    print("Id incorrecta")

  return 1
def delete_post(user):
  all_posts_user = Posts.objects.filter(iduser = user)
  print("------------------------------------------------\n")
  for post in all_posts_user:
    likes = PostUserLike.objects.filter(post = post).count()
    print("ID: " + str(post.id) + " Titulo: " + str(post.title) + " Post Info: " + str(post.post_info) + " LIKES: " + str(likes))
  print("------------------------------------------------\n")
  post_for_delete = input("Ingrese el ID de el post que quiere hacer delete: ")
  deletedpost = Posts.objects.get(id = post_for_delete)
  deletedpost.delete()
  print("Success, post deleted")
  return 1
