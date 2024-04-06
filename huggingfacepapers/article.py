import requests 
from bs4 import BeautifulSoup

class Article:
    def __init__(self, url, title=None, img=None, upvotes=None, authors=None):
        self.title = title
        self.img = img
        self.upvotes = upvotes
        self.authors = authors
        self.url = url
        self.abstract = None


    def load(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, "html.parser")
        self.authors = [
            author.text.strip() for author in soup.select("span.author button")
        ]
        self.abstract = soup.select_one("h2 + p").text
        self.pdfUrl = soup.select_one("div a + a").attrs["href"]

    def preview(self):
        return {
            "id": self.id,
            "img": self.img,
            "title": self.title,
            "n_authors": self.n_authors,
            "url": self.url,
        }

    def detail(self):
        return {
            "id": self.id,
            "img": self.img,
            "title": self.title,
            "n_authors": self.n_authors,
            "url": self.url,
            "authors": self.authors,
            "abstract": self.abstract,
            "pdfUrl": self.pdfUrl,
            "embedding": self.embedding.tolist(),
        }