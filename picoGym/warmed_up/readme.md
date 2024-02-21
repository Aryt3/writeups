# Warmed Up

## Description
```
What is 0x3D (base 16) in decimal (base 10)?
```

## Writeup

Starting off, we can simply convert the hexadecimal value `0x3D` to a decimal integer using python. <br/>
```sh
$ python3
Python 3.11.6 (main, Nov 14 2023, 09:36:21) [GCC 13.2.1 20230801] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print(int('0x3D', 16))
61
```

Enclosing the result `61` within the flag format we get the actual flag `picoCTF{61}` which concludes this writeup. 