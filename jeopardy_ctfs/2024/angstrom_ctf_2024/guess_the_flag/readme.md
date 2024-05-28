# Guess the flag

## Description
```
Do you have what it takes to guess the flag? Find out here!
```

## Provided Files
```
- guess_the_flag
```

## Writeup

Starting off, I used simple linux utility to inspect the file. <br/>
```sh
$ strings guess_the_flag
/lib64/ld-linux-x86-64.so.2

-----

Go ahead, guess the flag: 
Correct! It was kinda obvious tbh.
Wrong. Not sure why you'd think it'd be that.
:*3$"
`bugzbnllhuude^un^uid^md`ru^rhfohghb`ou^chu|

-----
```

Seeing the strange string above I thought that it may be the encoded-hardcoded flag.

Using [CyberChef](https://gchq.github.io/CyberChef/#recipe=XOR_Brute_Force(1,100,0,'Standard',false,true,false,'')&input=YGJ1Z3pibmxsaHV1ZGVedW5edWlkXm1kYHJ1XnJoZm9oZ2hiYG91XmNodXw&oeol=VT) I was able to retrieve the flag as it was just a simple `XOR-Shift`.