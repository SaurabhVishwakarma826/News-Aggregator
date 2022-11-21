from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
  path('scrap/', views.scrap, name="scrap"),
  path('sportnews/',views.sportnews, name="sportnews"),
  path("",views.index,name='home'),
  path("localnews",views.localnews,name='localnews'),
  path("currentnews",views.currentnews,name='currentnews'),
  path("sport",views.sport,name='sport'),
  path("businessnews", views.businessnews, name='businessnews')
  
]
