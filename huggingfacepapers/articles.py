from tqdm import tqdm
import datetime
import requests
from bs4 import BeautifulSoup
from pandas import date_range
import re
from huggingfacepapers.article import Article

from sentence_transformers import SentenceTransformer, util
from sklearn.decomposition import PCA

import plotly_express as px 

class Articles:
    def __init__(self):
        self.articles = {}

        print("Loading SentenceTransformer model")
        self.sentenceTransformerModel = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
        print("Model loaded")

    def loadArticles(self, start=None, end=None):
        if start is None:
            start = datetime.date.today()
        if end is None:
            end = datetime.date.today()
        for date in date_range(start=start, end=end, freq="D"):
            print(f"Fetching highlighted papers for date : {date}")
            response = requests.get(f"https://huggingface.co/papers?date={date}")
            if response.status_code != 200:
                raise Exception("Request error")
            articles = self.parseArticles(response)
            for article in articles:
                if article.id in self.articles:
                    continue
                self.articles[article.id] = article
        return

    def parseArticles(self, response):
        soup = BeautifulSoup(response.text, "html.parser")
        articles_els = soup.find_all("article")
        articles = []
        for article_el in articles_els:
            rounded_els = article_el.select(".rounded-xl")
            article = Article(
                title=article_el.find("h3").text,
                media=(rounded_els[0].find("img") or article_el.find("video")).attrs["src"],
                upvotes=int(rounded_els[1].text.strip()),
                n_authors=int(re.findall(r"[0-9]+", article_el.find("ul").text)[0]),
                id=article_el.select_one("h3 a").attrs["href"].split("/")[-1],
            )
            articles.append(article)
        return articles

    def preview(self):
        preview = []
        for article in self.articles.values():
            preview.append(article.preview())
        return preview

    def details(self):
        details = []
        for article in self.articles.values():
            details.append(article.detail())
        return details

    def get_by_id(self, id):
        if id in self.articles:
            return self.articles[id]
        else:
            article = Article(id)
            article.load()
            self.articles[id] = article
            return article

    def compute_embeddings(self):
        for article in tqdm(self.articles.values()):
            article.compute_embedding(self.sentenceTransformerModel)

    def get_by_query(self, query):
        queryEmbedding = self.sentenceTransformerModel.encode(query)
        results = []
        for article in self.articles.values():
            if article.embedding is None:
                article.compute_embedding(self.sentenceTransformerModel)
            results.append(
                {
                    "article": article.detail(),
                    "score": util.cos_sim(queryEmbedding, article.embedding).tolist()[0][0],
                }
            )
        return sorted(results, key=lambda result: result["score"], reverse=True)

    def viz(self): 
        X = []
        for article in self.articles.values():
            if article.embedding is None: 
                article.compute_embedding(self.sentenceTransformerModel)
            X.append(article.embedding)
    
        pca = PCA(n_components=2)
        X_2d = pca.fit_transform(X)
        fig = px.scatter(x=[pos[0] for pos in X_2d], y=[pos[1] for pos in X_2d],text=[article.title for article in self.articles.values()], size_max=30, width=1500, height=1500)
        fig.update_traces(textposition='top center')
        return fig.to_image()