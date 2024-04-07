from selenium import webdriver
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

 
def scrape():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.delete_all_cookies()  
    driver.get("https://blog.google/technology/ai/")
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "uni-article-card.feed-article"))
        )
        article_cards = driver.find_elements(By.CSS_SELECTOR, "uni-article-card.feed-article")
        data = []
 
        for article_card in article_cards:
            try:
                title_element = article_card.find_element(By.CSS_SELECTOR, "h3.feed-article__title")
                title = title_element.text
            except NoSuchElementException:
                title = "No Title"
            try:
                link_element = article_card.find_element(By.CSS_SELECTOR, "a.feed-article__overlay")
                link = link_element.get_attribute('href')
            except NoSuchElementException:
                link = "No URL"

            try:
                date_element = article_card.find_element(By.CSS_SELECTOR, "span.eyebrow__date")
                date = date_element.text
            except NoSuchElementException:
                date = "No Date"

            article_data = {
                "title": title,
                "url": link,
                "date": date
            }
            data.append(article_data)
 
        # Écriture dans le fichier JSON
        with open('articles.json', 'w') as outfile:
            json.dump(data, outfile)
 
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()
 
    return data