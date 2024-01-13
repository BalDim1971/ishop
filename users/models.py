from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):
    '''
    Класс, описывающий модель пользователь
    Стандартная модель расширяется:
    «Аватар»,
    «Номер телефона»,
    «Страна».
    Авторизация меняется на email
    '''
    
    username = None
    email = models.EmailField(max_length=200, verbose_name='электронная почта', unique=True)
    
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
