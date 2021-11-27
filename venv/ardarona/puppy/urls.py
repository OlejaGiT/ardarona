from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>', views.get_puppy, name='family'),
    path('', views.NewsListView.as_view(), name='puppy'),
    
]
