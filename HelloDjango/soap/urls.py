from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('all/', views.AllProd.as_view(), name='all'),
    path('all/<slug>/', views.AllProd_aroma.as_view(), name='all_aroma'),
    path('type/<slug>/', views.Type_slug.as_view(), name='type_slug'),
    path('type/<slug>/<slug_aroma>/', views.Type_aroma_slug.as_view(), name='type_aroma_slug'),
    path('prod/<slug>/', views.Prod.as_view(), name='prod'),
    path('about/', views.About.as_view() , name='about'),
    path('dostavka/', views.Dostavka.as_view() , name='dostavka')
]
