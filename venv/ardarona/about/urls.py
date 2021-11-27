from django.urls import path
from . import views


urlpatterns = [
    path('', views.AboutListView.as_view(), name='about'),
    path('', views.PostListView.as_view(), name='post'),

]
