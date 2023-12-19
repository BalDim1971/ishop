import os

from django.shortcuts import render
from django.views.generic import ListView, DetailView

from catalog.models import Product
from config import settings


class ProductListView(ListView):
	model = Product
	template_name = 'catalog/index.html'


class ProductDetailView(DetailView):
	model = Product
	template_name = 'catalog/info.html'


def contact(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		message = request.POST.get('message')
		print(f'You have new message from {name} ({email}): {message}')
	return render(request, 'catalog/contacts.html')

