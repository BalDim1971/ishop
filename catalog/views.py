import os

from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm, CategoryForm
from catalog.models import Product, VersionProduct, Category
from config import settings


class CategoryListView(ListView):
    model = Category
    template_name = 'catalog/category.html'
    extra_context = {
        'title': 'Список категорий товаров',
    }


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('catalog:category')
    extra_context = {
        'title': 'Создать категорию товара',
    }
    
    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.save()
        return super().form_valid(form)


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'catalog/category_info.html'
    extra_context = {
        'title': 'Подробно о категории',
    }


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('catalog:category')
    extra_context = {
        'title': 'Обновить данные о категории',
    }
    
    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.save()
        return super().form_valid(form)


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('catalog:category')
    extra_context = {
        'title': 'Удалить категорию',
    }


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/index.html'
    extra_context = {
        'title': 'Список товаров',
        'is_active_main': 'active'
    }
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['version'] = VersionProduct.objects.all()
        
        return context


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
        
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')
    extra_context = {
        'title': 'Обновить данные о товаре',
    }
    
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(self.model, VersionProduct, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        
        return context_data
    
    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        with transaction.atomic():
            self.object = form.save()
            if formset.is_valid():
                formset.instance = self.object
                formset.save()
        
        return super().form_valid(form)


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
