# nanoRSA

## Description
```
Where can I get a nanocomputer...
```

## Provided Files
`rsa.txt`

## Writeup

I started off by taking a look at the provided file. <br/>
```
e = 1
c = 9908255308151638808626355523286556242109836830117153917
n = 245841236512478852752909734912575581815967630033049838269083
```

Now this RSA is completely insecure because our exponent has the lowest value possible. <br/>
This results in us being able to decrypt the plaintext pretty easily. <br/>
I wrote a small python script for this purpose. <br/>
```py
e = 1
c = 9908255308151638808626355523286556242109836830117153917
n = 245841236512478852752909734912575581815967630033049838269083

# calculating message
m = c % n

# convert to bytes and deocde the flag
flag = m.to_bytes((m.bit_length() + 7) // 8, 'big').decode()

print(flag)
```

Executing the script I obtained the flag which concludes this writeup. 
```sh
kali@kali python3 nanorsa.py

grodno{R3sTcD4gH6iJ0kL}
```
