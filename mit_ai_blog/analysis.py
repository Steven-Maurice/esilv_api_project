from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#Script to perform sentiment analysis
# - Polarity: refers to the emotional intensity or sentiment expressed in text ;
# - Subjectivity: refers to the degree to which a statement is opinionated or expresses personal feelings.
def analyze_sentiment(articles, article_texts):
    model = Pipeline([
        ('vectorizer', CountVectorizer()),
        ('svm', SVC(kernel='linear'))
    ])
    train_data = [
        ("Positive article", "positive"),
        ("Negative article", "negative")
    ]
    model.fit([data[0] for data in train_data], [data[1] for data in train_data])
    predictions = model.predict(article_texts)
    sentiments = [TextBlob(text).sentiment for text in article_texts]
    polarities = [sentiment.polarity for sentiment in sentiments]
    subjectivities = [sentiment.subjectivity for sentiment in sentiments]
    sentiments_vader = SentimentIntensityAnalyzer()
    polarities_vader = [sentiments_vader.polarity_scores(text) for text in article_texts]
    results = [{"Article": (i+1), "title": articles[i]['title'], "sentiment": predictions[i], "polarity": polarities[i], "subjectivity": subjectivities[i], "Polarity analysis": polarities_vader[i]} for i in range(len(articles))]
    return results
