import os

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
from catalog.models import Product
from config import settings


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/index.html'
    extra_context = {
        'title': 'Список товаров',
    }


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/info.html'
    extra_context = {
        'title': 'Подробная информация',
    }


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')
    extra_context = {
        'title': 'Новый товар',
    }
    
    def form_valid(self, form):
        instance = form.save()
        instance.autor = self.request.user
        # send_order_email()
        
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')
    extra_context = {
        'title': 'Обновить данные о товаре',
    }


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:index')
    extra_context = {
        'title': 'Удалить данные о товаре',
    }


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'You have new message from {name} ({email}): {message}')
    return render(request, 'catalog/contacts.html')
