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

if __name__ == "__main__":
    headlines = [
        "Stock market reaches all-time high",
        "Natural disaster causes widespread destruction",
        "Local sports team wins championship",
        "Unemployment rate rises significantly"
    ]

    for headline in headlines:
        sentiment = sentiment_analysis(headline)
        print(f"{headline}: {sentiment}")
