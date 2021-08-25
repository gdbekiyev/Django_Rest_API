from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class Users(AbstractUser):
    user_types = (
        ('1', 'Admin'),
        ('2', 'User'),
    )
    user_type = models.CharField(max_length=10, default='1', choices=user_types)


class Tema(models.Model):
    name = models.CharField(max_length=500, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()


class Sorag_Type(models.Model):
    name = models.CharField(max_length=500)


class Sorag(models.Model):
    name = models.CharField(max_length=500)
    type = models.ForeignKey(Tema, on_delete=models.CASCADE)
    model_type = models.ForeignKey(Sorag_Type, on_delete=models.CASCADE)

class Result(models.Model):
    user = models.ForeignKey(Users,on_delete=models.SET_NULL,blank=True,null=True)
    tema = models.ForeignKey(Tema,on_delete=models.CASCADE)


