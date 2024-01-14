# Belarussian cipher 

## Description
```
“Кропка” is a “dot”, “працяжнiк” is a “dash”.

The rest is up to you)
```

## Provided Files
`bel_cipher.txt`

## Writeup

Taking a look at the provided file. <br/>
```
працяжнiк працяжнiк кропка ...
```

Seeing this and the having read the description I replaced every `Кропка` with a `.` and every `працяжнiк` with a `-`. <br/>
```
- - . . . - . - - . - - - . - - - . . - - . . . - . . . - - . - - . . - . . . . - . . - - . - - - . . - . . . - - . . - . . . . - . . . . - . . - . - - - . - - - - . . - - - - - . . - . . . - - - . - - . . . - . . . - . - - - . - . . . . . - . . - - - . - - . . - - . - . - . . - . . - - - - . . - - - . - . . - - . - . - . . . - . . - - . . - - . - . - . - . . . . . - . . . . - - . - . . - . . . . - . . . - . - . - . . . - - . - - . - . . . . . - . . - - . - . - . . . . - - . - . . - - . - . - . . . - - . . - - . - - - - . - . - . . . . . - . - . - . - - - . . - . - - - - - . . - - . . - . . . . - - . - . - . . . . . - - . . - - - - - . . - . . . - - . . - . . - - - . . . . - - . - . - . . . . . - . . . - - . . - . . - - . - . - . . - - . - . - . - . . . . . - . . - . . . . - . . - - - . - - . . . - - . . - . . . - . - - - - . . - . - - - . . - - - . . - . . - . . - - - . . - - . - . - . . . - - . . - . . . . . - . - . - . . . . - - - . - . - - .
```

Now this awfully looks like morsecode. <br/>
Decoding the morse code in CyberChef. <br/>
```
TTEEETETTETTTETTTEETTEEETEEETTETTEETEEEETEETTETTTEETEEETTEETEEEETEEEETEETETTTETTTTEETTTTTEETEEETTTETTEEETEEETETTTETEEEEETEETTTETTEETTETETEETEETTTTEETTTETEETTETETEEETEETTEETTETETETEEEEETEEEETTETEETEEEETEEETETETEEETTETTETEEEEETEETTETETEEEETTETEETTETETEEETTEETTETTTTETETEEEEETETETETTTEETETTTTTEETTEETEEEETTETETEEEEETTEETTTTTEETEEETTEETEETTTEEEETTETETEEEEETEEETTEETEETTETETEETTETETETEEEEETEETEEEETEETTTETTEEETTEETEEETETTTTEETETTTEETTTEETEETEETTTEETTETETEEETTEETEEEEETETETEEEETTTETETTE
```

Now having only 2 characters again I assumed this is probably binary. <br/>
Knowing this I write a small python script to convert binary to asci characters. <br/>
```py
def binary_to_ascii(binary_string):
    eight_bit_chunks = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]

    ascii_characters = ''.join([chr(int(chunk, 2)) for chunk in eight_bit_chunks])

    return ascii_characters

for line in open('version_01.txt', 'r'):
    print(binary_to_ascii(line))
```

Executing the script gives us interesting results. <br/>
```sh
kali@kali python3 solve.py

:Dgrodno{D0n't_bel1eve_your_eyes!_Th3y_0nly_see_obst4cles}^)
```

Obtaining the flag `grodno{D0n't_bel1eve_your_eyes!_Th3y_0nly_see_obst4cles}` concludes this challenge.