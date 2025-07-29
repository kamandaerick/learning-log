"""Define url patterns for user management"""

from django.urls import path, include

app_name = 'users'

urlpatterns = [
    # Include the default auth urls
    path('', include('django.contrib.auth.urls')),
]


