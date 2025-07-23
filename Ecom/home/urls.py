from django.urls import path
from .views import index, places_view

urlpatterns = [
    path('', index, name='index'),
    path('api/places/', places_view, name='places_view'),
]