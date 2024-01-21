"""
Сервисные функции кэширования
"""

from django.conf import settings
from django.core.cache import cache

from catalog.models import Product, Category


def get_cache_product_list():
    """
    Получение/сохранение кэшированного списка товаров
    :return: список товаров
    """
    
    product_list = None
    key = 'product_list'
    
    if settings.CACHE_ENABLED:
        product_list = cache.get(key)
        if product_list is None:
            product_list = Product.objects.filter(status='Активна')
            cache.set(key, product_list, 3600)
    else:
        product_list = Product.objects.filter(status='Активна')
    
    return product_list


def get_category_cache():
    """
    Получение/сохранение кэшированного списка категорий
    :return: список категорий
    """
    
    category_list = None
    key = 'category_list'
    
    if settings.CACHE_ENABLED:
        category_list = cache.get(key)
        
        if category_list is None or not settings.CACHE_ENABLED:
            category_list = Category.objects.all()
            cache.set(key, category_list)
    else:
        category_list = Category.objects.all()
    
    return category_list
