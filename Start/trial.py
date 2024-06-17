from bs4 import BeautifulSoup
import requests
import lxml
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

med_name = "dolo 650"

med_name_new = ""

for i in med_name:
    if (i == " "):
        med_name_new += "%20"
    else:
        med_name_new += i

Netmeds = []

link2 = f"https://www.netmeds.com/catalogsearch/result/{med_name_new}/all"
print(link2)
site2 = BeautifulSoup(requests.get(link2,headers=headers).content,features="lxml")

f = open("dump.txt")
f.write(str(site2))
f.close()

tab_names = site2.findAll("span", {"class" : "clsgetname"})
tab_names = [str(x) for x in tab_names]
tab_names = site2.findAll("a",{"class" : "category_name"} )
tab_names = [str(x) for x in tab_names]
print(tab_names)
price_list = site2.findAll("span", {"class" : "price_box"})
price_list = [str(x) for x in price_list]
print(price_list)
for i in range(len(tab_names)):
    tab_name = tab_names[i].split(">")[1].split("<")[0]
    price = str(price_list[i]).split(">")[1].split("</span>")[0]
    string = f"{tab_name} - {price}"
    Netmeds.append(string)
