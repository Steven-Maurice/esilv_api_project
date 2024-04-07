from bs4 import BeautifulSoup
import codecs
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
from heapq import nlargest
import nltk

nltk.download("punkt")
nltk.download("stopwords")


def summarizer(text, n_sentences=3):
    """
    text: a str you want to summarize
    n_sentences: lenght of the summary

    return a summary of a text
    """

    sentences = sent_tokenize(text)
    if len(sentences) < n_sentences:
        return text

    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text.lower())
    frequency = defaultdict(int)
    for word in words:
        if word not in stop_words and word.isalpha():
            frequency[word] += 1

    sentence_scores = defaultdict(int)
    for sentence in sentences:
        sentence_words = word_tokenize(sentence.lower())
        for word in sentence_words:
            if word in frequency:
                sentence_scores[sentence] += frequency[word]

    summary_sentences = nlargest(n_sentences, sentence_scores, key=sentence_scores.get)
    summary = " ".join(summary_sentences)
    return summary


def extract_and_summarize(filepath):
    """
    extract the text of an html file

    filepath: path of the html file

    return the summary
    """

    with codecs.open(filepath, "r", "utf-8") as file:
        soup = BeautifulSoup(file.read(), "html.parser")
        paragraphs = soup.find_all("p")
        text = " ".join([p.get_text() for p in paragraphs])
        return summarizer(text)
