from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse
from django.views import generic

from blog.models import BlogsPost


# Create your views here.

class indexView(generic.ListView):
	template_name = 'blog/index.html'
	context_object_name = 'posts'

	def get_queryset(self):
		return BlogsPost.objects.order_by('-timestamp')[:3]

class detailView(generic.DetailView):
	model = BlogsPost
	template_name = 'blog/detail.html'		
