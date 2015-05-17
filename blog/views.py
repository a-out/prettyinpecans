from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic

from blog.models import Post, Recipe
from .forms import RecipeBrowserForm, RecipeSearchForm
from newsletter.forms import SubscribeForm

class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_posts'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['at'] = 'home'
        context['subscribe_form'] = SubscribeForm()
        context['search_form'] = RecipeSearchForm()
        return context

    def get_queryset(self):
        return Post.objects.published().order_by('-written_on')[:5]


class FoodIndexView(IndexView):
    def get_queryset(self):
        return Post.objects.food().order_by('-written_on')

    def get_context_data(self, **kwargs):
        context = super(FoodIndexView, self).get_context_data(**kwargs)
        context['at'] = 'food'
        return context


class FashionIndexView(IndexView):
    def get_queryset(self):
        return Post.objects.fashion().order_by('-written_on')

    def get_context_data(self, **kwargs):
        context = super(FashionIndexView, self).get_context_data(**kwargs)
        context['at'] = 'fashion'
        return context


class TravelIndexView(IndexView):
    def get_queryset(self):
        return Post.objects.travel().order_by('-written_on')

    def get_context_data(self, **kwargs):
        context = super(TravelIndexView, self).get_context_data(**kwargs)
        context['at'] = 'travel'
        return context


class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['related_posts'] = Post.objects.related(context['post'])
        # todo: DRY -- inherit somehow
        context['subscribe_form'] = SubscribeForm()
        return context

def recipe_browser(request):
    if request.method == 'POST':
        form = RecipeBrowserForm(request.POST)
        if form.is_valid():
            filtered_recipes = Recipe.browser.filter(form.cleaned_data)
            return render(request,
                    'blog/recipe_browser.html',
                    {'form': form, 'recipes': filtered_recipes, 'show_clear': True, 'at': 'recipes'})
    else:
        form = RecipeBrowserForm()

    return render(request,
        'blog/recipe_browser.html',
        {'form': form, 'recipes': Recipe.browser.all(), 'show_clear': False, 'at': 'recipes'})
