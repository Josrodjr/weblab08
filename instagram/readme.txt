>>Commandos de (env) -cuando hago cambios en la estructura de los 
py manage.py makemigrations
py manage.py migrate

py manage.py shell

>>Commandos de la Shell
from models.models import Users, Posts, PostUserLike

q = Users.objects.all()   --sacar la info de la db
q.save()            --guardar los cambios en la tupla
q = Users.objects.get(id=1)  --el id lo puedo cambiar por cualqueir otro query



//guardando aca
title = input("Ingrese el titulo de su post: ")
        post_info = input("Ingrese la informacion del post: ")
        introduced_post = Posts(title=title, post_info=post_info)
        introduced_post.save()