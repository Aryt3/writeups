# A Pale, Violet Light

## Provided resources:
```
e= 5039

N = 34034827

C = 933969 15848125 24252056 5387227 5511551 10881790 3267174 14500698 28242580 933969 32093017 18035208 2594090 2594090 9122397 21290815 15930721 4502231 5173234 21290815 23241728 2594090 21290815 18035208 10891227 15930721 202434 202434 21290815 5511551 202434 4502231 5173234 25243036
```

## Writeup

Seems like we got some components of RSA. <br/>
| Component | Description |
| :-------: | :---------: |
| e | modulus (product of primenumbers p & q) |
| N | public exponent (part of the public-key) |
| C | ciphertexts |

Having `e` and `N` we are able to decrypt `C`. <br/>

Knowing this I found a stack overflow post which helped me find a tool to decrypt. <br/>
Source: https://stackoverflow.com/questions/49878381/rsa-decryption-using-only-n-e-and-c <br/>

Having this information I wrote a small script to automate the decryption process. <br/>
```sh
#!/bin/bash

while IFS= read -r line; do
        python3 RsaCtfTool.py -n 34034827 -e 5039 --decrypt $line
done < "encrypted.txt"
```

the `encrypted.txt` file content: <br/>
```txt
933969
15848125
24252056
5387227
5511551
10881790
3267174
14500698
28242580
933969
32093017
18035208
2594090
2594090
9122397
21290815
15930721
4502231
5173234
21290815
23241728
2594090
21290815
18035208
10891227
15930721
202434
202434
21290815
5511551
202434
4502231
5173234
25243036
```

Executing the script: <br/>
```sh
kali@kali bash solver.sh > output.txt
[!] Using native python functions for math, which is slow. install gmpy2 with: 'python3 -m pip install <module>'.
private argument is not set, the private key will not be displayed, even if recovered.

[*] Testing key /tmp/tmp0rtjh1bk.
[*] Performing smallq attack on /tmp/tmp0rtjh1bk.
[*] Attack success with smallq method !

Results for /tmp/tmp0rtjh1bk:

Decrypted data :
HEX : 0x00000070
INT (big endian) : 112
INT (little endian) : 1879048192
utf-8 : p
utf-16 : 瀀
STR : b'\x00\x00\x00p'
[!] Using native python functions for math, which is slow. install gmpy2 with: 'python3 -m pip install <module>'.
private argument is not set, the private key will not be displayed, even if recovered.

[*] Testing key /tmp/tmp66x_vnpw.
[*] Performing smallq attack on /tmp/tmp66x_vnpw.
[*] Attack success with smallq method !

Results for /tmp/tmp66x_vnpw:

Decrypted data :
HEX : 0x0000006f
INT (big endian) : 111
INT (little endian) : 1862270976
utf-8 : o
utf-16 : 漀
STR : b'\x00\x00\x00o'
[!] Using native python functions for math, which is slow. install gmpy2 with: 'python3 -m pip install <module>'.
private argument is not set, the private key will not be displayed, even if recovered.
```

Seems like we got each letter 1 for 1. <br/>
Knowing this I grep for the letters .<br/>
```sh
kali@kali cat output.txt | grep utf-8
utf-8 : p
utf-8 : o
utf-8 : c
utf-8 : t
utf-8 : f
utf-8 : {
utf-8 : u
utf-8 : w
utf-8 : s
utf-8 : p
utf-8 : _
utf-8 : 5
utf-8 : 3
utf-8 : 3
utf-8 : k
utf-8 :  
utf-8 : 4
utf-8 : n
utf-8 : d
utf-8 :  
utf-8 : y
utf-8 : 3
utf-8 :  
utf-8 : 5
utf-8 : h
utf-8 : 4
utf-8 : 1
utf-8 : 1
utf-8 :  
utf-8 : f
utf-8 : 1
utf-8 : n
utf-8 : d
utf-8 : }
```

Than I use regular expressiosn to compress the flag. <br/>
First regex `'utf-8 : '`, second regex `'\n'`. <br/>
Using those we receive `poctf{uwsp_533k 4nd y3 5h411 f1nd}`. <br/>
Seems like it didn't get every underscore. Changing the flag to `poctf{REDACTED}` ends this challenge. <br/>


