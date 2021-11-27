from django import template
from main.models import PrilTeam


register = template.Library()


@register.simple_tag()
def get_pril():
    return PrilTeam.objects.all()


