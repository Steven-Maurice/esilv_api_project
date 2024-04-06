from tqdm import tqdm
import datetime
import requests
from bs4 import BeautifulSoup
from pandas import date_range
import re
from huggingfacepapers.article import Article


class Articles:
    def _init_(self):
        self.articles = {}

    def loadArticles(self, start=None,   end=None):
        if start is None:
            start = datetime.date.today()
        if end is None:
            end = datetime.date.today()
        for date in date_range(start=start, end=end, freq="D"):
            response = requests.get("https://huggingface.co/papers")
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
                img=rounded_els[0].find("img").attrs["src"],
                upvotes=int(rounded_els[1].text.strip()),
                n_authors=int(re.findall(r"[0-9]+", article_el.find("ul").text)[0]),
                id=article_el.find("a").attrs["href"].split("/")[-1],
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

    def getById(self, id):
        if id in self.articles:
            return self.articles[id]
        else:
            article = Article(id)
            article.load()
            self.articles[id] = article
            return article

    def compute_embeddings(self):
        for article in tqdm(self.articles.values()):
            article.compute_embedding()