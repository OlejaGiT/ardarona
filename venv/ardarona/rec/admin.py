from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from .models import *


admin.site.register(Title)
admin.site.register(RecomendInfo)
admin.site.register(Accordion)
admin.site.register(AccordionText)
admin.site.register(RecomendLogo)
