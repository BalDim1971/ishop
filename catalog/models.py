from django.db import models

NULLABLE = {'blank': True, 'null': True}


# Create your models here.

class Category(models.Model):
	'''
	Класс-модель, описывающий некоторую категорию продуктов.
	'''
	
	name = models.CharField(max_length=50, verbose_name='Наименование', db_index=True)
	description = models.TextField(verbose_name='Описание', **NULLABLE)
	
	def __str__(self):
		# Строковое отображение категории
		return f'{self.name} ({self.description})'
	
	class Meta:
		verbose_name = 'категория'  # Настройка наименования одного объекта
		verbose_name_plural = 'категории'  # Настройка для наименования набора
		ordering = ('name',)


class Product(models.Model):
	'''
	Класс-модель, описывающий некий продукт.
	'''
	
	name = models.CharField(max_length=50, verbose_name='Наименование')
	description = models.TextField(verbose_name='Описание')
	preview = models.ImageField(upload_to='product/', verbose_name='Изображение', **NULLABLE)
	category = models.ForeignKey(to='Category', on_delete=models.CASCADE, verbose_name='Категория')
	price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена за штуку')
	date_create = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
	date_last_change = models.DateTimeField(auto_now_add=True, verbose_name='Дата последнего изменения')
	
	def __str__(self):
		# Строковое отображение продукта
		return f'{self.name} ({self.category}) {self.price}'
	
	class Meta:
		verbose_name = 'товар'  # Настройка наименования одного объекта
		verbose_name_plural = 'товары'  # Настройка для наименования набора
		ordering = ('name',)


class VersionProduct(models.Model):
	'''
	Класс-модель, описывающий версию товара
	'''
	
	product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
	version_number = models.IntegerField(verbose_name='номер версии')
	version_name = models.CharField(max_length=50, verbose_name='название версии')
	version_sign = models.BooleanField(verbose_name='признак версии', default=False)
	
	def __str__(self):
		# Строковое представление версии товара
		return f'{self.version_name}'
	
	class Meta:
		verbose_name = 'версия'
		verbose_name_plural = 'версии'
