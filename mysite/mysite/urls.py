"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_url = 'http://127.0.0.1:8000/app'  # Removes the 'View Site' link
admin.site.site_header = 'Check Website'

"""
The urls.py file defines the different urls that are available in the app
    * admin: The admin page of the app (the page that allows the user to manage the app)
    * accounts: The accounts page of the app (the page that allows the user to manage their account)
    * app: The app page of the app (the page that allows the user to use the app)
    * accounts: The accounts page of the app (the page that allows the user to manage their account)
"""
urlpatterns = [
    path('yourarenotgettingintotheadminpage/', admin.site.urls), # The admin url is not the default one to prevent people from accessing it
    path('accounts/', include('django.contrib.auth.urls')),
    path("accounts/", include("accounts.urls")),
    path('', include('app.urls'), name='info'),
    #path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('', TemplateView.as_view(template_name='app/index.html'), name='home'),
]
"""
The static() helper function allows you to serve static files during development
    * settings.MEDIA_URL: The url to the media folder
    * document_root: The root of the media folder
"""
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
