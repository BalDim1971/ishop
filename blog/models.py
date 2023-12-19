from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
	title = models.CharField(max_length=150, verbose_name='заголовок')
	slug = models.CharField(**NULLABLE, max_length=150, verbose_name='slug')
	body = models.TextField(verbose_name='содержимое')
	preview = models.ImageField(upload_to='blog/', verbose_name='превью', **NULLABLE)
	date_create = models.DateField(auto_now_add=True, verbose_name='дата создания')
	is_published = models.BooleanField(default=True, verbose_name='признак публикации')
	count_views = models.IntegerField(default=0, verbose_name='количество просмотров')
	
	def __str__(self):
		return f'{self.title} {self.slug}'
	
	class Meta:
		verbose_name = 'блог'
		verbose_name_plural = 'блоги'
