"""
URL configuration for cv_builder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin  # Django admin module
from django.urls import path       # URL routing
from authentication.views import *  # Import views from the authentication app
from django.conf import settings   # Application settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns  # Static files serving
from django.conf.urls.static import static
from home.views import *
 
# Define URL patterns
urlpatterns = [
    path('home/', home, name="recipes"),      # Home page
    path("admin/", admin.site.urls),          # Admin interface
    path('', login_page, name='login_page'),    # Login page
    path('register/', register_page, name='register'),  # Registration page
    path('logout/',user_lgot,name='logout'),
    path('home2', home2, name = 'home'), 
    path('resume/', gen_resume, name = 'resume'),
     path('editresume/', edit_resume, name = 'edit_resume'),  
    path('profile/', profile_view, name='profile_view'),
    
]
 
# Serve media files if DEBUG is True (development mode)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 
# Serve static files using staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()