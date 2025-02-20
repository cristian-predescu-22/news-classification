import requests
from bs4 import BeautifulSoup
import re

url = "https://www.goodnewsnetwork.org/category/news/world/feed/"

response = requests.get(url)
rss_feed_content = response.text

soup = BeautifulSoup(rss_feed_content, "xml")
items = soup.find_all("item")

headlines = []

with open("good_news.txt", "w", encoding="utf-8") as file:
    for item in items:
        title = item.find("title").text
        headlines.append(title)  # Save the headline to the list
        description = re.sub("<[^<]+?>", "", item.find("description").text)
        pubDate = item.find("pubDate").text

        file.write(f"Headline: {title}\n")
        file.write(f"Description: {description}\n")
        file.write(f"Date: {pubDate}\n\n")
