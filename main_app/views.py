from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View
from django.http import HttpResponse
from .models import Place
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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

# class Places:
#     def __init__(self, type, name, image, bio):
#         self.type = type
#         self.name = name
#         self.image = image
#         self.bio = bio

class PlacesList(TemplateView):
    template_name = "place_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["places"] = Place.objects.all()
        # context["places"] = places
        return context
    
class PlaceCreate(CreateView):
    model = Place
    fields = ['type', 'typefull', 'name', 'image', 'bio']
    template_name = "place_create.html"
    success_url = "/places/"

class PlaceUpdate(UpdateView):
    model = Place
    fields = ['type', 'typefull', 'name', 'image', 'bio']
    template_name = "place_update.html"
    success_url = "/places/"

class PlaceDelete(DeleteView):
    model = Place
    template_name = "place_delete_confirmation.html"
    success_url = "/places/"

class CulturalRichesCategory(TemplateView):
    template_name = "cr_category.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["places"] = Place.objects.filter(name__icontains=name)
            context["header"] = f'Search results for "{name}"'
        else:
            context["places"] = Place.objects.all()
        return context
    
class FoodWineCategory(TemplateView):
    template_name = "fw_category.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["places"] = Place.objects.filter(name__icontains=name)
            context["header"] = f'Search results for "{name}"'
        else:
            context["places"] = Place.objects.all()
        return context
    
class BigCityThrillsCategory(TemplateView):
    template_name = "bt_category.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["places"] = Place.objects.filter(name__icontains=name)
            context["header"] = f'Search results for "{name}"'
        else:
            context["places"] = Place.objects.all()
        return context
    
class MomentsWaterCategory(TemplateView):
    template_name = "mw_category.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["places"] = Place.objects.filter(name__icontains=name)
            context["header"] = f'Search results for "{name}"'
        else:
            context["places"] = Place.objects.all()
        return context
    
class FreshAirNatureCategory(TemplateView):
    template_name = "fn_category.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["places"] = Place.objects.filter(name__icontains=name)
            context["header"] = f'Search results for "{name}"'
        else:
            context["places"] = Place.objects.all()
        return context
    
class BeachVibesCategory(TemplateView):
    template_name = "bv_category.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["places"] = Place.objects.filter(name__icontains=name)
            context["header"] = f'Search results for "{name}"'
        else:
            context["places"] = Place.objects.all()
        return context

class TheFutureCategory(TemplateView):
    template_name = "tf_category.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["places"] = Place.objects.filter(name__icontains=name)
            context["header"] = f'Search results for "{name}"'
        else:
            context["places"] = Place.objects.all()
        return context