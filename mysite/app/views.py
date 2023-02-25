from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Animal


class IndexView(generic.ListView):
    template_name = 'app/index.html'
    context_object_name = 'latest_animal_list'

    def get_queryset(self):
        """Return the last five published animals."""
        return
    Animal.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Animal
    template_name = 'app/detail.html'
    def get_queryset(self):
        """Excludes any animals that aren't published yet"""
        return Animal.objects.filter(pub_date__lte=timezone.now())

def choose(request, animal_id):
    return HttpResponse("You're choosing animal %s." % animal_id)
