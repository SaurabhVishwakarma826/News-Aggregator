from django.shortcuts import render, redirect
from home.models import HomeNews, SportsNews, BusinessNews, WorldNews, PoliticsNews, Contact
import scraping
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from joblib import dump, load
import joblib
from manage import process
from newsModelCode.predict import Model
import pandas as pd
from django.shortcuts import redirect

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
		'home_list': home_headline,
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
    message = ''
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message_text = request.POST['message']
        contact = Contact(name=name, email=email, subject=subject, message=message_text)
        contact.save()
        message = ' Thanks, for connecting with us!'
    return render(request, 'contact.html', {'message': message})


def fackSMS(request):
    df = pd.read_csv("./SMS_model/spam.csv", encoding="latin-1")
    df.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1, inplace=True)
    # Features and Labels
    df['label'] = df['v1'].map({'ham': 0, 'spam': 1})
    X = df['v2']
    y = df['label']

    # Extract Feature With CountVectorizer
    cv = CountVectorizer()
    X = cv.fit_transform(X)  # Fit the Data
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    from sklearn.naive_bayes import MultinomialNB

    clf = MultinomialNB()
    clf.fit(X_train, y_train)
    clf.score(X_test, y_test)

    is_fake = ''
    if request.method == 'POST' and 'user_input' in request.POST:
        message = request.POST['user_input']
        if not message.strip():
            is_fake = 'NULL'
        else:
            data = [message]
            vect = cv.transform(data).toarray()
            is_fake = clf.predict(vect)
            print(is_fake)
            is_fake=is_fake[0]
    return render(request, 'sms.html', {'fack':is_fake})
	
def fackMail(request):
	model = joblib.load('./Mails_model/spam_classifier.joblib')
	is_fake = ''
	if request.method == 'POST' and 'user_input' in request.POST:
		message=request.POST['user_input']
		if not message.strip():
			is_fake = 'NULL'
		else:
			message = [message]
			is_fake = model.predict(message)[0]
			print(is_fake)
	return render(request, 'mails.html', {'fack':is_fake})

def fackNews(request):
    is_fake = ''
    if request.method == 'POST' and 'user_input' in request.POST:
        message = request.POST['user_input']
        if not message.strip():
            is_fake = 'NULL'
        else:
            model = Model(message)
            is_fake = model.predict()[0]
            print(is_fake)
    return render(request, 'news.html', {'fack':is_fake})

