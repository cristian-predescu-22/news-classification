import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

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

    return headlines

if __name__ == "__main__":
    headlines = read_headlines("good_news.txt")
    
    for headline in headlines:
        sentiment = sentiment_analysis(headline)
        print(f"{headline}: {sentiment}")
