from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    # Display these fields in the admin list view for Product.
    list_display =('id','title','time_create', 'photo','is_published')
    list_display_links = ('id','title')
    search_fields = ('title','content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')

class CategoryAdmin(admin.ModelAdmin):
    # Display these fields in the admin list view for Category.

    list_display =('id' , 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

# Register the Product,Category model with its admin options.

admin.site.register(Product)

admin.site.register(Category, CategoryAdmin)
