from bs4 import BeautifulSoup
import re
def articles(response):
    soup = BeautifulSoup(response.text, "html.parser")
    articles_els = soup.find_all("article")
    articles = []
    for article_el in articles_els: 
        rounded_els = article_el.select(".rounded-xl")
        article = {
            "title":article_el.find("h3").text,
            "img":rounded_els[0].find("img").attrs["src"],
            "upvotes": int(rounded_els[1].text.strip()),
            "authors":int(re.findall(r"[0-9]+",article_el.find("ul").text)[0]),
            "url": "https://huggingface.co"+article_el.find("a").attrs["href"]
        }
        articles.append(article)
    return articles
    
    