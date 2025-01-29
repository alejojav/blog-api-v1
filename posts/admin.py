from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted', 'last_updated')
    list_filter = ('author', 'date_posted')
    search_fields = ('title', 'content')
    ordering = ['date_posted']

admin.site.register(Post, PostAdmin)
