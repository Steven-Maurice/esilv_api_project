# Import libraries
import pandas as pd
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

import re
import string
from spacy.lang.fr.stop_words import STOP_WORDS

from textblob import Blobber
from textblob_fr import PatternTagger, PatternAnalyzer

from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt

from scrape_info import scrape_article_For_ML,findUrlHref


def scrape_all_articles(base_url):
    all_urls = findUrlHref(base_url)
    all_data = []
    
    for url in all_urls:
        print(url)
        data = scrape_article_For_ML(url)
        all_data.append(data)
    
    return all_data

base_blog_url = "https://blog-ia.com"
all_articles_data = scrape_all_articles(base_blog_url)
print(all_articles_data[0])
df = pd.DataFrame(all_articles_data)
