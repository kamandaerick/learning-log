"""Define url patterns for user management"""

from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    # Include the default auth urls
    path('', include('django.contrib.auth.urls')),
    # Registration page
    path('register/', views.register, name='register'),
]


