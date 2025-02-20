import requests
from bs4 import BeautifulSoup
import re
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import time


def remove_html_tags(text):
    return re.sub('<[^>]*>', '', text)


def sentiment_analysis(headline):
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(headline)['compound']

    if sentiment_score > 0.1:
        return "happy"
    elif sentiment_score < -0.1:
        return "sad"
    else:
        return "neutral"


def fetch_happy_headlines():
    url = 'https://www.goodnewsnetwork.org/category/news/feed/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'xml')

    items = soup.find_all('item')

    with open("happy_headlines.txt", "w", encoding="utf-8") as output_file:
        for item in items:
            title = item.title.text
            description = remove_html_tags(item.description.text)
            date = item.pubDate.text

            sentiment = sentiment_analysis(title)
            if sentiment == "happy":
                output_file.write(f"Title: {title}\n")
                output_file.write(f"Description: {description}\n")
                output_file.write(f"Date: {date}\n\n")

    print("Happy headlines written to happy_headlines.txt.")


while True:
    fetch_happy_headlines()
    time.sleep(1800)  # Sleep for 1800 seconds (30 minutes)