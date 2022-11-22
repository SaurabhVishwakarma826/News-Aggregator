from django.shortcuts import render, HttpResponse
import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as BSoup
from home.models import HomeNews, SportsNews, BusinessNews, WorldNews, PoliticsNews

def index(request):
    home_headline = HomeNews.objects.all()[::-1]
    context = {
        'home_list':home_headline
    }
    return render(request, 'index.html',context)

def politics(request):
	politics_headline = PoliticsNews.objects.all()[::-1]
	context = {
		'politics_list' : politics_headline
	}
	return render(request, 'politics.html', context)

def world(request):
	world_headline = WorldNews.objects.all()[::-1]
	context = {
		'world_list':world_headline
	}
	return render(request, 'world.html',context)

def sport(request):
    sport_headline = SportsNews.objects.all()[::-1]
    context = {
        'sport_list':sport_headline
    }
    return render(request, 'sport.html',context)

def businessnews(request):
	business_headline = BusinessNews.objects.all()[::-1]
	context = {
		'business_list' : business_headline
	}
	return render(request, 'businessnews.html', context)


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

def scrapbusiness(request):
	session = requests.Session()
	session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
	url = "https://zeenews.india.com/business"
	content = session.get(url, verify=False).content
	soup = BSoup(content, "html.parser")
	news = soup.find('div',{"class":"more-news-section"})
	News = news.find_all('div', {"class":"row no-gutters morenews-block"})
	for artcile in News:
		link = artcile.find('div',{"class":"col-lg-3 col-12 pl-0"}).find('a')['href']
		link = 'https://zeenews.india.com'+link
		image_src = artcile.find('div',{"class":"col-lg-3 col-12 pl-0"}).find('img')['src']
		title = artcile.find('div',{"class":"col-md-9 pl-4"}).find('div',{"class":"news_description desc-title morenews-title"}).text
		new_business = BusinessNews()
		new_business.business_title = title
		new_business.business_image = image_src
		new_business.business_url = link
		new_business.save()
	return redirect("../")

def scrapworld(request):
	session = requests.Session()
	session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
	url = "https://www.news18.com/world/"
	content = session.get(url, verify=False).content
	soup = BSoup(content, "html.parser")
	News = soup.find_all('div', {"class":"jsx-3328680553 blog_list_row"})
	for artcile in News:
		link = artcile.find('a')['href']
		image_src = artcile.find("div",{"class":"jsx-3328680553 blog_img"}).find('img')['data-src']
		title = artcile.h4.text
		new_world = WorldNews()
		new_world.world_title = title
		new_world.world_image = image_src
		new_world.world_url = link
		new_world.save()
	return redirect("../")

def scrappolitics(request):
	session = requests.Session()
	session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
	url = "https://www.news18.com/politics/"
	content = session.get(url, verify=False).content
	soup = BSoup(content, "html.parser")
	News = soup.find_all('div', {"class":"jsx-3328680553 blog_list_row"})
	for artcile in News:
		link = artcile.find('a')['href']
		image_src = artcile.find("div",{"class":"jsx-3328680553 blog_img"}).find('img')['data-src']
		title = artcile.h4.text
		new_politics = PoliticsNews()
		new_politics.politics_title = title
		new_politics.politics_image = image_src
		new_politics.politics_url = link
		new_politics.save()
	return redirect("../")