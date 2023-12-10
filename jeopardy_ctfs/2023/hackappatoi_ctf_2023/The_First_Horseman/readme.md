# The First Horseman

## Description
```
I don’t think you’re welcome inside this castle… SHISH!
```

## Provided Files
`thefirsthorseman38.pyc`

## Writeup

Starting off I decompiled the compiled python script using an online decompiler. (https://www.toolnb.com/tools-lang-en/pyc.html) <br/>
This gave me the following code: <br/>
```py
# uncompyle6 version 3.5.0
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.7.2 (default, Dec 29 2018, 06:19:36) 
# [GCC 7.3.0]
# Embedded file name: ../thefirsthorseman.py
# Size of source mod 2**32: 2794 bytes
from time import sleep
import codecs
print("You've inserted the key you found on the mysterious Laptop and you've been teleported to a place you don't know.")
print('All you can see is an enormous door keeping a castle safe. You approach it and with a bit of fear proceed to open it.')
print('In the middle of the hall you see a funny man, it seems the court jester, but still he scares you.')
print("'SHISH, SHISH' is the only thing he says, and now you realize he is the first horseman, ready to stop you from reaching further in your mission.")
print('The man walks towards you and tries to hit you multiple times! Avoid his punches!\n')

def shish():
    exit("The funny man manages to hit you. You fall on the ground.\nYou don't remember anything. All you know now is a word...\nSHISH\n")


f = ['r3st', '4s_a', 'b3_c', 'm4tt', 'l3t_']
l = ['4ll0', '30_1', '7t3_', 'jkin', 'p1ck']
a = ['5_th', '3_4n', '1t_1', '00p5', '1n_1']
g = ['p1_7', '3_w0', 't0g3', '00_k', 'n0th']
s = ['ear5', 'k!1!', '1n6!', '33p5', 'rd_!']
counter = 0
indexes = []

def print_flag():
    flag = ''
    flag += f[indexes[0]]
    flag += l[indexes[1]]
    flag += a[indexes[2]]
    flag += g[indexes[3]]
    flag += s[indexes[4]]
    flag = 'upgs{' + flag + '}'
    flag = codecs.encode(flag, 'rot13')
    print(flag)


try:
    for t in range(1, 6):
        print(f"{t}...")
        counter = t
        sleep(1)

    shish()
except KeyboardInterrupt:
    if counter == 4:
        print('\nYou dodged it\n')
        indexes.append(counter - 1)
    else:
        shish()

try:
    for t in range(1, 6):
        print(f"{t}...")
        counter = t
        sleep(1)

    shish()
except KeyboardInterrupt:
    if counter == 2:
        print('\nYou dodged it\n')
        indexes.append(counter - 1)
    else:
        shish()

try:
    for t in range(1, 6):
        print(f"{t}...")
        counter = t
        sleep(1)

    shish()
except KeyboardInterrupt:
    if counter == 1:
        print('\nYou dodged it\n')
        indexes.append(counter - 1)
    else:
        shish()

try:
    for t in range(1, 6):
        print(f"{t}...")
        counter = t
        sleep(1)

    shish()
except KeyboardInterrupt:
    if counter == 2:
        print('\nYou dodged it\n')
        indexes.append(counter - 1)
    else:
        shish()
else:
    try:
        for t in range(1, 6):
            print(f"{t}...")
            counter = t
            sleep(1)

        shish()
    except KeyboardInterrupt:
        if counter == 5:
            print('\nYou dodged it\n')
            indexes.append(counter - 1)
        else:
            shish()
    else:
        print('The man is tired, he just hands you a slip of paper, to open the next door.\nThis is what you read')
        print_flag()
        print("The man then says his last words...\n 'https://youtu.be/XH0CSzdHwg0?si=DOwRhOnorrc-WWIx'")
```

Taking a look at the file I saw that we basically have pieces of the flag which when put together in the correct order would give us the flag. <br/>
Knowing this I wrote a small script to solve it. <br/>
```py
import codecs

f = ['r3st', '4s_a', 'b3_c', 'm4tt', 'l3t_']
l = ['4ll0', '30_1', '7t3_', 'jkin', 'p1ck']
a = ['5_th', '3_4n', '1t_1', '00p5', '1n_1']
g = ['p1_7', '3_w0', 't0g3', '00_k', 'n0th']
s = ['ear5', 'k!1!', '1n6!', '33p5', 'rd_!']

indexes = []  

def print_flag():
    flag = ''
    flag += f[indexes[0]]
    flag += l[indexes[1]]
    flag += a[indexes[2]]
    flag += g[indexes[3]]
    flag += s[indexes[4]]
    flag = 'upgs{' + flag + '}'
    flag = codecs.encode(flag, 'rot13')
    return flag

indexes.append(3)
indexes.append(1)
indexes.append(0)
indexes.append(1)
indexes.append(4)

print(print_flag())
```

Executing this we get the flag `hctf{z4gg30_15_gu3_j0eq_!}` which concludes this challenge. 














