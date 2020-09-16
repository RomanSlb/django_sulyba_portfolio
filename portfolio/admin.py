from django.contrib import admin
from .models import Post

admin.site.register(Post)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'body', 'publish', 'status', 'image',)
    list_filter = ('status',)
    date_hierarchy = 'publish'
