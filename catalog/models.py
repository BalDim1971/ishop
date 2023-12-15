from django.db import models
from django.utils import timezone


# Create your models here.

class Product(models.Model):
	'''
	Класс-модель, описывающий некий продукт.
	'''
	
	name = models.CharField(max_length=50, verbose_name='наименование')
	description = models.TextField(verbose_name='описание')
	preview = models.ImageField(verbose_name='превью')
	category = models.ForeignKey('Category', on_delete=models.PROTECT)
	price = models.IntegerField(verbose_name='цена за штуку')
	date_create = models.DateTimeField(verbose_name='время создания')
	date_last_change = models.DateTimeField(verbose_name='время последнего изменения')
	
	def __str__(self):
		# Строковое отображение продукта
		return f'{self.name} {self.description}'
	
	class Meta:
		verbose_name = 'товар'  # Настройка наименования одного объекта
		verbose_name_plural = 'товары'   # Настройка для наименования набора


class Category(models.Model):
	'''
	Класс-модель, описывающий некоторую категорию продуктов.
	'''
	
	name = models.CharField(max_length=50, verbose_name='наименование', db_index=True)
	description = models.TextField(verbose_name='описание')
	
	def __str__(self):
		# Строковое отображение категории
		return f'{self.name} {self.description} {self.created_at}'
		
	class Meta:
		verbose_name = 'категория'  # Настройка наименования одного объекта
		verbose_name_plural = 'категории'   # Настройка для наименования набора
