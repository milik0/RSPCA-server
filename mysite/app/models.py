import datetime

from django.db import models
from django.utils import timezone
# Create your models here.

class Animal(models.Model):
    """The animal class defining the different animals that are available in a
    specific RSPCA site"""
    species = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    #img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    def __str__(self):
        return self.species
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
