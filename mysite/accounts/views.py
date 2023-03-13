from django.shortcuts import render

# Create your views here.

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

class SignUpView(generic.CreateView):
    """
    The signup view for the RSPCA site
        * form_class: The form class to use
        * success_url: The url to redirect to on success
        * template_name: The name of the template to use
    """
    form_class = UserCreationForm
    #success_url = reverse_lazy("login")
    success_url = reverse_lazy("info")
    template_name = "registration/signup.html"
