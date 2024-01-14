import random

from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE

code = ''.join([str(random.randint(0, 9)) for _ in range(12)])


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
    country = models.CharField(max_length=150, verbose_name='страна', **NULLABLE)
    
    is_active = models.BooleanField(default=True, verbose_name='почта проверена')
    email_verified = models.BooleanField(default=False, verbose_name='проверка почты')
    
    code = models.CharField(max_length=50, default=code, verbose_name='проверочный код', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    