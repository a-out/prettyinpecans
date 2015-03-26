from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from blog.models import Post

def index(request):
    return HttpResponse("hello world")

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/detail.html', {'post': post})
