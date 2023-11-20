# If You Don't, Remember Me

## Description
```
Here is a PDF file that seems to have some problems. 
I'm not sure what it used to be, but that's not important. 
I know it contains the flag, but I'm sure you can find it and drag it out of the file somehow. 
This is a two-step flag as you will find it partially encoded.
```

## Provided Files
`DF1.pdf`

## Writeup

Starting off I do a strings on the file. <br/>
```sh
kali@kali strings DF1.pdf
---------------------------------------------------
poctf(uwsp_77333163306D335F37305F3768335F39346D33} 
```

Doesn't seem to be our flag yet. <br/>
Inputing `77333163306D335F37305F3768335F39346D33` into CyberChef I use the magic module. <br/>
Seems like magic module found a match `From Hex` giving us `w31c0m3_70_7h3_94m3`. <br/>
Using this we build the flag `poctf{uwsp_w31c0m3_70_7h3_94m3}`.
