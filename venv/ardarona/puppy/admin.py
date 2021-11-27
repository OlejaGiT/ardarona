
from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import *


class InfoAdminForm(forms.ModelForm):
    info = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = DogInfo
        fields = '__all__'


class PostImageAdmin(admin.StackedInline):
    model = PostImage

@admin.register(DogInfo)
class DogInfoAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]
    form = InfoAdminForm
    list_display = ('name', 'position', 'gender', 'status', 'pos')
    list_display_links = ('name', )
    search_fields = ('name', 'position__dog_position', 'gender__dog_gender', 'status__dog_status')
    class Meta:
        model = DogInfo

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass



admin.site.register(DogColor)
admin.site.register(DogGender)
admin.site.register(DogStatus)
admin.site.register(DogPosition)
admin.site.register(DogDisplayPuppy)
admin.site.register(DogDisplayGalery)
