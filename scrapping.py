from selenium import webdriver
import json
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://deepmind.google/discover/blog/")
print('-----------------------------------------------------')
print(f"Connected to the website: {driver.title}")
print('-----------------------------------------------------')

articles = driver.find_elements(By.CSS_SELECTOR, "li a.glue-card.card")

data = []

for article in articles:

    href = article.get_attribute("href")
    text = article.text.split("\n")

    article_data = {
        "url": href,
        "category":text[0],
        "title": text[1],
        "description": text[2],
        "date": text[3]
    }
    data.append(article_data)

with open('articles.json', 'w') as outfile:
    json.dump(data, outfile)
    
driver.quit()

print('-----------------------------------------------------')
print(f"Website scrapped and info written in 'articles.json'")
print('-----------------------------------------------------')