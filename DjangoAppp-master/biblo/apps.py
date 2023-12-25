from django.apps import AppConfig

class BibloConfig(AppConfig):
    # This class is used for application-specific configurations.
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'biblo'
    # Human-readable name for display in the Django admin panel.
    verbose_name = 'Book'
