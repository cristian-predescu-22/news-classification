import feedparser
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.classify import NaiveBayesClassifier
import csv

nltk.download('punkt')
nltk.download('stopwords')

# Training dataset
training_data = []
with open("train.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        training_data.append((row["Title"], row["Description"]))

# Preprocessing function
def preprocess(sentence):
    words = word_tokenize(sentence)
    words = [word.lower() for word in words if word.isalpha()]
    words = [word for word in words if word not in stopwords.words("english")]
    return {word: True for word in words}

# Train the Naive Bayes classifier
training_data_preprocessed = [(preprocess(sentence), sentiment) for (sentence, sentiment) in training_data]
classifier = NaiveBayesClassifier.train(training_data_preprocessed)

# BBC news feed
bbc_feed = "https://www.goodnewsnetwork.org/category/news/world/feed/"
feed = feedparser.parse(bbc_feed)

# Classify and print news headlines
for entry in feed.entries:
    headline = entry.title
    sentiment = classifier.classify(preprocess(headline))
    print(f"{headline} -> {sentiment}")
