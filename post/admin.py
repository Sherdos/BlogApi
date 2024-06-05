from django.contrib import admin

from post.models import Category, Post

# Register your models here. 

# admin.site.register(Post)
admin.site.register(Category)

@admin.register(Post)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    list_filter = ('created',)