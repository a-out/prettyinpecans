from django.contrib import admin

from blog.models import Post, Image, Recipe, Ingredient, Diet, MealType

class ImageAdmin(admin.ModelAdmin):
    model = Image
    readonly_fields = ('image_tag',)


class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient


class DietAdmin(admin.ModelAdmin):
    model = Diet


class MealTypeAdmin(admin.ModelAdmin):
    model = MealType


class ImageInline(admin.TabularInline):
    model = Post.images.through


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Meta',    {'fields': [('title', 'slug')]}),
        ('Content', {'fields': ['body', 'header_image']}),
        (None, {'fields': ['recipes']})
    ]
    prepopulated_fields = {'slug': ['title']}
    inlines = [ImageInline]


class RecipeAdmin(admin.ModelAdmin):
    ordering = ['name']
    filter_horizontal = ['ingredients']
    fieldsets = [
        (None, {'fields': ('name',)}),
        ('Recipe Card', {'fields': ('ingredients_text', 'instructions', 'ingredients')}),
        ('Times', {'fields': (('prep_time', 'cook_time'),)}),
        ('Nutrition', {'fields': ('calories',)}),
        ('Tags', {'fields': (('season', 'diets', 'mealTypes'))})
    ]

admin.site.register(Post, PostAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Diet, DietAdmin)
admin.site.register(MealType, MealTypeAdmin)
admin.site.register(Recipe, RecipeAdmin)