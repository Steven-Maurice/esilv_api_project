import requests 

class Article:
    def __init__(self, url, title=None, img=None, upvotes=None, authors=None):
        self.title = title
        self.img = img
        self.upvotes = upvotes
        self.authors = authors
        self.url = url
        self.abstract = None