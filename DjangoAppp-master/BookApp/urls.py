from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from biblo.views import *  # Importing views from the 'biblo' app.
from rest_framework import routers
from BookApp import settings  # Importing settings from the 'BookApp' module.
# Define URL patterns for the application.
urlpatterns = [
    # Admin panel URL.
    path('admin/', admin.site.urls),
    # API URLs for handling Product operations.
    path('api/v1/product/', bibloAPIList.as_view()),
    path('api/v1/product/<int:pk>/', bibloAPIUpdate.as_view()),
    path('api/v1/productdelete/<int:pk>/', bibloAPIDestroy.as_view()),
    # URL patterns for Django Rest Framework (DRF) authentication.
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/auth/', include('djoser.urls')),  # new
    re_path(r'^auth/', include('djoser.urls.authtoken')),  # new
    # Token-related URLs for JWT authentication.
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # URL patterns for captcha.
    path('captcha/', include('captcha.urls')),
    # Default URL patterns for the main application.
    path('', include('biblo.urls')),
]

# Include additional URL patterns for debug mode.
if settings.DEBUG:
    import debug_toolbar

    # Add debug toolbar URLs in development mode.
    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns

    # Add URL patterns for serving media files in development mode.
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Define custom error handling views.
handler400 = 'biblo.views.handler400'
handler403 = 'biblo.views.handler403'
handler404 = 'biblo.views.handler404'
handler500 = 'biblo.views.handler500'
