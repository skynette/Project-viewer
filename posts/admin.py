from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'slug', 'date']
	list_display_links = ['title', 'slug']
	list_filter = ['date', 'user']
	search_fields = ['user', 'title']


admin.site.register(Post, PostAdmin)