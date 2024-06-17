import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import codecs
import re
from webdriver_manager.chrome import ChromeDriverManager

from bs4 import BeautifulSoup
import requests
import lxml
import json


headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
}

def dynamic_conversion(site_link):
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    wait = WebDriverWait(driver, 10)
    driver.get(site_link)

    get_url = driver.current_url
    wait.until(EC.url_to_be(site_link))


    if get_url == site_link:
        page_source = driver.page_source

    soup = BeautifulSoup(page_source,features="html.parser")
    
    return soup

'''def create_dict(list):
    d = {}
    
    for i in list:
        d[i[0]] = i[1]
        
    return d'''

def clear_meds(med_list, og_name):
    l = og_name.split()
    l = [x for x in l if x.isalpha()]
    
    nl = []
    
    for i in l:
        for j in med_list:
            if (i in j.lower()) and (j not in nl):
                nl.append(j)
            
    return nl

def one_mg(link, med_name):
    medicines = []
    
    site = BeautifulSoup(requests.get(link, headers=headers).content, features="lxml")
    tab_names = site.findAll("span", {"class" : "style__pro-title___3zxNC"})
    if(len(tab_names)==0):
        tab_names = site.findAll("div", {"class" : "style__pro-title___3G3rr"})
    tab_names = [str(x) for x in tab_names]
    strip_type = site.findAll("div", {"class" : "style__pack-size___254Cd"})
    if(len(strip_type)==0):
        strip_type = site.findAll("div", {"class" : "style__pack-size___3jScl"})
    strip_type = [str(x) for x in strip_type]
    price_list = site.findAll("div", {"class" : "style__price-tag___B2csA"})
    if(len(price_list)==0):
        price_list = site.findAll("div", {"class" : "style__price-tag___KzOkY"})
    price_list = [str(x) for x in price_list]
    for i in range(len(tab_names)):
        tab_name = tab_names[i].split(">")[1].split("<")[0]
        strip_types = strip_type[i].split(">")[1].split("<")[0]
        price = str(price_list[i]).split("->")[1].split("<")[0]
        string = f"{tab_name} - {strip_types} - {price}"
        medicines.append(string)
        
    return clear_meds(medicines, med_name)

def apollo_meds(link, med_name):
    apollo = []
    
    site3 = BeautifulSoup(requests.get(link,headers=headers).content,features="lxml")
    tab_names = site3.findAll("p", {"class" : "ProductCard_productName__vXoqs"})
    tab_names = [str(x) for x in tab_names]
    price_list = site3.findAll("div", {"class" : "ProductCard_priceGroup__4D4k0"})
    for i in range(len(tab_names)):
        tab_name = tab_names[i].split(">")[1].split("<")[0]
        price = str(price_list[i]).split("-->")[1].split("<!")[0]
        string = f"{tab_name} - {price}"
        apollo.append(string)
    return clear_meds(apollo, med_name)

def truemeds(link, med_name):
    soup = dynamic_conversion(link)
    tm = []

    tab_names = soup.findAll("div", {"class" : "sc-452fc789-11 iHTDQb"})
    tab_names = [str(x) for x in tab_names]
    price_list = soup.findAll("span", {"class" : "sc-452fc789-15 dJeYYc"})
    price_list = [str(x) for x in price_list]
    for i in range(len(price_list)):
        tab_name = tab_names[i].split(">")[1].split("<")[0]
        price = (price_list[i]).split(">")[1].split("<")[0][1:]
        string = f"{tab_name} - {price}"
        tm.append(string)
        
    print(tm)
        
    return clear_meds(tm, med_name)
        
def pharmeasy(link, med_name):
    pharm = []
    
    site1 = BeautifulSoup(requests.get(link,headers=headers).content,features="lxml")
    tab_names = site1.findAll("h1", {"class" : "ProductCard_medicineName__8Ydfq"})
    tab_names = [str(x) for x in tab_names]
    price_list = site1.findAll("span", {"class" : "ProductCard_striked__jkSiD"})
    price_list = [str(x) for x in price_list]
    for i in range(len(price_list)):
        tab_name = tab_names[i].split(">")[1].split("<")[0]
        price = (price_list[i]).split("->")[1].split("</span>")[0]
        string = f"{tab_name} - {price}"
        pharm.append(string)
        
    return clear_meds(pharm, med_name)

def netmeds(link, med_name):
    soup = dynamic_conversion(link)
    nm = []

    site2 = BeautifulSoup(requests.get(link,headers=headers).content,features="lxml")
    tab_names = soup.findAll("span", {"class" : "clsgetname"})
    tab_names = [str(x) for x in tab_names]
    price_list = soup.findAll("span", {"id" : "final_price"})
    if not price_list:
        print("in")
        price_list = soup.findAll("span", {"class" : "final-price"})
    price_list = [str(x) for x in price_list]
    for i in range(len(price_list)):
        tab_name = tab_names[i].split(">")[1].split("<")[0]
        price = (price_list[i]).split(">")[1].split("<")[0][1:]
        string = f"{tab_name} - {price}"
        nm.append(string)
        
    return clear_meds(nm, med_name)


        
    