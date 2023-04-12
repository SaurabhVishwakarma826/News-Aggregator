from django.urls import path
from .views import HomeNewsList, SportNewsList, BusinessNewsList, WorldNewsList, PoliticsNewsList, ContactList, DetailHomeNewsList
from .views import DetailSportNewsList, DetailBusinessNewsList,DetailWorldNewsList,DetailPoliticsNewsList, DetailContactList


urlpatterns = [
    path('home',HomeNewsList.as_view()),
    path('<int:pk>/', DetailHomeNewsList.as_view()),
    path('sport',SportNewsList.as_view()),
    path('<int:pk>/',DetailSportNewsList.as_view()),
    path('business',BusinessNewsList.as_view()),
    path('<int:pk>/',DetailBusinessNewsList.as_view()),
    path('world',WorldNewsList.as_view()),
    path('<int:pk>/',DetailWorldNewsList.as_view()),
    path('politics',PoliticsNewsList.as_view()),
    path('<int:pk>/',DetailPoliticsNewsList.as_view()),
    path('contact',ContactList.as_view()),
    path('<int:pk>/',DetailContactList.as_view())
]
