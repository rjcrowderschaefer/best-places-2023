from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View
from django.http import HttpResponse

# Create your views here.

# class Home(View):

#     def get(self, request):
#         return HttpResponse("Best Places To Visit 2023")
    

# class About(View):

#     def get(self, request):
#         return HttpResponse("Best Places About")
    
# class PlacesList(View):

#     def get(self, request):
#         return HttpResponse("Best Places List")

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

# class PlaceList(TemplateView):
#     template_name = "place_list.html"