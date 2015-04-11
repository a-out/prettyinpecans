from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic

from blog.models import Post
from .forms import RecipeBrowserForm

class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_posts'

    def get_queryset(self):
        return Post.objects.order_by('-written_on')[:5]

class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'

def recipe_browser(request):
    if request.method == 'POST':
        form = RecipeBrowserForm(request.POST)
        if form.is_valid():
            return HttpResponse("valid")
    else:
        form = RecipeBrowserForm()

    return render(request, 'blog/recipe_browser.html', {'form': form})