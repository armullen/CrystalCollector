from django.urls import path
from . import views

urlpatterns = [
   path('', views.Home.as_view(), name='home'), 
   path('about/', views.About.as_view(), name="about"),
   path('crystals/', views.CrystalList.as_view(), name='crystal_list')
]