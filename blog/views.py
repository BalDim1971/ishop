from django.views.generic import CreateView

from blog.models import Blog


class BlogCreteView(CreateView):
	model = Blog
	fields = ('title', 'slug', 'body',)
	