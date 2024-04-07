import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except LookupError:
    nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    """
    Analyzes the sentiment of the provided text.

    :param text: The text to analyze sentiment of.
    :return: A dictionary containing the sentiment scores.
    """
    if not text:
        return {"neg": 0, "neu": 0, "pos": 0, "compound": 0}
    
    return sia.polarity_scores(text)
