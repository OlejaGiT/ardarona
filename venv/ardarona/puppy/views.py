from typing import Any, Tuple

from django.shortcuts import render, get_object_or_404
from .models import DogInfo, PostImage
from django.views.generic import DetailView, ListView



class NewsDetailView(DetailView):
    model = DogInfo
    template_name = 'puppy/family.html'
    context_object_name = 'family'


class NewsListView(ListView):
    model = DogInfo
    template_name = 'puppy/puppy.html'
    context_object_name = 'dog'


class PostDetailView(DetailView):
    model = PostImage
    template_name = 'puppy/family.html'
    context_object_name = 'photos'



class AboutListView(ListView):
    model = DogInfo
    template_name = 'puppy/about.html'
    context_object_name = 'dog'


class PhotoListView(ListView):
    model = PostImage
    template_name = 'puppy/about.html'
    context_object_name = 'photos'


def get_puppy(request, pk):
    puppy = DogInfo.objects.filter(father__id=pk)
    mot = DogInfo.objects.filter(mother__id=pk)
    family = DogInfo.objects.get(pk=pk)
    photos = PostImage.objects.filter(post=pk)
    context={
        "puppy":puppy,
        "mot":mot,
        "family":family,
        "photos":photos,
    }
    return render(request, 'puppy/family.html', context=context)


