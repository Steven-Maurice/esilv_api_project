import requests 
from bs4 import BeautifulSoup

class Article:
    def __init__(self, id, title=None, media=None, upvotes=None, n_authors=None):
        self.title = title
        self.media = media
        self.upvotes = upvotes
        self.n_authors = n_authors
        self.id = id
        self.url = "https://huggingface.co/papers/" + self.id
        self.abstract = None
        self.embedding = None
        self.authors = []
        self.loaded = False

    def load(self):
        if self.loaded: return
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, "html.parser")
        self.authors = [
            author.text.strip() for author in soup.select("span.author button")
        ]
        print(self.id)
        self.abstract = soup.select_one("h2 + p").text
        self.pdfUrl = soup.select_one("div a + a").attrs["href"]
        self.loaded=True

    def preview(self):
        return {
            "id": self.id,
            "media": self.media,
            "title": self.title,
            "n_authors": self.n_authors,
            "url": self.url,
        }

    def detail(self):
        self.load()
        return {
            "id": self.id,
            "media": self.media,
            "title": self.title,
            "n_authors": self.n_authors,
            "url": self.url,
            "authors": self.authors,
            "abstract": self.abstract,
            "pdfUrl": self.pdfUrl
        }
        
    def compute_embedding(self, sentenceTransformerModel):
        if self.embedding is not None:
            return
        if self.abstract is None: 
            self.load()
        embeddings = sentenceTransformerModel.encode([self.title, self.abstract])
        self.embedding = embeddings[0] * 0.6 + embeddings[1] * 0.4