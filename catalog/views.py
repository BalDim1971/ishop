import os

from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, VersionProduct
from config import settings


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/index.html'
    extra_context = {
        'title': 'Список товаров',
    }
    
    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['is_active_main'] = True
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
        # send_order_email()
        
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
        VersionFormset = inlineformset_factory(Product, VersionProduct, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)

        return context_data
    
    def form_valid(self, form):
        formset = self.get_context_data()['formset']
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
