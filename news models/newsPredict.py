import re
import nltk
import pickle
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

loaded_model = pickle.load(open('./model.pkl', 'rb'))
loaded_tfidf = pickle.load(open('./tfidf.pkl','rb'))
lemmatizer = WordNetLemmatizer()
stpwrds = list(stopwords.words('english'))

def fake_news_det(news):
    review = news
    review = re.sub(r'[^a-zA-Z\s]', '', review)
    review = review.lower()
    review = nltk.word_tokenize(review)
    corpus=[]
    for y in review :
        if y not in stpwrds :
            corpus.append(lemmatizer.lemmatize(y))
    input_data = [' '.join(corpus)]
    vectorized_input_data = loaded_tfidf.transform(input_data)
    prediction = loaded_model.predict(vectorized_input_data)
    return prediction


if __name__ == '__main__':
    n = 'CricketNext Poll: Pick Your Strongest Team India Playing XI for the 1st T20I Against New Zealand'
    prediction=fake_news_det(n)
    if prediction[0] == 0:
        print("Prediction of the News :  Looking Fake⚠ News������ ")
    else:
        print("Prediction of the News : Looking Real News������ ")
