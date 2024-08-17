import dns.resolver  # Used For DNS Resolution To Check If A Subdomain Exists
from colorama import Fore, init  # Coloring Foreground For Text
import concurrent.futures  # To Speed Up Things By Threads/Workers

init(autoreset=True)
banner = """

 _______ _     _ ______  _     _ _     _ __   _ _______ _______  ______
 |______ |     | |_____] |_____| |     | | \  |    |    |______ |_____/
 ______| |_____| |_____] |     | |_____| |  \_|    |    |______ |    \_
                                                            Version 1.1             
                                                                By MR BILRED
                                                                
SubHunter is a Python tool designed for discovering subdomains associated with a target domain. This tool is 
practical for cybersecurity enthusiasts and penetration testers who want to map out potential subdomains quickly and 
efficiently.

SubHunter Version 1.1 uses a predefined list of over 500 common and potential subdomains to check against a target 
domain. The tool leverages DNS resolution to determine if a subdomain exists.

Created by MR BILRED aka Bilal Ahmad Khan
GitHub: https://github.com/BilalAhmadKhanKhattak                                                                                                       
"""
print(Fore.LIGHTCYAN_EX + banner)


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


def enumerate_subdomains(domain_to_be_processed):
    """Enumerate Through A PREDEFINED LIST of subdomains to find the existing ones..."""
    subdomains_list = [
        "www", "mail", "ftp", "dev", "test", "api", "staging", "beta",
        "shop", "blog", "admin", "support", "portal", "secure", "vpn",
        "chat", "news", "m", "mobile", "cdn", "assets", "download",
        "images", "static", "media", "docs", "store", "services", "internal",
        "auth", "login", "payments", "status", "prod", "backup", "monitor",
        "dashboard", "app", "console", "webmail", "crm", "db", "sandbox",
        "new", "social", "private", "info", "help", "api2", "account",
        "forum", "tickets", "mail2", "office", "reviews", "community",
        "feedback", "resources", "video", "calendar", "docs2", "wiki",
        "support2", "knowledge", "status2", "alerts", "monitoring",
        "billing", "newsletter", "payment", "docs3", "mobile2", "dev2",
        "test2", "api3", "data", "updates", "admin2", "support3",
        "portal2", "secure2", "app2", "server", "appdev", "cloud",
        "web", "desktop", "project", "api4", "user", "team",
        "download2", "contact", "contactus", "guides", "tools", "training",
        "alerts2", "files", "archive", "backup2", "images2", "media2",
        "status3", "monitor2", "api5", "beta2", "dev3", "test3",
        "shop2", "blog2", "admin2", "support3", "portal3", "secure3",
        "vpn2", "chat2", "news2", "cdn2", "assets2", "download3",
        "store2", "services2", "internal2", "auth2", "login2", "payments2",
        "prod2", "backup3", "dashboard2", "console2", "webmail2",
        "crm2", "db2", "sandbox2", "social2", "private2", "info2",
        "help2", "api6", "account2", "forum2", "tickets2", "mail3",
        "office2", "reviews2", "community2", "feedback2", "resources2",
        "video2", "calendar2", "wiki2", "support3", "knowledge2",
        "alerts3", "monitoring2", "billing2", "newsletter2", "payment2",
        "docs4", "mobile3", "dev4", "test4", "data2", "updates2",
        "admin3", "support4", "portal4", "secure4", "app3", "server2",
        "appdev2", "cloud2", "desktop2", "project2", "api7", "user2",
        "team2", "contact2", "contactus2", "guides2", "tools2", "training2",
        "alerts4", "files2", "archive2", "backup4", "images3", "media3",
        "status4", "monitor3", "api8", "beta3", "dev5", "test5",
        "shop3", "blog3", "admin3", "support5", "portal5", "secure5",
        "vpn3", "chat3", "news3", "cdn3", "assets3", "download4",
        "store3", "services3", "internal3", "auth3", "login3", "payments3",
        "prod3", "backup5", "dashboard3", "console3", "webmail3",
        "crm3", "db3", "sandbox3", "social3", "private3", "info3",
        "help3", "api9", "account3", "forum3", "tickets3", "mail4",
        "office3", "reviews3", "community3", "feedback3", "resources3",
        "video3", "calendar3", "wiki3", "support4", "knowledge3",
        "alerts5", "monitoring3", "billing3", "newsletter3", "payment3",
        "docs5", "mobile4", "dev6", "test6", "data3", "updates3",
        "admin4", "support5", "portal6", "secure6", "app4", "server3",
        "appdev3", "cloud3", "desktop3", "project3", "api10", "user3",
        "team3", "contact3", "contactus3", "guides3", "tools3", "training3",
        "alerts6", "files3", "archive3", "backup6", "images4", "media4",
        "status5", "monitor4", "api11", "beta4", "dev7", "test7",
        "shop4", "blog4", "admin4", "support6", "portal7", "secure7",
        "vpn4", "chat4", "news4", "cdn4", "assets4", "download5",
        "store4", "services4", "internal4", "auth4", "login4", "payments4",
        "prod4", "backup7", "dashboard4", "console4", "webmail4",
        "crm4", "db4", "sandbox4", "social4", "private4", "info4",
        "help4", "api12", "account4", "forum4", "tickets4", "mail5",
        "office4", "reviews4", "community4", "feedback4", "resources4",
        "video4", "calendar4", "wiki4", "support5", "knowledge4",
        "alerts7", "monitoring4", "billing4", "newsletter4", "payment4",
        "docs6", "mobile5", "dev8", "test8", "data4", "updates4",
        "admin5", "support6", "portal8", "secure8", "app5", "server4",
        "appdev4", "cloud4", "desktop4", "project4", "api13", "user4",
        "team4", "contact4", "contactus4", "guides4", "tools4", "training4",
        "alerts8", "files4", "archive4", "backup8", "images5", "media5",
        "status6", "monitor5", "api14", "beta5", "dev9", "test9",
        "shop5", "blog5", "admin5", "support7", "portal9", "secure9",
        "vpn5", "chat5", "news5", "cdn5", "assets5", "download6",
        "store5", "services5", "internal5", "auth5", "login5", "payments5",
        "prod5", "backup9", "dashboard5", "console5", "webmail5",
        "crm5", "db5", "sandbox5", "social5", "private5", "info5",
        "help5", "api15", "account5", "forum5", "tickets5", "mail6",
        "office5", "reviews5", "community5", "feedback5", "resources5",
        "video5", "calendar5", "wiki5", "support6", "knowledge5",
        "alerts9", "monitoring5", "billing5", "newsletter5", "payment5",
        "docs7", "mobile6", "dev10", "test10", "data5", "updates5",
        "admin6", "support7", "portal10", "secure10", "app6", "server5",
        "appdev5", "cloud5", "desktop5", "project5", "api16", "user5",
        "team5", "contact5", "contactus5", "guides5", "tools5", "training5",
        "alerts10", "files5", "archive5", "backup10", "images6", "media6",
        "status7", "monitor6", "api17", "beta6", "dev11", "test11",
        "shop6", "blog6", "admin6", "support8", "portal11", "secure11",
        "vpn6", "chat6", "news6", "cdn6", "assets6", "download7",
        "store6", "services6", "internal6", "auth6", "login6", "payments6",
        "prod6", "backup11", "dashboard6", "console6", "webmail6",
        "crm6", "db6", "sandbox6", "social6", "private6", "info6",
        "help6", "api18", "account6", "forum6", "tickets6", "mail7",
        "office6", "reviews6", "community6", "feedback6", "resources6",
        "video6", "calendar6", "wiki6", "support7", "staging2", "api18", "beta7", "test12"
    ]  # If you think this list is huge, relax, I Just Copied it XD

    valid_subdomains = []

    ''' A lil bit tricky snippet, but u gotta understand this, I'm Leaving this one commented with the explanation'''
    # with concurrent.futures.ThreadPoolExecutor(max_workers=12) as executor:  # Creates a pool of 12 worker threads.
    #     futures = {executor.submit(check_subdomain, sub, domain): sub for sub in  # 'check_subdomain' func to be run
    #                subdomains_list}  # in separate thread and sub and domain are arguments, the result of 'submit' is
    #     # a 'Future' object, which represents a task that will complete in the future
    #
    #     for future in concurrent.futures.as_completed(futures):
    #         result = future.result()
    #         if result:
    #             valid_subdomains.append(result)
    # return valid_subdomains

    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        futures = {executor.submit(check_subdomain, sub, domain_to_be_processed): sub for sub in subdomains_list}
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                valid_subdomains.append(result)
    return valid_subdomains


if __name__ == "__main__":
    domain = input(Fore.LIGHTCYAN_EX + "Enter The Domain: ")
    found_subdomains = enumerate_subdomains(domain)
    print(Fore.LIGHTCYAN_EX + f"\nValid Subdomains For {domain}:")
    for i, subdomain in enumerate(found_subdomains, start=1):
        print(Fore.LIGHTCYAN_EX + f"{i}. {subdomain}")

    input(Fore.GREEN + "_____End Bro_____" "\nEnter Any Key To Exit")
