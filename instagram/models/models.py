from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Users (models.Model):
  username = models.CharField(max_length=25)
  name = models.CharField(max_length=50)
  password = models.CharField(max_length=25)
  email = models.CharField(max_length=50)
#nombre appellido email username

class Posts (models.Model):
  title = models.CharField(max_length=50)
  post_info = models.CharField(max_length=125)
  #likes = models.ManyToManyField(Users, through='PostUserLike')
  iduser = models.ForeignKey(Users, null= False, on_delete=models.CASCADE)
  date = models.DateField(auto_now=True)

class PostUserLike(models.Model):
  user = models.ForeignKey(Users, on_delete=models.CASCADE)
  post = models.ForeignKey(Posts, on_delete=models.CASCADE)
  creation_datetime = models.DateTimeField(auto_now=True)


#acceder usando username y email

#salir -Adios.
