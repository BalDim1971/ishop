from django.contrib import admin

# Register your models here.
from catalog.models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('pk', 'name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ('pk', 'name', 'price', 'category', 'date_create', 'date_last_change')
	list_filter = ('category',)
	search_fields = ('name', 'description',)
