
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



# on va nettoyer le titre et le content
def clean_text(text):
    text = re.sub(r'#','',text) # remove symbol
    text = re.sub(r'https?:\/\/\S+' , '' , text) #Remove hyperlink
    text = text.replace("  " , " ") #Remove space
    text = ''.join(x for x in text if not x.isdigit()) # Remove numbers
    text =  re.sub(r'[.,"\-?:!;()]', ' ', text) # Remove punctuation without single quotes
    text =  re.sub(r'[\']', ' ', text) # Remove punctuation
    #text = ''.join(ch for ch in text if ch not in exclude) # Remove punctuation
    text = text.lower() # lower text
    return text

def scrape_all_articles(base_url):
        all_urls = findUrlHref(base_url)
        all_data = []
        
        for url in all_urls:
            data = scrape_article_For_ML(url)
            # Appliquer la fonction clean_text à chaque élément du tuple
            cleaned_data = tuple(clean_text(item) for item in data)
            all_data.append(cleaned_data)
            all_data.append(data)
        
        return all_data

def graph(base_blog_url):


    all_articles_data = scrape_all_articles(base_blog_url)
    all_articles_data_tokenizer=[]
    for data_tuple in all_articles_data:
        word_tokenizer = []
        for item in data_tuple:
            if isinstance(item, str):  
                for word in re.sub("\W", " ", item).split():
                    cleaned_word = clean_text(word)  # on applique la fonction clean_text à chaque mot
                    word_tokenizer.append(cleaned_word)
        all_articles_data_tokenizer.append(word_tokenizer)

    # Remove stop words and unselect specific stop words from the list
    stop_words=set(STOP_WORDS)

    deselect_stop_words = ['n\'', 'ne','plus','personne','aucun','ni','aucune','rien']
    for w in deselect_stop_words:
        if w in stop_words:
            stop_words.remove(w)
        else:
            continue

    # Remove STOP_WORDS
    all_articles_data_tokenizer_filtred=[]
    for comment in all_articles_data_tokenizer:
        filteredComment = [w for w in comment if not ((w in stop_words) or (len(w) == 1))]
        all_articles_data_tokenizer_filtred.append(' '.join(filteredComment))



    tb = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
    # Sentiment score
    sentiment_score_polarity = []
    sentiment_mapping = []
    for text in all_articles_data_tokenizer_filtred:
        vs = tb(text).sentiment[0]
        sentiment_score_polarity.append(vs)
        if (vs > 0):
            sentiment_mapping.append('Positive')
        elif (vs < 0):
            sentiment_mapping.append('Negative')
        else:
            sentiment_mapping.append('Neutral')   

    # on trace la repartition
    sentiment_df = pd.DataFrame({'Sentiment': sentiment_mapping})

    palette_colors = {"Neutral": "blue", "Positive": "green", "Negative": "red"}
    plt.figure(figsize=(8, 6))
    sns.countplot(x='Sentiment', data=sentiment_df, palette=palette_colors)
    plt.title('Histogramme du Mapping de Sentiment')
    plt.xlabel('Sentiment')
    plt.ylabel('Nombre d articles')
    # Enregistrement du graphique en tant que fichier PNG
    plt.savefig('sentiment_plot.png', bbox_inches='tight')  # bbox_inches='tight' pour s'assurer que rien ne soit coupé

    return 'sentiment_plot.png'

