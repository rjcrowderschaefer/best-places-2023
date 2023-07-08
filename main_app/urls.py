from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('places/', views.PlacesList.as_view(), name='places_list'),
    path('places/cultural-riches/', views.CulturalRichesCategory.as_view(), name='cultural_riches'),
    path('places/food-wine/', views.FoodWineCategory.as_view(), name="food_wine"),
]