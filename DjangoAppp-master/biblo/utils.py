# Import all models from the current module or package (assuming they are defined in __init__.py)
from .models import *

# Define a list representing the main menu items
menu = ["about", "Log In", "Categories"]

# This mixin class can be used by other views to easily provide common data to templates.
class DataMixin:
    # Set a default value for pagination (8 items per page)
    paginate_by = 8

    # Define a method to get user-related context data
    def get_user_context(self, **kwargs):
        # Extract context data from the keyword arguments
        context = kwargs
        # Retrieve all categories from the Category model
        cats = Category.objects.all()
        # Create a copy of the menu list
        user_menu = menu.copy()
        # If the user is not authenticated, remove the "Log In" item from the menu
        if not self.request.user.is_authenticated:
            user_menu.pop(1)
        # Add menu and categories to the context
        context['menu'] = user_menu
        context['cats'] = cats
        # If 'cat_selected' is not already in the context, set its default value to 0
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        # Return the updated context
        return context
