# ᒣ⍑╎ϟ ╎ϟ リᒷᖋᒣ

## Description
```
We have reason to believe that Mortimer is rebuilding the Armageddon Machine. 
We managed to intercept a message sent from his personal computer. 
After consulting with the Oracle, we were only able to discover two things:

The tool used to encrypt messages (encrypt.py)
All messages sent by Mortimer begin with Mortimer_McMire:

Can you decrypt the message?
```

## Provided Files
```
- encrypt.py
- message.enc
```

## Writeup

Looking at `encrypt.py` we can see the encryption used for the plaintext. <br/>
```py
from Crypto.Cipher import AES
import binascii, os

key = b"3153153153153153"
iv =  os.urandom(16)

plaintext = open('message.txt', 'rb').read().strip()

cipher = AES.new(key, AES.MODE_CBC, iv)

encrypted_flag = open('message.enc', 'wb')
encrypted_flag.write(binascii.hexlify(cipher.encrypt(plaintext)))
encrypted_flag.close()
```

`message.enc` contains the output of `encrypt.py`. <br/>
```
2a21c725b4c3a33f151be9dc694cb1cfd06ef74a3eccbf28e506bf22e8346998952895b6b35c8faa68fac52ed796694f62840c51884666321004535834dd16b1
```

To get the flag we actually already have everything we need. <br/>
- `key` - Key used for encryption and decryption, `b'3153153153153153'`.
- `iv` - Initialization vector used for encryption algorithm (first 16 bytes of ciphertext), `b'2a21c725b4c3a33f'`.
- `ciphertext` - Ciphertext containg the flag `151be9dc694cb1cfd06ef74a3eccbf28e506bf22e8346998952895b6b35c8faa68fac52ed796694f62840c51884666321004535834dd16b1`. 

Putting these things together in a solution script: <br/>
```py
from Crypto.Cipher import AES
import binascii

key = b"3153153153153153"

with open('message.enc', 'rb') as file:
    hex_data = file.read()

cipher_text_bytes = binascii.unhexlify(hex_data)

iv = cipher_text_bytes[:16]  # IV is first 16 bytes of ciphertext
cipher_text = cipher_text_bytes[16:]  # The rest is the actual ciphertext

cipher = AES.new(key, AES.MODE_CBC, iv)

plain_text = cipher.decrypt(cipher_text)

print(plain_text.decode('utf-8'))
```

Running the decryption script concludes this writeup. <br/>
```sh
$ python3 decrypt.py 
        shctf{th1s_was_ju5t_a_big_d1str4ction}
```