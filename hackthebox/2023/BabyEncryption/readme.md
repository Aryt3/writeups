# BabyEncryption

## Description
```
You are after an organised crime group which is responsible for the illegal weapon market in your country. 
As a secret agent, you have infiltrated the group enough to be included in meetings with clients. 
During the last negotiation, you found one of the confidential messages for the customer. 
It contains crucial information about the delivery. Do you think you can decrypt it?
```

## Writeup

Starting off we get 2 files. <br/>
1 file for the encrypted flag and 1 file for the encryption method. <br/>

Encrypted flag: <br/>
```hex
6e0a9372ec49a3f6930ed8723f9df6f6720ed8d89dc4937222ec7214d89d1e0e352ce0aa6ec82bf622227bb70e7fb7352249b7d893c493d8539dec8fb7935d490e7f9d22ec89b7a322ec8fd80e7f8921
```

Python file for encryption
```py
import string
from secret import MSG

def encryption(msg):
    ct = []
    for char in msg:
        ct.append((123 * char + 18) % 256)
    return bytes(ct)

ct = encryption(MSG)

f = open('./msg.enc','w')
f.write(ct.hex())
f.close()
```

Taking a look at the python file we just need to reverse/inverse the encryption function. <br/>
For this purpose we can write a little script ourselves. <br/>
```py
f = open("msg.enc", "r")
line = f.readlines()
f.close()

enc_msg = line[0].strip()

ct = bytes.fromhex(enc_msg)

def decryption(ct):
    msg = []
    for char in ct:
        inverse = pow(123, -1, 256)
        msg.append((inverse * (char - 18)) % 256)
    return bytes(msg)

decrypted_message = decryption(ct)

print(decrypted_message.decode("utf-8"))
```

This Python script decryptes the encrypted message and returns to us the flag. <br/>
```sh
kali@kali python3 .\decrypter.py
Th3 nucl34r w1ll 4rr1v3 0n fr1d4y.
HTB{REDACTED}
```

