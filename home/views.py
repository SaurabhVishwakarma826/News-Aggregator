from django.shortcuts import render, HttpResponse
import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as BSoup
from home.models import HomeNews, SportsNews

def index(request):
    home_headline = HomeNews.objects.all()[::-1]
    context = {
        'home_list':home_headline
    }
    return render(request, 'index.html',context)

def localnews(request):
    return render(request, 'localnews.html')

def currentnews(request):
    return render(request, 'currentnews.html')

def sport(request):
    sport_headline = SportsNews.objects.all()[::-1]
    context = {
        'sport_list':sport_headline
    }
    return render(request, 'sport.html',context)

def businessnews(request):
    return render(request, 'businessnews.html')


def scrap(request):
	session = requests.Session()
	session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
	url = "https://www.news18.com/india/"
	content = session.get(url, verify=False).content
	soup = BSoup(content, "html.parser")
	News = soup.find_all('div', {"class":"jsx-3328680553 blog_list_row"})
	for artcile in News:
		link = artcile.find('a')['href']
		image_src = artcile.find("div",{"class":"jsx-3328680553 blog_img"}).find('img')['data-src']
		title = artcile.h4.text
		new_home = HomeNews()
		new_home.home_title = title
		new_home.home_url = link
		new_home.home_image = image_src
		new_home.save()
	return redirect("../")


def sportnews(request):
	session = requests.Session()
	session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
	url = "https://zeenews.india.com/cricket/t20-world-cup"
	content = session.get(url, verify=False).content
	soup = BSoup(content, "html.parser")
	News = soup.find_all('div', {"class":"news_item"})
	for artcile in News:
		link = artcile.find('div',{"class":"news_left"}).find('div',{"class":"news_title"}).find('a')['href']
		link = 'https://zeenews.india.com'+link
		image_src = artcile.find('div',{"class":"news_right"}).find('img')['src']
		title = artcile.find('div',{"class":"news_left"}).find('div',{"class":"news_title"}).text
		new_sport = SportsNews()
		new_sport.sports_title = title
		new_sport.sports_url = link
		new_sport.sports_image = image_src
		new_sport.save()
	return redirect("../")