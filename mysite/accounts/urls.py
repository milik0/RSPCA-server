from django.urls import path

from .views import SignUpView

"""
The urls.py file defines the different urls that are available in the app
    * signup: The signup page of the app (the page that allows the user to create an account)
"""
urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
]
