import dns.resolver  # Used For DNS Resolution To Check If A Subdomain Exists
from colorama import Fore, init  # Coloring Foreground For Text
import concurrent.futures  # To Speed Up Things By Threads/Workers
import time
import requests
import json
import random
from datetime import datetime



init(autoreset=True)
banner = r"""
 _______ _     _ ______  ______   _____  _     _ _______  ______
 |______ |     | |_____] |     \ |     |  \___/  |______ |_____/
 ______| |_____| |_____] |_____/ |_____| _/   \_ |______ |    \_

                                                            Version 2.0             
                                                                By MR BILRED

Did Someone Say Subdomains???
Oh I see! C'mon then!

SubDoxer Version 1.1 was a past! 
Used predefined list, but still gonna be used somehow
Leveraged DNS resolution to determine if a subdomain exists.

SubDoxer Version 2.0 taps into SSL/TLS certificates to identify the target's subdomains

DISCLAIMER:
This tool is intended for EDUCATIONAL and ETHICAL SECURITY RESEARCH only.
Unauthorized scanning of domains without permission is ILLEGAL. 
You are solely responsible for your actions. Use it responsibly...

Created by MR BILRED aka Bilal Ahmad Khan
GitHub: https://github.com/BilalAhmadKhanKhattak                                                                                                       
"""
print(Fore.LIGHTMAGENTA_EX + banner)


def check_subdomain(subdomain, domain_to_be_processed):
    """ This Block Of Code is just to Check IF the subdomain exists by resolving its DNS 'A' Record """
    try:
        full_domain = f"{subdomain}.{domain_to_be_processed}"
        dns.resolver.resolve(full_domain, 'A')
        print(Fore.GREEN + f"Subdomain Found: {full_domain}")
        return full_domain
    except dns.resolver.NXDOMAIN:  # NXDOMAIN means no A record found
        return None
    except Exception as e:
        print(Fore.LIGHTYELLOW_EX + f"Error Checking {full_domain}, Reason:{str(e)}")


def load_subdomains(filename):
    """Enumerate Through A PREDEFINED LIST of subdomains to find the existing ones..."""
    try:
        with open(filename, 'r') as file:

            subdomains = [line.strip() for line in file if line.strip()]
        return subdomains
    except FileNotFoundError:
        print(Fore.RED + f"Error: File {filename} not found")
    return []


def enumerate_subdomains(domain_to_be_processed):
    subdomains_list = load_subdomains("Subdomains_list")
    valid_subdomains = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        futures = {executor.submit(check_subdomain, sub, domain_to_be_processed): sub for sub in subdomains_list}
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                valid_subdomains.append(result)
    return valid_subdomains


def cert(domain_to_be_processed):
    url = f"https://crt.sh/?q=%25.{domain_to_be_processed}&output=json"
    attempts = 3
    headers = {  # I had to copy this stuff ;)
        "User-Agent": random.choice([
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Mozilla/5.0 (X11; Linux x86_64)",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
        ])
    }
    print(Fore.LIGHTCYAN_EX + f"[*] Fetching info from cert.sh for {domain_to_be_processed}")
    print(Fore.LIGHTMAGENTA_EX + f"[!] Timeout set to 30 secs... hang on")

    for attempt in range(1, attempts + 1):
        try:
            print(Fore.LIGHTYELLOW_EX + f"[+] Attempt {attempt}/{attempts}...")
            response = requests.get(url, headers=headers, timeout=30)

            if response.ok:
                timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
                file_name = f"{domain_to_be_processed}_cert_{timestamp}.json"
                print(Fore.LIGHTCYAN_EX + "Downloading JSON File...")
                with open(f"{file_name}", "w", encoding='utf-8') as f:
                    f.write(response.text)
                print(Fore.LIGHTGREEN_EX + f"Saved to {file_name}")
                return file_name
            else:
                print(Fore.LIGHTRED_EX + f"[!] Failed To get info from cert.sh... Status Code: {response.status_code}")

        except Exception as e:
            print(Fore.LIGHTRED_EX + f"[!] Ah man, Error on attempt {attempt}: {e}")

        if attempt < attempts:
            print(Fore.LIGHTBLUE_EX + f"[*] Retrying in 3 seconds...\n")
            time.sleep(3)

    print(Fore.LIGHTRED_EX + f"All Attempts Failed. Exiting...")
    return None


def parse_json(filepath):
    subdomains = set()
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for entry in data:
            names = entry.get('name_value', '').split('\n')
            for name in names:
                subdomains.add(name.strip().lower())
        return sorted(subdomains)
    except Exception as e:
        print(Fore.LIGHTRED_EX + f"[!] Error reading/parsing JSON: {e}")
    return []



if __name__ == "__main__":
    domain = input(Fore.LIGHTCYAN_EX + "Enter The Domain (e.g: example.com): ")
    found_subdomains = enumerate_subdomains(domain)

    print(Fore.LIGHTCYAN_EX + f"\nValid Subdomains For {domain}:")
    for i, subdomain in enumerate(found_subdomains, start=1):
        print(Fore.LIGHTCYAN_EX + f"{i}. {subdomain}\n")

    json_file = cert(domain)
    if json_file:
        results = parse_json(json_file)
        print(f"\nFound {len(results)} unique subdomains: \n")
        for i, sub in enumerate(results, 1):
            print(f"{i}. {sub}")

        with open(f"{json_file}Subdomains.txt", 'w', encoding='utf-8') as d:
            # d.write(results) # will raise: TypeError: write() argument must be str, not list
            d.write('\n'.join(results))
        print(Fore.LIGHTMAGENTA_EX + "[!] ATTENTION! Some certs might be expired!")
        print(Fore.LIGHTGREEN_EX + f"SUCCESSFULLY SAVED TO TXT FILE")
        print(Fore.LIGHTBLUE_EX + "If you really wanna dive deep, visit the sites below, they're worth it, I guess:"
                                  "\nsearch.censys.io"
                                  "\nosint.sh"
                                  "\ndigger.tools/subdomains"
                                  "\n"
                                  "\nThank me Later...")
    input(Fore.LIGHTGREEN_EX + "_____End Bro_____" "\nEnter Any Key To Exit")


















#  We're humans...
#  sometimes it gets hard... but it's not over yet... You gotta make it, the sky is all yours!
#  GO MAKE IT, man...! NEVER GIVE UP
#  BELIEVE IN YOURSELF
#  You're UNIQUE, YOU'RE SPECIAL!
#  IF YOU QUIT TODAY... YOU SUFFERED YESTERDAY FOR NOTHING (that's what I wrote on my Register)
#  DO SOMETHING THAT FINALLY MAKES A DIFFERENCE!
#  Help someone who's in pain...

#  Some words by Mr. BILRED