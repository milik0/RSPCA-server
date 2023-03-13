from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings

"""
The urls.py file defines the different urls that are available in the app
    * index: The index page of the app (the page that lists all the animals : Read)
    * edit: The edit page of the app (the page that allows the user to edit an animal : Update)
    * create: The create page of the app (the page that allows the user to create an animal : Create)
    * delete: The delete page of the app (the page that allows the user to delete an animal : Delete)
"""
app_name = 'app'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.EditAnimalView.as_view(), name='edit'),
    path('create/', views.AnimalView.as_view(), name='create'),
    path('delete/<int:pk>/', views.DeleteAnimalView.as_view(), name='delete')
    #path('<int:animal_id>/choose/', views.choose, name='choose')
]

"""
The following line is used to serve the media files (images) in development mode
"""
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
