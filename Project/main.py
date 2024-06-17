from helper import *
start_time = time.time()

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
med_name = input("Enter the name of the medicine: ").lower()
med_name_new = ""
for i in med_name:
    if (i == " "):
        med_name_new += "%20"
    else:
        med_name_new += i


        
mg_1 = one_mg(f"https://www.1mg.com/search/all?name={med_name_new}", med_name)
apollo = apollo_meds(f"https://www.apollopharmacy.in/search-medicines/{med_name_new}", med_name)
tm = truemeds(f"https://www.truemeds.in/search/{med_name_new}", med_name)
pharm = pharmeasy(f"https://pharmeasy.in/search/all?name={med_name_new}", med_name)
nm = netmeds(f"https://www.netmeds.com/catalogsearch/result/{med_name_new}/all", med_name)

meds = {}


meds_dict = {
    "1mg" : mg_1,
    "Apollo" : apollo,
    "TrueMeds" : tm,
    "PharmEasy" : pharm,
    "Netmeds" : nm
}

with open("med_list1.json", "w") as f:
    json.dump(meds_dict, f, indent = 2)

for i in mg_1:
    meds[f"1mg: {' '.join(i.split()[:-1])}"] = float(i.split()[-1])
    
for i in apollo:
    meds[f"Apollo: {' '.join(i.split()[:-1])}"] = float(i.split()[-1])
    
for i in tm:
    meds[f"TrueMeds: {' '.join(i.split()[:-1])}"] = float(i.split()[-1])
    
for i in pharm:
    meds[f"PharmEasy: {' '.join(i.split()[:-1])}"] = float(i.split()[-1])
    
for i in nm:
    meds[f"NetMeds: {' '.join(i.split()[:-1])}"] = float(i.split()[-1])

meds_1 = sorted(meds.items(), key=lambda x:x[1], reverse=False)
meds = dict(meds_1)

end_time = time.time()
total_time = end_time - start_time
print(f"Total running time: {total_time} seconds")

with open("med_list.json", "w") as f:
    json.dump(meds, f, indent = 2)
    