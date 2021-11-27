from django.shortcuts import render
from .models import About
from puppy.models import PostImage
from django.views.generic import DetailView, ListView



class AboutListView(ListView):
    model = About
    template_name = 'about/about.html'
    context_object_name = 'about'


class PostListView(ListView):
    model = PostImage
    template_name = 'about/about.html'
    context_object_name = 'post'


