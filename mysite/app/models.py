import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin
# Create your models here.

class Species(models.Model):
    """
    The species class defining the different species of animals that are
    available in a specific RSPCA site
        * name: The name of the species
    """
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Animal(models.Model):
    """
    The animal class defining the different animals that are available in a
    specific RSPCA site
        * species: The species of the animal
        * pub_date: The date the animal was published
        * name: The name of the animal
        * image: The image of the animal
    """
    species = models.ForeignKey(Species,on_delete=models.CASCADE) 
    pub_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='img_data/',default='d.png')
    #img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    def __str__(self):
        """
        Returns the name of the animal
            * name: The name of the animal
        """
        return self.species
    
    @admin.display(
            boolean=True,
            ordering='pub_date',
            description='Published recently?'
            )
    def was_published_recently(self):
        """
        Returns True if the animal was published recently
            * now: The current time
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


