# Keyboard Cipher

## Description
```
I designed an algorithm to encrypt a message using my keyboard. No one can decrypt it without any information about my algorithm. Note: Wrap the flag in TUCTF{}.
```

## Provided Files
`keyboard_cipher.enc`

## Writeup

I start off by taking a look at the content of the provided file. <br/>
```
0x636a56355279424b615464354946686b566942794e586c4849455279523359674d47394d49486845643045675a316b315569426163304d675a316c715469426163314567616b6c7354534268563252594947745063434178643045675332395149466c6e536d343d
```

It appears we got a rather large `hex` string. I used CyberChef to decrypt. <br/>
```
cjV5RyBKaTd5IFhkViByNXlHIERyR3YgMG9MIHhEd0EgZ1k1UiBac0MgZ1lqTiBac1EgaklsTSBhV2RYIGtPcCAxd0EgS29QIFlnSm4=
```

Seems like we extracted a `base64` encoded string. I again used CyberChef to decode it. <br/>
```
r5yG Ji7y XdV r5yG DrGv 0oL xDwA gY5R ZsC gYjN ZsQ jIlM aWdX kOp 1wA KoP YgJn
```

I couldn't decrypt further because this was no known encryption. Knowing this I took a look at the english keyboard layout. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/4bde16d1-3912-4422-9470-544c6ad4e102)

To make some sense I tried to connect all the different keys. (Please don't hate my shaky drawings)<br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/95abce5b-c78e-4def-87e9-82469219cdbb)

Strangely I saw that all of the connections were creating geometrical shapes which were kind of surrounding other letters. <br/>
Seeing that I wrote down the letters which were encircled. This gave me the following output:
```
T U C T F P S T X H A K S L Q L H
```

Knowing that the flag-format was `TUCTF` I assumed that I found the actual flag. <br/>
Using the instructions I got the flag `TUCTF{PSTXHAKSLQLH}` which concluded this challenge.


