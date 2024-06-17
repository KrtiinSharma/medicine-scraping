from bs4 import BeautifulSoup
import requests
import lxml

import json

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

med_name = "dolo 650"

med_name_new = ""

for i in med_name:
    if (i == " "):
        med_name_new += "%20"
    else:
        med_name_new += i

link = f"https://www.1mg.com/search/all?name={med_name_new}"
print(link)
link1 = f"https://pharmeasy.in/search/all?name={med_name_new}"
print(link1)
link2 = f"https://www.netmeds.com/catalogsearch/result/{med_name_new}/all"
print(link2)
link3 = f"https://www.apollopharmacy.in/search-medicines/{med_name_new}"
print(link3)
link4 = f"https://frankrosspharmacy.com/searchResult/{med_name_new}/"
print(link4)

site = BeautifulSoup(requests.get(link,headers=headers).content,features="lxml")
site1 = BeautifulSoup(requests.get(link1,headers=headers).content,features="lxml")
site2 = BeautifulSoup(requests.get(link2,headers=headers).content,features="lxml")
site3 = BeautifulSoup(requests.get(link3,headers=headers).content,features="lxml")
site4 = BeautifulSoup(requests.get(link4,headers=headers).content,features="lxml")

mg1, pharmeasy, netmeds , apollopharmacy , frankrosspharmacy= [], [], [], [], []


# tab_names = site.findAll("span", {"class" : "style__pro-title___3zxNC"})
# tab_names = [str(x) for x in tab_names]
# strip_type = site.findAll("div", {"class" : "style__pack-size___254Cd"})
# strip_type = [str(x) for x in strip_type]
# price_list = site.findAll("div", {"class" : "style__price-tag___B2csA"})
# price_list = [str(x) for x in price_list]
# for i in range(len(tab_names)):
#     tab_name = tab_names[i].split(">")[1].split("<")[0]
#     strip_types = strip_type[i].split(">")[1].split("<")[0]
#     price = str(price_list[i]).split("->")[1].split("<")[0]
#     string = f"{tab_name} - {strip_types} - {price}"
#     mg1.append(string)

# tab_names = site1.findAll("h1", {"class" : "ProductCard_medicineName__8Ydfq"})
# tab_names = [str(x) for x in tab_names]
# price_list = site1.findAll("div", {"class" : "ProductCard_ourPrice__yDytt"})
# price_list = [str(x) for x in price_list]
# for i in range(len(tab_names)):
#     tab_name = tab_names[i].split(">")[1].split("<")[0]
#     price = (price_list[i]).split("-->")[1].split("</div>")[0]
#     string = f"{tab_name} - {price}"
#     pharmeasy.append(string)
    
# tab_names = site2.findAll("span", {"class" : "clsgetname"})
# tab_names = [str(x) for x in tab_names]
# price_list = site2.findAll("span", {"id" : "final_price"})
# price_list = [str(x) for x in price_list]
# for i in range(len(tab_names)):
#     tab_name = tab_names[i].split(">")[1].split("<")[0]
#     price = str(price_list[i]).split(">")[1].split("</span>")[0]
#     string = f"{tab_name} - {price}"
#     netmeds.append(string)
    
    
# tab_names = site3.findAll("p", {"class" : "ProductCard_productName__vXoqs"})
# tab_names = [str(x) for x in tab_names]
# price_list = site3.findAll("span", {"class" : "ProductCard_regularPrice__z3z3F"})
# print(price_list)

# price_list = [str(x) for x in price_list]
# #print(price_list)
# for i in range(len(tab_names)):
#     tab_name = tab_names[i].split(">")[1].split("<")[0]
#     price = str(price_list[i]).split("->")[1].split("<")[0]
#     print(price)
#     string = f"{tab_name} - {price}"
#     apollopharmacy.append(string)
    
# tab_names = site4.findAll("a", {"class" : "ng-binding"})
# tab_names = [str(x) for x in tab_names]
# price_list= site4.findAll("span", {"class" : "price ng-binding"})
# price_list= [int(x) for x in price_list]
# for i in range(len(tab_names)):
#     tab_name = tab_names[i].split(">")[1].split("<")[0]
#     price = price_list[i]
#     string = f"{tab_name} - {price}"
#     frankrosspharmacy.append(string)
    

d = {
    "1mg" : mg1,
    "pharmeasy" : pharmeasy,
     "netmeds" : netmeds,
     "apollopharmacy" : apollopharmacy,
#     "frankrosspharmacy" : frankrosspharmacy
 }
    
with open("meds.json", "w") as f:
    json.dump(d, f, indent = 2)