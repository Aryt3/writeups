# 2Warm

## Description
```
Can you convert the number 42 (base 10) to binary (base 2)? 
```

## Writeup

Starting off, we can simply convert the decimal integer `42` to binary using python. <br/>
```sh
$ python3
Python 3.11.6 (main, Nov 14 2023, 09:36:21) [GCC 13.2.1 20230801] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> '{0:b}'.format(42)
'101010'
```

Enclosing the result `101010` within the flag format we get the actual flag `picoCTF{101010}` which concludes this writeup. 