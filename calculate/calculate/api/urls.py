from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_number', views.add_number, name='add_number'),
    path('get_numbers', views.get_numbers, name='get_numbers'),
]