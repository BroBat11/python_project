from django.urls import path
from django.urls import path, include
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
# Each URL pattern is associated with a specific view, and the comments provide
# a brief description of each pattern
path('',cache_page(60)( ProductHome.as_view()), name='home'),
# Mapping the '/about/' URL to the about view.
path('about/', about, name='about'),
path('addpage/', AddPage.as_view(), name='addpage'),
path('login/', LoginUser.as_view(), name='login'),
path('logout/', logout_user, name='logout'),
path('register/', RegisterUser.as_view(), name='register'),
    # URL pattern for category page with dynamic category ID, mapped to 'show_category' view
    path('category/<int:cat_id>/', show_category, name='category'),
path('contact/', ContactFormView.as_view(), name='contact'),
    # URL pattern for post page with dynamic post slug, mapped to 'ShowPost' view
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
]