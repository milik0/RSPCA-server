from django.contrib import admin

# Register your models here.
from .models import Animal

class AnimalAdmin(admin.ModelAdmin):
    fieldsets = [
            (None,               {'fields': ['species']}),
            ('Date information', {'fields': ['pub_date']}),
    ]

admin.site.register(Animal, AnimalAdmin)
