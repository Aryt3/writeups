# Never gonna let you crypto

## Description
```
You read the title and thought Blockchain? You were successfully baited. 
Like the people before you, you now have to solve this challenge.
```

## Provided Files
```
- chall.py
- FLAG.enc
```

## Writeup

Starting off, I analyzed the `chall.py` file. <br/>
```py
import os
def encrypt(message,key):
    message = message.encode()
    out = []
    for i in range(len(message)):
        out+= [message[i]^key[i%len(key)]]
    return bytes(out).hex()
FLAG = "GPNCTF{fake_flag}"
key = os.urandom(5)

print(encrypt(FLAG,key))
```

Now this looks more complicated than it really is, so let's simplify. <br/>
```py
import os
def encrypt(message,key):
    message = message.encode() # Encoded GPNCTF{...}
    out = []
    for i in range(len(message)):

        out+= [message[i] ^ key[i%5]] # len(key) -> 5      (os.urandom(5))

    return bytes(out).hex()

FLAG = "GPNCTF{fake_flag}"
key = os.urandom(5)

print(encrypt(FLAG,key))
```

The crucial thing to notice here is the `XOR` operation between single characters of the flag (message[i]) and single parts of the key (key[i%5]). <br/>
The result which we get is also a simple encoded array with numbers. <br/>
```py
enc_flag = 'd24fe00395d364e12ea4ca4b9f2da4ca6f9a24b2ca729a399efb2cd873b3ca7d9d1fb3a66a9b73a5b43e8f3d'

decoded_list = [byte for byte in bytes.fromhex(enc_flag)]

print(decoded_list)
```
The result of this decoding can be seen below. <br/>
```py
[210, 79, 224, 3, 149, 211, 100, 225, 46, 164, 202, 75, 159, 45, 164, 202, 111, 154, 36, 178, 202, 114, 154, 57, 158, 251, 44, 216, 115, 179, 202, 125, 157, 31, 179, 166, 106, 155, 115, 165, 180, 62, 143, 61]
```

Knowing that these numbers are the results of the `XOR` operations we can setup simple equations for the first characters which we know. <br/>
```py
# res_0 = base_0 ^ key_0
# 210 = ord('G') ^ key_0
key_0 = 210 ^ 71 # ord('G') -> 71  -- Decimal Number for ASCII char 'G'  
```

Using the known prefix we can use the first 5 known characters to reverse the key which is only 5 bytes in length (os.urandom(5)). <br/>

I put all of this together into a single script. <br/>
```py
# Encrypted Flag
enc_flag = 'd24fe00395d364e12ea4ca4b9f2da4ca6f9a24b2ca729a399efb2cd873b3ca7d9d1fb3a66a9b73a5b43e8f3d'

# Key is only 5 bytes in size so we dont need more of the prefix GPNCTF{
FLAG_PREFIX = 'GPNCT' 

dec_enc_flag = bytes.fromhex(enc_flag)

# Decode array from encoded bytes
decoded_list = [byte for byte in dec_enc_flag]

# Derive the key from known Flag-Prefix GPNCTF{ using XOR on the known result(decoded array above) and base(decimal value of G,P,N,C,T)
key = [a ^ b for a, b in zip([ord(i) for i in FLAG_PREFIX], [i for i in decoded_list[:5]])]

# Reverse-XOR Operations to derive the decimal values of the original flag
flag_digits = [a ^ key[b] for a, b in zip(decoded_list,[i % 5 for i in range(0, int(len(enc_flag) / 2))])]

# Convert Numbers to ASCII-Characters/Letters
flag = [chr(i) for i in flag_digits]

# Print flag parsed together from above array
print("".join(flag))
```

Executing the script returns `GPNCTF{One_T1me_p4ds_m4y_n3v3r_b3_r3u53d!!!}` which concludes this writeup.