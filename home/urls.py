from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
  path("",views.index, name='home'),
  path("politics",views.politics,name='politics'),
  path("world",views.world,name='world'),
  path("sports",views.sports,name='sports'),
  path("business", views.businessnews, name='businessnews'),
  path("contact", views.contact, name='contact'),
  path("sms", views.fackSMS, name='sms'),
  path("mails",views.fackMail, name = 'mails'),
  path("news", views.fackNews, name = 'news')
]
