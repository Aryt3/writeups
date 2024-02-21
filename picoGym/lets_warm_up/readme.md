# Lets Warm Up

## Description
```
If I told you a word started with 0x70 in hexadecimal, what would it start with in ASCII? 
```

## Writeup

Starting off, we can simply convert the hexadecimal value `0x70` to ASCII using python. <br/>
```sh
$ python3
Python 3.11.6 (main, Nov 14 2023, 09:36:21) [GCC 13.2.1 20230801] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> chr(0x70)
'p'
```

Using `python` to convert it we get the `ASCII character` paired to the `hexadecimal` value. <br/>
Enclosing it within the flag format we get the actual flag `picoCTF{p}` which concludes this writeup. 