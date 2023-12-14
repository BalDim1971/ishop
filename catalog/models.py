from django.db import models


# Create your models here.

class Product(models.Model):
	
	def __str__(self):
		# Строковое отображение продукта
		return f'{"product1"} {"product2"}'
	
	class Meta:
		# Начальные настройки?
		pass


class Category(models.Model):
	
	def __str__(self):
		# Строковое отображение категории
		return f'{"category1"} {"category2"}'
		
	class Meta:
		# Начальные настройки?
		pass
