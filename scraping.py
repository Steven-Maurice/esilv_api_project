from selenium import webdriver
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.delete_all_cookies()  
    driver.get("https://blog.google/technology/ai/")
    print('-----------------------------------------------------')
    print(f"Connected to the website: {driver.title}")
    print('-----------------------------------------------------')

    articles = driver.find_elements(By.CSS_SELECTOR, "div a.feed-article__overlay")



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
    print(f"The website is scrapped and the info are written in 'articles.json'")

    print('-----------------------------------------------------')