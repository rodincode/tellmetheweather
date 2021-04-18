from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('weather',views.weatherview,name='weather'),
    path('spotify',views.spotifyview,name='spotify')
]
