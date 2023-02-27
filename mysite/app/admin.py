from django.contrib import admin

# Register your models here.
from .models import Animal, Species

"""class AnimalAdmin(admin.ModelAdmin):
    fieldsets = [
            (None,               {'fields': ['species']}),
            ('Date information', {'fields': ['pub_date']}),
    ]
    list_display = ('species', 'pub_date', 'was_published_recently')
    # Adding a filter for the research
    list_filter = ['pub_date']
    search_fields = ['species']
admin.site.register(Animal, AnimalAdmin)"""

admin.site.register(Animal)
admin.site.register(Species)
