from django.contrib import admin
from .models import *


# Admin configuration for the Product model.
class ProductAdmin(admin.ModelAdmin):
    # Display these fields in the admin list view for Product.
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')

    # Make 'id' and 'title' clickable to navigate to the change view.
    list_display_links = ('id', 'title')
    # Enable searching by 'title' and 'content' in the admin.
    search_fields = ('title', 'content')
    # Allow editing 'is_published' directly from the list view.
    list_editable = ('is_published',)
    # Add filters for 'is_published' and 'time_create' in the admin sidebar.
    list_filter = ('is_published', 'time_create')


# Admin configuration for the Category model.
class CategoryAdmin(admin.ModelAdmin):
    # Display these fields in the admin list view for Category.
    list_display = ('id', 'name')
    # Make 'id' and 'name' clickable to navigate to the change view.
    list_display_links = ('id', 'name')
    # Enable searching by 'name' in the admin.
    search_fields = ('name',)

    # Automatically generate the 'slug' field based on the 'name'.
    prepopulated_fields = {"slug": ("name",)}


# Register the Product model with its admin options.
admin.site.register(Product, ProductAdmin)
# Register the Category model with its admin options.
admin.site.register(Category, CategoryAdmin)
