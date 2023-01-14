import joblib
import re
import string
import pandas as pd

model = joblib.load('./newsModel/model.pkl')
def wordpre(text):
    text = text.lower()
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub("\\W"," ",text) # remove special chars
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub(r'\w*\d\w*', '', text)
    return text

class Model:
  def __init__(self, news):
    self.news = news
  def predict(self):
      news = self.news
      newsword = wordpre(news)
      Snwes = pd.Series(newsword)
      result = model.predict(Snwes)
      return result
