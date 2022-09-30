from selenium import webdriver
from dotenv import load_dotenv
import os
from search_google import search_google
import time
import json

load_dotenv()

REMOTE_URL = os.environ['REMOTE_URL']
SC_FOLDER = os.environ['SC_FOLDER']

with open("./www.linkedin.com.cookies.json", "r") as fc:
    contents = fc.read()
    cookies_dict = json.loads(contents)

if not os.path.exists(SC_FOLDER):
    os.makedirs(SC_FOLDER)

firefox_options = webdriver.FirefoxOptions()
driver = webdriver.Remote(
    command_executor=REMOTE_URL,
    options=firefox_options
)

driver.get("https://www.linkedin.com/")

for cookie in cookies_dict:
    driver.add_cookie({"name": cookie['name'], "value": cookie['value'], "domain": cookie['domain']})

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