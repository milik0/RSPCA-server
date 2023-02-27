from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Animal
from .forms import AnimalForm


class IndexView(generic.ListView):
    template_name = 'app/index.html'
    context_object_name = 'latest_animal_list'

    def get_queryset(self):
        """Return the last five published animals."""
        return Animal.objects.order_by('-pub_date')[:5]
    #Animal.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class AnimalView(generic.CreateView):
    model = Animal
    form_class = AnimalForm
    template_name = 'app/detail.html'
    success_url = '../'


class EditAnimalView(generic.UpdateView):
    model = Animal
    form_class = AnimalForm
    template_name = 'app/edit.html'
    success_url = '../'

class DeleteAnimalView(generic.DeleteView):
    model = Animal
    template_name = 'app/delete.html'
    success_url = '../../'

def choose(request, animal_id):
    return
#    return HttpResponse("You're choosing animal %s." % animal_id)
