import re
import nltk
from pickle import load
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

loaded_model = load(open('./newsModel/model.pkl', 'rb'))
loaded_tfidf = load(open('./newsModel/tfidf.pkl','rb'))
lemmatizer = WordNetLemmatizer()
stpwrds = list(stopwords.words('english'))

class Model:
  def __init__(self, news):
    self.news = news
  def predict(self):
      review = self.news
      review = re.sub(r'[^a-zA-Z\s]', '', review)
      review = review.lower()
      review = nltk.word_tokenize(review)
      corpus = []
      for y in review:
          if y not in stpwrds:
              corpus.append(lemmatizer.lemmatize(y))
      input_data = [' '.join(corpus)]
      vectorized_input_data = loaded_tfidf.transform(input_data)
      prediction = loaded_model.predict(vectorized_input_data)
      return prediction