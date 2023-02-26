
from django.shortcuts import render, redirect
# from bs4 import BeautifulSoup as BSoup
from home.models import HomeNews, SportsNews, BusinessNews, WorldNews, PoliticsNews
# from newsModelCode.predict import Model
import scraping

def index(request):
	scraping.home()
	home_headline = HomeNews.objects.all().order_by('?')[:6]
	politics_headline = PoliticsNews.objects.all().order_by('?')[:4]
	world_headline = WorldNews.objects.all().order_by('?')[:4]
	sport_headline = SportsNews.objects.all().order_by('?')[:4]
	business_headline = BusinessNews.objects.all().order_by('?')[:4]

	home_2 = HomeNews.objects.all().order_by('?')[6:8]       # popular news
	home_3 = HomeNews.objects.all().order_by('?')[8:10]      # populer news
	home_4 = HomeNews.objects.all().order_by('?')[10:15]     # latest news
	home_5 = WorldNews.objects.all().order_by('?')[4:9]      # latest news
	home_6 = HomeNews.objects.all().order_by('?')[4:10]      # trending news

	context = {
		'home_list':home_headline,
		'politics_list': politics_headline,
		'world_list' : world_headline,
		'business_list' : business_headline,
		'sport_list' : sport_headline,
		'home_2': home_2,
		'home_3': home_3,
		'home_4': home_4,
		'home_5': home_5,
		'home_6': home_6,
	}
	return render(request, 'index.html',context)

def politics(request):
	scraping.politics()
	politics_headline = PoliticsNews.objects.all().order_by('?')[::-1]
	context = {
		'politics_list' : politics_headline
		}
	return render(request, 'politics.html', context)

def world(request):
	scraping.world()
	world_headline = WorldNews.objects.all().order_by('?')[::-1]
	context = {
		'world_list':world_headline
		}
	return render(request, 'world.html',context)


def sports(request):
	scraping.sport()
	sport_headline = SportsNews.objects.all().order_by('?')[::-1]
	context = {
		'sport_list':sport_headline
		}
	return render(request, 'sports.html',context)

def businessnews(request):
	scraping.business()
	business_headline = BusinessNews.objects.all().order_by('?')[::-1]
	context = {
		'business_list' : business_headline
		}
	return render(request, 'business.html', context)

def contact(request):
	return render(request, 'contact.html')

