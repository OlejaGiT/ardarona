from django import template
from puppy.models import DogInfo
from puppy.models import PostImage
from main.models import PrilTeam


register = template.Library()

@register.simple_tag()
def get_puppy():
    return DogInfo.objects.all()


@register.simple_tag()
def get_post():
    return PostImage.objects.all()


@register.simple_tag()
def get_pril():
    return PrilTeam.objects.all()


