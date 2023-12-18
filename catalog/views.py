import os

from django.shortcuts import render

from catalog.models import Product
from config import settings


def index(request):
	path = settings.MEDIA_ROOT
	img_list = os.listdir(os.path.join(path, 'images'))
	context = {
		'product_list': Product.objects.all,
		'title': 'Список продуктов',
		'images': img_list
	}
	return render(request, 'catalog/product.html', context)


def contact(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		message = request.POST.get('message')
		print(f'You have new message from {name} ({email}): {message}')
	return render(request, 'catalog/contacts.html')

def info(request):
    return render(request, 'catalog/info.html')
