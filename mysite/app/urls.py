from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'app'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.EditAnimalView.as_view(), name='edit'),
    path('create/', views.AnimalView.as_view(), name='create'),
    path('delete/<int:pk>/', views.DeleteAnimalView.as_view(), name='delete')
    #path('<int:animal_id>/choose/', views.choose, name='choose')
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
