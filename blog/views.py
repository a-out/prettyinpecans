from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic

from blog.models import Post

class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_posts'

    def get_queryset(self):
        return Post.objects.order_by('-written_on')[:5]

class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'
