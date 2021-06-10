from django.shortcuts import render, redirect
from .models import Post

def index(request):
	posts = Post.objects.all().order_by('-date')
	context = {
		'posts':posts,
	}
	return render(request, 'index.html', context)


def detail(request, slug):
	post = Post.objects.get(slug=slug)
	fposts = Post.objects.all().order_by('-date')[:3]
	context = {
		'post':post,
		'fposts':fposts,
	}
	return render(request, 'detail.html', context)
