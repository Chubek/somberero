from selenium import webdriver
from dotenv import load_dotenv
import os
from search_google import search_google
import time

load_dotenv()

REMOTE_URL = os.environ['REMOTE_URL']
SC_FOLDER = os.environ['SC_FOLDER']

if not os.path.exists(SC_FOLDER):
    os.makedirs(SC_FOLDER)

firefox_options = webdriver.FirefoxOptions()
driver = webdriver.Remote(
    command_executor=REMOTE_URL,
    options=firefox_options
)


search_queries = [
    "marketing united kingdom site:linkedin.com/in/",
    "marketing india site:linkedin.com/in/",
    "seo united states site:linkedin.com/in/",
    "email marketing kingdom site:linkedin.com/in/",
    "seo united kingdom site:linkedin.com/in/",
]


for sq in search_queries:
    links = search_google(sq)

    for i, link in enumerate(links):
        driver.get(link)
        time.sleep(5)
        driver.save_screenshot(os.path.join(SC_FOLDER, f"{link}_{i}.png"))




driver.quit()