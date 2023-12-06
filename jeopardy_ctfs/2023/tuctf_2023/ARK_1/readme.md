# A.R.K. 1

## Description
```
One sheep, two sheep, three sheep. (Note: to speed up the process, only include entries containing "sheep" in your attempts) Flag is in the format TUCTF{<password>} (don't include the brackets)
```

## Provided Files
`sheep`

## Writeup

Starting off I took a look at the file. <br/>
```sh
file sheep

sheep: OpenSSH private key
```

Looking at the actual content. <br/>
```sh
cat sheep

-----BEGIN OPENSSH PRIVATE KEY-----
b3B...uog==
-----END OPENSSH PRIVATE KEY-----
```

It just looked like an avergae openssh private key. <br/>
Knowing that ssh private keys are bruteforceable I got the file has. <br/>
```sh
ssh2john sheep > sheep.hash
```

Now I only needed a wordlist to crack it. <br/>
The description stated that we should only include "sheep" so I created the following wordlist. <br/>
```sh
grep "sheep" rockyou.txt > sheep_wordlist.txt
```

Using this wordlist I started bruteforcing the openssh private key. <br/>
```sh
john --wordlist=sheep_wordlist.txt sheep.hash
Using default input encoding: UTF-8
Loaded 1 password hash (SSH, SSH private key [RSA/DSA/EC/OPENSSH 32/64])
Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 2 for all loaded hashes
Cost 2 (iteration count) is 16 for all loaded hashes
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
baabaablacksheep (sheep)     
1g 0:00:00:01 DONE (2023-12-01 18:11) 0.7936g/s 50.79p/s 50.79c/s 50.79C/s bluesheep..sheepp
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```

I couldn't do anything much with the decrypted private key, so I just tried the cracked password as flag. <br/>
Luckily it worked and we found the correct flag `TUCTF{baabaablacksheep}` which concluded the challenge.






