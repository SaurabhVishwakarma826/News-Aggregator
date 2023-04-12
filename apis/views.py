from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from home import models
from .serializers import HomeNewsSerializer, SportNewsSerializer, BusinessNewsSerializer, WorldNewsSerializer, PoliticsNewsSerializer,ContactSerializer

class HomeNewsList(generics.ListCreateAPIView):
    queryset = models.HomeNews.objects.all()
    serializer_class = HomeNewsSerializer

class SportNewsList(generics.ListCreateAPIView):
    queryset = models.SportsNews.objects.all()
    serializer_class = SportNewsSerializer

class BusinessNewsList(generics.ListCreateAPIView):
    queryset = models.BusinessNews.objects.all()
    serializer_class = BusinessNewsSerializer

class WorldNewsList(generics.ListCreateAPIView):
    queryset = models.WorldNews.objects.all()
    serializer_class = WorldNewsSerializer

class PoliticsNewsList(generics.ListCreateAPIView):
    queryset = models.PoliticsNews.objects.all()
    serializer_class = PoliticsNewsSerializer

class ContactList(generics.ListCreateAPIView):
    queryset = models.Contact.objects.all()
    serializer_class = ContactSerializer

class DetailHomeNewsList(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.HomeNews.objects.all()
    serializer_class = HomeNewsSerializer

class DetailSportNewsList(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.SportsNews.objects.all()
    serializer_class = SportNewsSerializer

class DetailBusinessNewsList(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.BusinessNews.objects.all()
    serializer_class = BusinessNewsSerializer

class DetailWorldNewsList(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.WorldNews.objects.all()
    serializer_class = WorldNewsSerializer

class DetailPoliticsNewsList(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.PoliticsNews.objects.all()
    serializer_class = PoliticsNewsSerializer

class DetailContactList(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Contact.objects.all()
    serializer_class = ContactSerializer