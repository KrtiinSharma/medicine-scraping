from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import codecs
import re
from webdriver_manager.chrome import ChromeDriverManager

import json


driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))


val = "https://www.truemeds.in/search/dolo%20650"
wait = WebDriverWait(driver, 10)
driver.get(val)

get_url = driver.current_url
wait.until(EC.url_to_be(val))


if get_url == val:
    page_source = driver.page_source

data = []

soup = BeautifulSoup(page_source,features="html.parser")
tab_names = soup.findAll("div", {"class" : "sc-452fc789-11 iHTDQb"})
tab_names = [str(x) for x in tab_names]

tab_names = soup.findAll("div", {"class" : "sc-452fc789-11 iHTDQb"})
tab_names = [str(x) for x in tab_names]
price_list = soup.findAll("span", {"class" : "sc-452fc789-15 dJeYYc"})
price_list = [str(x) for x in price_list]
print(price_list)
for i in range(len(price_list)):
    tab_name = tab_names[i].split(">")[1].split("<")[0]
    price = (price_list[i]).split(">")[1].split("<")[0][1:]
    string = f"{tab_name} - {price}"
    data.append(string)
    
print(json.dumps(data, indent = 2))