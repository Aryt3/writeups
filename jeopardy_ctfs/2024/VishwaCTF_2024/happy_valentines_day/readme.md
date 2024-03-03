# Happy Valentine's Day

## Description
```
My girlfriend and I captured our best moments of Valentine's Day in a portable graphics network. 
But unfortunately I am not able to open it as I accidentally ended up encrypting it. 
Can you help me get my memories back?
```

## Provided Files
```
- source.txt
- enc.txt
```

## Writeup

Taking a look at the encrypted image I couldn't display it because the encrypted seems to have corrupted it. <br/>
```py
from PIL import Image
from itertools import cycle

def xor(a, b):
    return [i^j for i, j in zip(a, cycle(b))]

f = open("original.png", "rb").read()
key = [f[0], f[1], f[2], f[3], f[4], f[5], f[6], f[7]]

enc = bytearray(xor(f,key))

open('enc.txt', 'wb').write(enc)
```

The code above seems to use the `file-header` of a file which are the first few bytes of a file as the key to encrypt the image. <br/>
Knowing this I used a normal `.png` file to replicate the key. <br/>
```py
f = open("test.png", "rb").read()
key = [f[0], f[1], f[2], f[3], f[4], f[5], f[6], f[7]]

print(key)
```

Getting the key: <br/>
```sh
$ python3 key.py

[137, 80, 78, 71, 13, 10, 26, 10]
```

Using the key to decrypt the ecnrypted image I made another small script to reverse the encryption. <br/>
```py
from itertools import cycle

def xor(a, b):
    return [i ^ j for i, j in zip(a, cycle(b))]

enc = open("enc.txt", "rb").read()

key = [137, 80, 78, 71, 13, 10, 26, 10]

dec = bytearray(xor(enc, key))

open('decrypted.png', 'wb').write(dec)
```

Executing the script with the key I was able to reverse the encrypted image. <br/>
[IMAGE]()

Looking at the decrypted image I obtained the flag which concludes this writeup.