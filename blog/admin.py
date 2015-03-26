from django.contrib import admin

from blog.models import Post, Image

class ImageInline(admin.TabularInline):
    model = Post.images.through

class ImageAdmin(admin.ModelAdmin):
    model = Image

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Meta',    {'fields': ['title', 'slug']}),
        ('Content', {'fields': ['body']})
    ]
    prepopulated_fields = {'slug': ['title']}
    inlines = [ImageInline]


admin.site.register(Post, PostAdmin)
admin.site.register(Image, ImageAdmin)
