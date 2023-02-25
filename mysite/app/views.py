from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Animal


class IndexView(generic.ListView):
    template_name = 'app/index.html'
    context_object_name = 'latest_animal_list'

    def get_queryset(self):
        """Return the last five published animals."""
        return Animal.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Animal
    template_name = 'app/detail.html'

def choose(request, animal_id):
    return HttpResponse("You're choosing animal %s." % animal_id)
