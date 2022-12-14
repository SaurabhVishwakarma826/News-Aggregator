from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
  path('scrap/', views.scrap, name="scrap"),
  path('sportnews/',views.sportnews, name="sportnews"),
  path('scrapbusiness/',views.scrapbusiness,name='scrapbusiness'),
  path('scrapworld/',views.scrapworld,name='scrapworld'),
  path('scrappolitics/',views.scrappolitics,name='scrappolitics'),
  path("",views.index,name='home'),
  path("politics",views.politics,name='politics'),
  path("world",views.world,name='world'),
  path("sport",views.sport,name='sport'),
  path("businessnews", views.businessnews, name='businessnews')
  
]
