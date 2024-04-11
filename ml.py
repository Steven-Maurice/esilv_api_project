import requests
from textblob import TextBlob
from bs4 import BeautifulSoup
from transformers import BartTokenizer, BartForConditionalGeneration

def analyze_sentiment(text):
    analysis = TextBlob(text)
    sentiment = analysis.sentiment.polarity  # -1 to 1 where 1 is positive
    return sentiment


def summarize_article(article_url):
    # Ensure that the transformers model and tokenizer are loaded only once
    # at the start of the application, not every time the function is called
    # For simplicity, we're loading it each time here, but this is not efficient
    tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
    model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')

    response = requests.get(article_url)
    if response.status_code == 200:
        content = response.content
        soup = BeautifulSoup(content, 'html.parser')
        text = soup.get_text()
        inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=1024, truncation=True)
        summary_ids = model.generate(inputs, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary
    else:
        print('Unable to retrieve the article.')
        return None