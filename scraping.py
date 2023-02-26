


import requests
from home.models import HomeNews, SportsNews, BusinessNews, WorldNews, PoliticsNews
from newsModelCode.predict import Model
from bs4 import BeautifulSoup as BSoup

def home():
    try:
        HomeNews.objects.all().delete()
        session = requests.Session()
        session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
        url = "https://www.news18.com/india/"
        content = session.get(url, verify=False).content
        soup = BSoup(content, "html.parser")
        News = soup.find_all('div', {"class": "jsx-3621759782 blog_list_row"})
        for artcile in News:
            link = artcile.find('a')['href']
            image_src = artcile.find("div", {"class": "jsx-3621759782 blog_img"}).find('img')['data-src']
            title = artcile.h4.text
            new_home = HomeNews()
            model = Model(title)
            if model.predict()[0] == 1:
                new_home.home_title = title
                new_home.home_url = link
                new_home.home_image = image_src
                new_home.save()
        url = "https://news.abplive.com/trending"
        content = session.get(url, verify=False).content
        soup = BSoup(content, "html.parser")
        al = soup.find_all('div', {'class': 'other_news'})
        for allnews in al:
            link = allnews.find('a')['href']
            title = allnews.find('a').text
            image_src = allnews.find('img')['data-src']
            new_home = HomeNews()
            model = Model(title)
            if model.predict()[0] == 1:
                new_home.home_title = title
                new_home.home_url = link
                new_home.home_image = image_src
                new_home.save()
    except Exception as e:
        print(e)

def politics():
    try:
        PoliticsNews.objects.all().delete()
        session = requests.Session()
        session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
        url = "https://www.news18.com/politics/"
        content = session.get(url, verify=False).content
        soup = BSoup(content, "html.parser")
        News = soup.find_all('div', {"class": "jsx-3621759782 blog_list_row"})
        for artcile in News:
            link = artcile.find('a')['href']
            image_src = artcile.find("div", {"class": "jsx-3621759782 blog_img"}).find('img')['data-src']
            title = artcile.h4.text
            new_politics = PoliticsNews()
            model = Model(title)
            if model.predict()[0] == 1:
                new_politics.politics_title = title
                new_politics.politics_image = image_src
                new_politics.politics_url = link
                new_politics.save()
        url = "https://economictimes.indiatimes.com/news/politics"
        content = session.get(url, verify=False).content
        soup = BSoup(content, "html.parser")
        al = soup.find_all('div', {'class': 'botplData flt'})
        for allnews in al:
            title = allnews.find('h3').text
            link = 'https://economictimes.indiatimes.com/news/politics'
            link += allnews.find('h3').find('a')['href']
            image_src = allnews.find('img')['data-original']
            new_politics = PoliticsNews()
            model = Model(title)
            if model.predict()[0] == 1:
                new_politics.politics_title = title
                new_politics.politics_image = image_src
                new_politics.politics_url = link
                new_politics.save()
        url = "https://www.indiatoday.in/politics"
        content = session.get(url, verify=False).content
        soup = BSoup(content, "html.parser")
        al = soup.find_all('article', {'class': 'B1S3_story__card__A_fhi B1S3_Bcard__L7ikx Bcard'})
        for allnews in al:
            title = allnews.find('h2').text
            link = url + allnews.find('a')['href']
            image_src = allnews.find('img')['src']
            new_politics = PoliticsNews()
            model = Model(title)
            if model.predict()[0] == 1:
                new_politics.politics_title = title
                new_politics.politics_image = image_src
                new_politics.politics_url = link
                new_politics.save()
    except Exception as e:
        print(e)

def world():
    try:
        WorldNews.objects.all().delete()
        session = requests.Session()
        session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
        url = "https://www.news18.com/world/"
        content = session.get(url, verify=False).content
        soup = BSoup(content, "html.parser")
        News = soup.find_all('div', {"class": "jsx-3621759782 blog_list_row"})
        for artcile in News:
            link = artcile.find('a')['href']
            image_src = artcile.find("div", {"class": "jsx-3621759782 blog_img"}).find('img')['data-src']
            title = artcile.h4.text
            new_world = WorldNews()
            model = Model(title)
            if model.predict()[0] == 1:
                new_world.world_title = title
                new_world.world_image = image_src
                new_world.world_url = link
                new_world.save()
        session = requests.Session()
        session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
        url = "https://economictimes.indiatimes.com/news/international/world-news"
        content = session.get(url, verify=False).content
        soup = BSoup(content, "html.parser")
        al = soup.find_all('div', {'class': 'eachStory'})
        for allnews in al:
            link = url + allnews.find('a')['href']
            title = allnews.find('h3').text
            image_src = allnews.find('img')['data-original']
            new_world = WorldNews()
            model = Model(title)
            if model.predict()[0] == 1:
                new_world.world_title = title
                new_world.world_image = image_src
                new_world.world_url = link
                new_world.save()
        url = "https://www.hindustantimes.com/world-news"
        content = session.get(url, verify=False).content
        soup = BSoup(content, "html.parser")
        al = soup.find_all('div', {'class': 'cartHolder listView track timeAgo'})
        for allnews in al:
            link = url + allnews.find('a')['href']
            title = allnews.find('h3').text
            image_src = allnews.find('img')['data-src']
            new_world = WorldNews()
            model = Model(title)
            if model.predict()[0] == 1:
                new_world.world_title = title
                new_world.world_image = image_src
                new_world.world_url = link
                new_world.save()
    except Exception as e:
        print(e)

def sport():
    try:
        SportsNews.objects.all().delete()
        session = requests.Session()
        session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
        url = "https://zeenews.india.com/cricket/t20-world-cup"
        content = session.get(url, verify=False).content
        soup = BSoup(content, "html.parser")
        News = soup.find_all('div', {"class": "news_item"})
        for artcile in News:
            link = artcile.find('div', {"class": "news_left"}).find('div', {"class": "news_title"}).find('a')['href']
            link = 'https://zeenews.india.com' + link
            image_src = artcile.find('div', {"class": "news_right"}).find('img')['src']
            title = artcile.find('div', {"class": "news_left"}).find('div', {"class": "news_title"}).text
            new_sport = SportsNews()
            model = Model(title)
            if model.predict()[0] == 1:
                new_sport.sports_title = title
                new_sport.sports_url = link
                new_sport.sports_image = image_src
                new_sport.save()
        url = "https://www.hindustantimes.com/sports"
        content = session.get(url, verify=False).content
        soup = BSoup(content, "html.parser")
        al = soup.find_all('div', {'class': 'cartHolder listView track timeAgo'})
        for allnews in al:
            link = 'https://www.hindustantimes.com' + allnews.find('h3').find('a')['href']
            title = allnews.find('h3').text
            image_src = allnews.find('img')['data-src']
            new_sport = SportsNews()
            model = Model(title)
            if model.predict()[0] == 1:
                new_sport.sports_title = title
                new_sport.sports_url = link
                new_sport.sports_image = image_src
                new_sport.save()
        url = "https://zeenews.india.com/sports"
        content = session.get(url, verify=False).content
        soup = BSoup(content, "html.parser")
        al = soup.find_all('div', {'class': 'row no-gutters morenews-block'})
        for allnews in al:
            link = 'https://zeenews.india.com'+allnews.find('div', {'class': 'section-tumbnail-top-post d-flex'}).find('a')['href']
            title = allnews.find('div', {'class': 'news_description desc-title morenews-title'}).find('a').text
            image_src = allnews.find('div', {'class': 'section-tumbnail-top-post d-flex'}).find('img')['item-src']
            new_sport = SportsNews()
            model = Model(title)
            if model.predict()[0] == 1:
                new_sport.sports_title = title
                new_sport.sports_url = link
                new_sport.sports_image = image_src
                new_sport.save()
    except Exception as e:
        print(e)

def business():
    try:
        BusinessNews.objects.all().delete()
        session = requests.Session()
        session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
        url = "https://zeenews.india.com/business"
        content = session.get(url, verify=False).content
        soup = BSoup(content, "html.parser")
        news = soup.find('div', {"class": "more-news-section"})
        News = news.find_all('div', {"class": "row no-gutters morenews-block"})
        for artcile in News:
            link = artcile.find('div', {"class": "col-lg-3 col-12 pl-0"}).find('a')['href']
            link = 'https://zeenews.india.com' + link
            image_src = artcile.find('div', {"class": "col-lg-3 col-12 pl-0"}).find('img')['src']
            title = artcile.find('div', {"class": "col-md-9 pl-4"}).find('div', {"class": "news_description desc-title morenews-title"}).text
            new_business = BusinessNews()
            model = Model(title)
            if model.predict()[0] == 1:
                new_business.business_title = title
                new_business.business_image = image_src
                new_business.business_url = link
                new_business.save()
        session = requests.Session()
        session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
        url = "https://www.news18.com/business/"
        content = session.get(url, verify=False).content
        soup = BSoup(content, "html.parser")
        al = soup.find_all('div', {'class': 'jsx-3621759782 blog_list_row'})
        for allnews in al:
            link = allnews.find('a')['href']
            title = allnews.find('h4').text
            image_src = allnews.find('img')['data-src']
            new_business = BusinessNews()
            model = Model(title)
            if model.predict()[0] == 1:
                new_business.business_title = title
                new_business.business_image = image_src
                new_business.business_url = link
                new_business.save()
        url = "https://news.abplive.com/business"
        content = session.get(url, verify=False).content
        soup = BSoup(content, "html.parser")
        al = soup.find_all('div', {'class': 'other_news'})
        for allnews in al:
            link = allnews.find('a')['href']
            title = allnews.find('a').text
            image_src = allnews.find('img')['data-src']
            new_business = BusinessNews()
            model = Model(title)
            if model.predict()[0] == 1:
                new_business.business_title = title
                new_business.business_image = image_src
                new_business.business_url = link
                new_business.save()
    except Exception as e:
        print(e)

