from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q

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


# @login_required(login_url='/login/')
def create_post(request):
	if request.method == "POST" and request.FILES['document']:
		doc = request.FILES['document']
		title = request.POST['title']
		# image = request.POST['image']
		# snippet = request.POST['snippet']
		# content = request.POST['content']
		post = Post.objects.create(user=request.user, title=title, document=doc)
		post.save()
	return render(request, 'create_post.html')


@login_required(login_url='/accounts/login/')
def update_post(request, slug):
	Post = Post.objects.get(slug=slug)
	print('url = ', Post.get_absolute_url())
	form = CreatePost(request.POST or None,
	                     request.FILES or None, instance=Post,)
	if request.method == "POST":
		form = CreatePost(request.POST or None, instance=Post)
		if form.is_valid():
			form.save()
			return redirect(Post.get_absolute_url())
	return render(request, 'Posts/create_Post.html', {'form': form})


@login_required(login_url='/accounts/login/')
def delete_post(request, slug):
	Post = Post.objects.get(slug=slug)
	Post.delete()
	return redirect('/')
