from bs4 import BeautifulSoup
import requests
import lxml

import json

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

med_name = input()

med_name_new = ""

for i in med_name:
    if (i == " "):
        med_name_new += "%20"
    else:
        med_name_new += i

# part1
link = f"https://www.1mg.com/search/all?name={med_name_new}" #1mg
print(link)
link1 = f"https://www.netmeds.com/catalogsearch/result/{med_name_new}/all" #netmeds
print(link1)
link2 = f"https://www.apollopharmacy.in/search-medicines/{med_name_new}" #apollo
print(link2)

# part2
site = BeautifulSoup(requests.get(link,headers=headers).content,features="lxml")
site1 = BeautifulSoup(requests.get(link1,headers=headers).content,features="lxml")
site2 = BeautifulSoup(requests.get(link2,headers=headers).content,features="lxml")

#part3
mg1, netmeds, apollo = [], [], []

# part4
# 1mg
tab_names = site.findAll("span", {"class" : "style_pro-title__3zxNC"})
tab_names = [str(x) for x in tab_names]
strip_type = site.findAll("div", {"class" : "style_pack-size__254Cd"})
strip_type = [str(x) for x in strip_type]
price_list = site.findAll("div", {"class" : "style_price-tag__B2csA"})
price_list = [str(x) for x in price_list]
for i in range(len(tab_names)):
    tab_name = tab_names[i].split(">")[1].split("<")[0]
    strip_types = strip_type[i].split(">")[1].split("<")[0]
    price_lists = price_list[i].split(">")[1].split("<")[0]
    pl = price_list[i].split("-->")[1].split("</div>")[0]
    string = f"{tab_name} - {strip_types} - {price_lists}{pl}"
    mg1.append(string)

# netmeds
tab_names = site1.findAll("span", {"class" : "clsgetname"})
tab_names = [str(x) for x in tab_names]
price_list = site1.findAll("span", {"id" : "final_price"})
price_list = [str(x) for x in price_list]
print(tab_names)
print(price_list)
for i in range(len(tab_names)):
    tab_name = tab_names[i].split("name\">")[1].split("</span>")[0]
    pl = price_list[i].split("price\">")[1].split("</span>")[0]
    string = f"{tab_name} - {pl}"
    netmeds.append(string)

# apollo
tab_names = site2.findAll("p", {"class" : "ProductCard_productName__vXoqs"})
tab_names = [str(x) for x in tab_names]
price_list = site2.findAll("span", {"class" : "ProductCard_regularPrice__z3z3F"})
price_list = [str(x) for x in price_list]
for i in range(len(tab_names)):
    tab_name = tab_names[i].split(">")[1].split("<")[0]
    price_lists = price_list[i].split(">(")[1].split("<!")[0]
    pl = price_list[i].split("-->")[1].split("<!")[0]
    string = f"{tab_name} - {price_lists}{pl}"
    apollo.append(string)

# part5
d = {"1mg" : mg1, "netmeds": netmeds, "apollo" : apollo}

# part6
with open("meds.json", "w") as f:
    json.dump(d, f, indent = 2)