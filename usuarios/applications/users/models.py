from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin #creacion de usuarios 

from .managers import UserManager

# Create your models here.
GENDER_CHOICES = (
    ('M', 'MASCULINO'),
    ('F', 'FEMENINO'),
    ('O', 'OTROS')
)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=10, unique=True)
    email = models.CharField()
    nombres = models.CharField(max_length=30,blank=True)
    apellidos = models.CharField(max_length=30,blank=True)
    genero = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    codregistro = models.CharField( max_length=6, blank=True)

    is_staff = models.BooleanField(default=False)#Especificar si puedo o no puede entrar al administrador
    is_active = models.BooleanField(default=False) #Verificar usuarios activos

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email',]

    objects = UserManager()
    
    def get_short_name(self):
        return self.username
    
    def get_full_name(self):
        return self.nombres + ' ' + self.apellidos

