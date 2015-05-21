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


class RecipeInline(admin.StackedInline):
    model = Recipe
    extra = 0
    filter_vertical = ['ingredients']
    fieldsets = [
        (None, {'fields': ('name',)}),
        ('Details',
            {'fields': ('description', 'ingredients_text',
                        'instructions', 'ingredients')}),
        ('Times', {'fields': ('prep_time', 'cook_time')}),
        ('Nutrition', {'fields': ('calories',)}),
        ('Tags', {'fields': (('season', 'diets', 'meal_type'))})
    ]


class PostAdmin(admin.ModelAdmin):
    list_display = ('type', 'title', 'written_on', 'published')
    list_display_links = ('title',)
    fieldsets = [
        ('Meta',    {'fields': ['title', 'slug', 'type', 'published', 'tags']}),
        ('Content', {'fields': ['body', 'header_image']})
    ]
    prepopulated_fields = {'slug': ['title']}
    inlines = [ImageInline, RecipeInline]


class RecipeAdmin(admin.ModelAdmin):
    ordering = ['name']
    filter_horizontal = ['ingredients']
    fieldsets = [
        (None, {'fields': ('name', 'post')}),
        ('Details',
            {'fields': ('description', 'ingredients_text',
                        'instructions', 'ingredients')}),
        ('Times', {'fields': (('prep_time', 'cook_time'),)}),
        ('Nutrition', {'fields': ('calories',)}),
        ('Tags', {'fields': (('season', 'diets', 'meal_type'))})
    ]


admin.site.register(Post, PostAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Diet, DietAdmin)
admin.site.register(MealType, MealTypeAdmin)
admin.site.register(Recipe, RecipeAdmin)