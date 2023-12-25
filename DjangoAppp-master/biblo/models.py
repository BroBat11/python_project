from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Product(models.Model):
        # Fields for Product model
        product_id = models.IntegerField  # NOTE: This should be a method call, e.g., models.IntegerField()
        name = models.CharField(max_length=255, verbose_name="title")
        slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
        image = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="image")
        content = models.TextField(blank=True, verbose_name="content")
        author = models.TextField(blank=True, verbose_name="author")
        price = models.IntegerField  # NOTE: This should be a method call, e.g., models.IntegerField()
        is_published = models.BooleanField(default=True, verbose_name="publicasia")
        cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категории")
        user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

        # String representation of a Product instance
        def __str__(self):
            return self.name

        # Get absolute URL for a Product instance
        def get_absolute_url(self):
            return reverse('post', kwargs={'post_slug': self.slug})

        # Meta class for configuring the behavior of the Product model
        class Meta:
            verbose_name = 'Book'
            verbose_name_plural = 'Books'
            ordering = ['id']

    # Define the Category model
class Category(models.Model):
        # Fields for Category model
        name = models.CharField(max_length=255, db_index=True)
        slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

        # String representation of a Category instance
        def __str__(self):
            return self.name

        # Get absolute URL for a Category instance
        def get_absolute_url(self):
            return reverse('category', kwargs={'cat_id': self.pk})

        # Meta class for configuring the behavior of the Category model
        class Meta:
            verbose_name = 'Category'
            verbose_name_plural = 'Categories'  # Comment for Categories in plural form
