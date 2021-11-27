from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import *


class RecListView(ListView):
    model = RecomendInfo
    template_name = 'rec/rec.html'
    context_object_name = 'rec'


def accordion(request):
    img = Accordion.objects.all()
    text = AccordionText.objects.all()
    recomend = RecomendInfo.objects.all()
    context ={
        'img':img,
        'text':text,
        'recomend':recomend
    }
    return render(request, 'rec/rec.html', context=context)
