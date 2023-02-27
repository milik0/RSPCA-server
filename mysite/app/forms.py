from django import forms
from .models import Animal

class AnimalForm(forms.ModelForm):
    """
    The animal form for the RSPCA site
        * Meta: The meta class
            * model: The model to use
            * exclude: The fields to exclude
    """
    class Meta:
        model = Animal
        exclude = ['pub_date']
