import time
from datetime import datetime as dt

hosts_path = r"C:\Users\aust1713\Desktop\git_playground\python 10 applications\12 - website blocker\hosts.txt"
redirect = "127.0.0.1"
sites_to_block = ["www.facebook.com", "facebook.com", "www.instagram.com", "instagram.com"]

def get_content(path):
   with open(path, "r") as file:
     return file.readlines()

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 7) <= dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 10):
        print("working hours")
        with open(hosts_path, "r+") as file:
            content = file.read()
            for site in sites_to_block:
                if site not in content:
                    file.write("\n{redirect} {site}".format(redirect = redirect, site = site))
    else:
        print("fun time!")
        content = get_content(hosts_path)
        if any(site in line for line in content for site in sites_to_block):
            with open(hosts_path, "w") as file:
                for line in content:
                    if not any(site in line for site in sites_to_block):
                        file.write(line)
                        print(line)
    time.sleep(5)
