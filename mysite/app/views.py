from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Animal
from .forms import AnimalForm


class IndexView(generic.ListView):
    """
    The index view for the RSPCA site
        * template_name: The name of the template to use
        * context_object_name: The name of the context object to use
    """
    template_name = 'app/index.html'
    context_object_name = 'latest_animal_list'

    def get_queryset(self):
        """
        Return the last five published animals.
            * Animal: The animal model
            * objects: The objects of the animal model
            * order_by: The order of the objects
            * pub_date: The date the animal was published
            * timezone: The timezone of the animal
            * now: The current time
            * timedelta: The time difference
            * days: The number of days
        """
        return Animal.objects.order_by('-pub_date')[:5]
    #Animal.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class AnimalView(generic.CreateView):
    """
    The animal view for the RSPCA site
        * model: The model to use
        * form_class: The form class to use
        * template_name: The name of the template to use
        * success_url: The url to redirect to on success
    """
    model = Animal
    form_class = AnimalForm
    template_name = 'app/detail.html'
    success_url = '../'


class EditAnimalView(generic.UpdateView):
    """
    The edit animal view for the RSPCA site
        * model: The model to use
        * form_class: The form class to use
        * template_name: The name of the template to use
        * success_url: The url to redirect to on success
    """
    model = Animal
    form_class = AnimalForm
    template_name = 'app/edit.html'
    success_url = '../'

class DeleteAnimalView(generic.DeleteView):
    """
    The delete animal view for the RSPCA site
        * model: The model to use
        * template_name: The name of the template to use
        * success_url: The url to redirect to on success
    """
    model = Animal
    template_name = 'app/delete.html'
    success_url = '../../'

def choose(request, animal_id):
    return
#    return HttpResponse("You're choosing animal %s." % animal_id)
