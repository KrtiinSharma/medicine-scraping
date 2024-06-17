from helper import *


headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
med_name = input("Enter the name of the medicine: ").lower()
med_name_new = ""
for i in med_name:
    if (i == " "):
        med_name_new += "%20"
    else:
        med_name_new += i

start_time = time.time()
        
mg_1 = one_mg(f"https://www.1mg.com/search/all?name={med_name_new}", med_name)
apollo = apollo_meds(f"https://www.apollopharmacy.in/search-medicines/{med_name_new}", med_name)
tm = truemeds(f"https://www.truemeds.in/search/{med_name_new}", med_name)
pharm = pharmeasy(f"https://pharmeasy.in/search/all?name={med_name_new}", med_name)
nm = netmeds(f"https://www.netmeds.com/catalogsearch/result/{med_name_new}/all", med_name)

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    # This is the master process; it can handle common tasks.
    # For example, you can read the list of links to process and divide them among workers.
    links = [f"https://www.1mg.com/search/all?name={med_name_new}", f"https://www.apollopharmacy.in/search-medicines/{med_name_new}", f"https://www.truemeds.in/search/{med_name_new}", "https://pharmeasy.in/search/all?name={med_name_new}", f"https://www.netmeds.com/catalogsearch/result/{med_name_new}/all"]  # Your list of links
    num_links = len(links)

    if size > 1:  # Check if there are enough processes to divide the work.
        # Divide the work among workers.
        work_per_worker = num_links // (size - 1)
        for i in range(1, size):
            start = (i - 1) * work_per_worker
            end = i * work_per_worker if i < size - 1 else num_links
            worker_data = links[start:end]
            comm.send(worker_data, dest=i)
    else:
        print("There are not enough processes to divide the work.")
else:
    # This is a worker process; it receives its portion of work from the master.
    worker_data = comm.recv(source=0)

    # Process the received data (worker_data) in parallel.
    # You can call your existing functions on this data.

# Ensure all processes have finished their work before proceeding.

    
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

comm.Barrier()

if rank == 0:
    print("All processes have completed.")

end_time = time.time()
total_time = end_time - start_time
print(f"Total running time: {total_time} seconds")


with open("med_list.json", "w") as f:
    json.dump(meds, f, indent = 2)

# Finalize MPI
MPI.Finalize()