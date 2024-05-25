import requests
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('stopwords')

def fetch_trends():
    url = 'https://www.vogue.com/fashion/trends'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('h2')

    trends = []
    for article in articles:
        text = article.get_text()
        tokens = word_tokenize(text)
        words = [word for word in tokens if word.isalnum()]
        filtered_words = [word for word in words if word not in stopwords.words('english')]
        trends.extend(filtered_words)

    return trends
