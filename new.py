import requests
from bs4 import BeautifulSoup

url = "https://www.goodnewsnetwork.org/category/news/world/feed/"
response = requests.get(url)
xml_data = response.content

soup = BeautifulSoup(xml_data, "xml")

items = soup.find_all("item")

def clean_description(description_html):
    soup = BeautifulSoup(description_html, "html.parser")
    paragraphs = soup.find_all("p")
    description_text = "\n".join(p.get_text(strip=True) for p in paragraphs if "The post" not in p.get_text())
    return description_text

with open("news_data.txt", "w", encoding="utf-8") as file:
    for item in items:
        title = item.find("title").text
        description = clean_description(item.find("description").text)
        pub_date = item.find("pubDate").text

        file.write(f"Title: {title}\n")
        file.write(f"Description: {description}\n")
        file.write(f"Date: {pub_date}\n")
        file.write("\n\n")

print("News data saved in news_data.txt")
