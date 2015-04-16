from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic

from blog.models import Post, Recipe
from .forms import RecipeBrowserForm

class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_posts'

    def get_queryset(self):
        return Post.objects.published().order_by('-written_on')[:5]


class FoodIndexView(IndexView):
    def get_queryset(self):
        return Post.objects.food().order_by('-written_on')


class FashionIndexView(IndexView):
    def get_queryset(self):
        return Post.objects.fashion().order_by('-written_on')


class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'

def recipe_browser(request):
    if request.method == 'POST':
        form = RecipeBrowserForm(request.POST)
        if form.is_valid():
            filtered_recipes = Recipe.browser.filter(
                ingredients=form.cleaned_data['ingredients'])
            return render(request,
                    'blog/recipe_browser.html',
                    {'form': form, 'recipes': filtered_recipes, 'show_clear': True})
    else:
        form = RecipeBrowserForm()

    return render(request,
        'blog/recipe_browser.html',
        {'form': form, 'recipes': Recipe.browser.all(), 'show_clear': False})
