import requests
import feedparser
import html2text
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def extract_news(url):
    feed = feedparser.parse(url)
    h = html2text.HTML2Text()
    h.ignore_links = True
    h.ignore_images = True

    with open("good_news.txt", "w", encoding="utf-8") as file:
        for entry in feed.entries:
            headline = entry.title
            description_html = entry.description
            description = h.handle(description_html).strip()
            date = entry.published
            file.write(f"Headline: {headline}\n")
            file.write(f"Description: {description}\n")
            file.write(f"Date: {date}\n\n")

def sentiment_analysis(headline):
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(headline)['compound']

    if sentiment_score > 0.1:
        return "happy"
    elif sentiment_score < -0.1:
        return "sad"
    else:
        return "neutral"

def read_headlines(filename):
    with open(filename, "r", encoding="utf-8") as file:
        content = file.readlines()

    headlines = []
    for line in content:
        if line.startswith("Headline:"):
            headlines.append(line[len("Headline:"):].strip())

    return headlines, content

if __name__ == "__main__":
    url = "https://www.goodnewsnetwork.org/category/news/world/feed/"
    extract_news(url)

    headlines, content = read_headlines("good_news.txt")

    with open("happy_news.txt", "w", encoding="utf-8") as happy_file:
        for headline in headlines:
            sentiment = sentiment_analysis(headline)
            if sentiment == "happy":
                index = headlines.index(headline)
                happy_file.write(f"Headline: {headline}\n")
                happy_file.write(f"Description: {content[index * 4 + 1].strip()}\n")
                happy_file.write(f"Date: {content[index * 4 + 2].strip()}\n\n")
