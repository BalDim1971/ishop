from django.db import models


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
		# Начальные настройки?
		pass


class Category(models.Model):
	'''
	Класс-модель, описывающий некоторую категорию продуктов.
	'''
	
	name = models.CharField(max_length=50, verbose_name='наименование', db_index=True)
	description = models.TextField(verbose_name='описание')
	
	def __str__(self):
		# Строковое отображение категории
		return f'{self.name} {self.description}'
		
	class Meta:
		# Начальные настройки?
		pass
