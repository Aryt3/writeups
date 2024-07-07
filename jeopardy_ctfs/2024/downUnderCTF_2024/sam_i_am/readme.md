# SAM I AM

## Description
```
The attacker managed to gain Domain Admin on our rebels Domain Controller! 
Looks like they managed to log on with an account using WMI and dumped some files.

Can you reproduce how they got the Administrator's Password with the artifacts provided?

Place the Administrator Account's Password in DUCTF{}, e.g. DUCTF{password123!}

Author: TurboPenguin
```

## Provided Files
```
- sam.bak
- system.bak
```

## Writeup

Having both the `system.bak` file and the `sam.bak` file I knew that I was probably able to extract the password-hash using a tool like `samdump2` so I started up my Forensics-Vm. <br/>
```sh
$ samdump2 system.bak sam.bak > hashes.txt
$ ls -la
insgesamt 12080
drwxr-xr-x 2 root root     4096  6. Jul 17:37 .
drwxr-xr-x 3 root root     4096  6. Jul 17:36 ..
-rw-r--r-- 1 root root      177  6. Jul 17:37 hashes.txt
-rw-r--r-- 1 root root    32768  6. Jul 17:35 sam.bak
-rw-r--r-- 1 root root 12324864  6. Jul 17:35 system.bak
$ cat hashes.txt 
Administrator:500:aad3b435b51404eeaad3b435b51404ee:476b4dddbbffde29e739b618580adb1e:::
*disabled* Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
```

Using an online [hash-cracker](https://hashes.com/en/decrypt/hash) I was able to extract `!checkerboard1` which concludes this writeup. <br/>