from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('', views.About.as_view(), name='about'),
    path('', views.PlacesList.as_view(), name='places_list'),
]