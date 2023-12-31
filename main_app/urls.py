from django.urls import path
from . import views

urlpatterns = [
   path('', views.Home.as_view(), name='home'), 
   path('about/', views.About.as_view(), name="about"),
   path('crystals/', views.CrystalList.as_view(), name='crystal_list'),
   path('crystal/new/', views.CrystalCreate.as_view(), name='crystal_create'),
   path('crystals/<int:pk>/', views.CrystalDetail.as_view(), name='crystal_detail'),
   path('crystals/<int:pk>/update', views.CrystalUpdate.as_view(), name='crystal_update'),
   path('crystals/<int:pk>/delete', views.CrystalDelete.as_view(), name="crystal_delete"),
   path('crystals/<int:pk>/uses/new', views.UseCreate.as_view(), name='use_create'),
   path('wishlists/<int:pk>/crystals/<int:crystal_pk>/', views.WishlistCrystalAssoc.as_view(), name='wishlist_crystal_assoc'),
]