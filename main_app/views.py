from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class PlaceList(TemplateView):
    template_name = "place_list.html"