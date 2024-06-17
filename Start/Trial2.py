from bs4 import BeautifulSoup
import requests
import lxml
import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import codecs
import re
from webdriver_manager.chrome import ChromeDriverManager


headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
med_name = "dolo 650"
med_name_new = ""
for i in med_name:
    if (i == " "):
        med_name_new += "%20"
    else:
        med_name_new += i
mg1 = []
apollo= []
Netmeds=[]
FrankRoss=[]
Pharmeasy=[]
Truemeds=[]
Medibuddy=[]

# #1MG done
link = f"https://www.1mg.com/search/all?name={med_name_new}"
print(link)
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
    mg1.append(string)
    
# # #Apollo done
link3 = f"https://www.apollopharmacy.in/search-medicines/{med_name_new}"
print(link3)
site3 = BeautifulSoup(requests.get(link3,headers=headers).content,features="lxml")
tab_names = site3.findAll("p", {"class" : "ProductCard_productName__vXoqs"})
tab_names = [str(x) for x in tab_names]
price_list = site3.findAll("div", {"class" : "ProductCard_priceGroup__4D4k0"})
for i in range(len(tab_names)):
    tab_name = tab_names[i].split(">")[1].split("<")[0]
    price = str(price_list[i]).split("-->")[1].split("<!")[0]
    string = f"{tab_name} - {price}"
    apollo.append(string)
    

#Netmeds
# link2 = f"https://www.netmeds.com/catalogsearch/result/{med_name_new}/all"
# print(link2)
# site2 = BeautifulSoup(requests.get(link2,headers=headers).content,features="lxml")
# tab_names = site2.findAll("span", {"class" : "clsgetname"})
# tab_names = [str(x) for x in tab_names]
# tab_names = site2.findAll("a",{"class" : "category_name"} )
# tab_names = [str(x) for x in tab_names]
# print(tab_names)
# price_list = site2.findAll("span", {"class" : "price_box"})
# price_list = [str(x) for x in price_list]
# print(price_list)
# for i in range(len(tab_names)):
#     tab_name = tab_names[i].split(">")[1].split("<")[0]
#     price = str(price_list[i]).split(">")[1].split("</span>")[0]
#     string = f"{tab_name} - {price}"
#     Netmeds.append(string)
    
    
    
#  FrankRoss

# link4 = f"https://frankrosspharmacy.com/searchResult/{med_name_new}/"
# print(link4)

# site4 = BeautifulSoup(requests.get(link4,headers=headers).content,features="lxml")

# tab_names = site4.findAll("a", {"class" : "ng-binding"})
# tab_names = [str(x) for x in tab_names]
# price_list= site4.findAll("span", {"class" : "price ng-binding"})
# price_list= [int(x) for x in price_list]
# print(price_list)
# for i in range(len(tab_names)):
#     tab_name = tab_names[i].split(">")[1].split("<")[0]
#     price = price_list[i]
#     string = f"{tab_name} - {price}"
#     FrankRoss.append(string)


# # Pharmeasy done
link1 = f"https://pharmeasy.in/search/all?name={med_name_new}"
print(link1)
site1 = BeautifulSoup(requests.get(link1,headers=headers).content,features="lxml")
tab_names = site1.findAll("h1", {"class" : "ProductCard_medicineName__8Ydfq"})
tab_names = [str(x) for x in tab_names]
price_list = site1.findAll("span", {"class" : "ProductCard_striked__jkSiD"})
price_list = [str(x) for x in price_list]
for i in range(len(price_list)):
    tab_name = tab_names[i].split(">")[1].split("<")[0]
    price = (price_list[i]).split("->")[1].split("</span>")[0]
    string = f"{tab_name} - {price}"
    Pharmeasy.append(string)

med="Saridon"
Alist=[word for word in apollo if med in word]
print("new lsit 2")
print(Alist)   
Mlist=[word for word in mg1 if med in word]
print(Mlist)

#True Meds
 
link5= f"https://www.truemeds.in/search/{med_name_new}"

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

link5 = "https://www.truemeds.in/search/dolo%20650"
wait = WebDriverWait(driver, 10)
driver.get(link5)

get_url = driver.current_url
wait.until(EC.url_to_be(link5))


if get_url == link5:
    page_source = driver.page_source

soup = BeautifulSoup(page_source,features="html.parser")
tab_names = soup.findAll("div", {"class" : "sc-452fc789-11 iHTDQb"})
tab_names = [str(x) for x in tab_names]

tab_names = soup.findAll("div", {"class" : "sc-452fc789-11 iHTDQb"})
tab_names = [str(x) for x in tab_names]
price_list = soup.findAll("span", {"class" : "sc-452fc789-15 dJeYYc"})
price_list = [str(x) for x in price_list]
for i in range(len(price_list)):
    tab_name = tab_names[i].split(">")[1].split("<")[0]
    price = (price_list[i]).split(">")[1].split("<")[0][1:]
    string = f"{tab_name} - {price}"
    Truemeds.append(string)


d = {
    "1mg": mg1,
    "apollo": apollo,
    "Netmeds": Netmeds,
    "FrankRoss": FrankRoss,
    "Pharmeasy": Pharmeasy,
    "Truemeds": Truemeds,
    "Medibuddy": Medibuddy,
}


with open("meds1.json", "w") as f:
    json.dump(d, f, indent=2)    