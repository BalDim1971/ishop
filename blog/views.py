'''
Представления для задачи Блог
'''

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, DeleteView, ListView, DetailView, UpdateView
from django.urls import reverse_lazy, reverse
from django.shortcuts import render
from pytils.translit import slugify

from blog.models import Blog


class BlogCreateView(CreateView):
	model = Blog
	fields = ('title', 'body',)
	success_url = reverse_lazy('catalog:index')
	
	# success_url = reverse_lazy('blog:list')
	
	def form_valid(self, form):
		if form.is_valid():
			new_blog = form.save()
			new_blog.slug = slugify(new_blog.title)
			new_blog.save()
		return super().form_valid(form)


class BlogListView(LoginRequiredMixin, ListView):
	model = Blog
	
	def get_queryset(self, *args, **kwargs):
		queryset = super().get_queryset(*args, **kwargs)
		queryset = queryset.filter(is_published=True)
		
		return queryset


class BlogDetailView(DetailView):
	model = Blog