# Cookies

## Description 
```
Be patient. The site is very hungry)
```

## Writeup

Visiting the website we receive the message `I'm hungry!!! Feed me!`. <br/>
Getting this I thought I would just have to send a huge payload in the header `cookies`. <br/>
For this purpose I write a small script. <br/>
```py
import requests

url = 'https://ctf.mf.grsu.by/tasks/0423917d9fc95820065749eb3ca411fe/'

cookies = {}

# Loop to create a dictionary with 100 different objects in a dictionary
for i in range(1, 101):
    cookies[f'object{i}'] = f'randomContent{i}'

req = requests.get(url, cookies=cookies, verify=False)

print(req.text)
```

Executing this I obtained the flag which concludes the writeup. <br/>
```html
<html>
<head>
    <title>CTF-task Grodno</title>
    <meta name="owner" content="grodno_CTF" />
    <meta name="publisher" content="grodno_CTF" />
    <meta name="copyright" content="grodno_CTF" />
    <meta name="robots" content="noindex,nofollow">
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
</head>
<body>


    Я наелся! Вот флаг:grodno{515ec0oW0uJWX1ZYxG9caZFX1D8f1848}  </body>
</html>
```