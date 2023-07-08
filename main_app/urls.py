from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('places/', views.PlacesList.as_view(), name='places_list'),
    path('places/new', views.PlaceCreate.as_view(), name='place_create'),
    path('places/cultural-riches/', views.CulturalRichesCategory.as_view(), name='cultural_riches'),
    path('places/food-wine/', views.FoodWineCategory.as_view(), name="food_wine"),
    path('places/big-city-thrills/', views.BigCityThrillsCategory.as_view(), name="big_city_thrills"),
    path('places/moments-water/', views.MomentsWaterCategory.as_view(), name='moments_water'),
    path('places/fresh-air-nature/', views.FreshAirNatureCategory.as_view(), name="fresh_air_nature"),
    path('places/beach-vibes/', views.BeachVibesCategory.as_view(), name='beach_vibes'),
    path('places/the-future/', views.TheFutureCategory.as_view(), name='the_future'),
]