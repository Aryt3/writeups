# CriptoRocks 

## Description
```
Description Bob: Do you have it yet? Alice: Sure! And the best of all is that I can choose the key I want! Bob: You mean 2048 bits, right? Alice: What? Bob: […]

If you find the key, use for unzip the flag.zip
```

## Provided Files
```
DatosdelReto.txt
flag.rar
```

## Writeups

Starting off I took a look at the file. <br/>
```
Challenge data

g = 173247436685893593416376928
p = 271046059989500989696377226
gA = 182351711645430656964122520
gB = 60508729390849113619409504

s = ?

password = pow(s, 4)
```

Looking at this I can instantly detect that this is a `diffie-hellman key exchange`. <br/>

I knew this because `diffie-hellman` exists of 2 public keys from `Alice` and `Bob` and also 1 prime number and 1 public parameter. Like stated in the descrption the 2 names are used. <br/>

Having all 4 parameters I can use them to bruteforce the shared key `s`. <br/>
```py
g = 173247436685893593416376928
p = 271046059989500989696377226
gA = 182351711645430656964122520
gB = 60508729390849113619409504

for b in range(1, p):
    if pow(g, b, p) == gA:
        s = pow(gB, b, p)
        print("Shared Secret (s):", s)
        break
```

Executing it: <br/>
```sh
kali@kali python3 yeet.py   
Shared Secret (s): 7544979023975407849055044
```

Using another 2 lines of python code to calculate the password: <br/>
```py
s = 7544979023975407849055044

password = pow(s, 4)

print(password)
```

Getting the password: <br/>
```sh
kali@kali python3 solve.py
3240650137482137399900530458075287208982259303962493588298898898116706676976752352360865234008228096
```

Using the password to unzip the `.rar`: <br/>
```sh
kali@kali unrar x flag.rar                            


UNRAR 6.21 freeware      Copyright (c) 1993-2023 Alexander Roshal


Extracting from flag.rar

Enter password (will not be echoed) for flag.txt: 

Extracting  flag.txt                                                  OK 
All OK
```

Getting the flag: <br/>
```sh
cat flag.txt
flag{DiffieHelman%RocksAlsoAlice&Bob} 
```

This concludes the challenge. 