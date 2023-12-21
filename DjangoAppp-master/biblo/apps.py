from django.apps import AppConfig

class BibloConfig(AppConfig):
    # Use a large auto field for model identifiers.
    default_auto_field = 'django.db.models.BigAutoField'
    # Set the name of the application to "biblo".
    name = 'biblo'
    # Human-readable name for display in the Django admin panel.
    verbose_name = 'Book'
