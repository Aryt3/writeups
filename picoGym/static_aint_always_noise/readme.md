# Static ain't always noise

## Description
```
Can you look at the data in this binary: static? This BASH script might help!
```

## Provided Files
```
- ltdis.sh
- static
```

## Writeup

Before taking a look at the `bash` script we should try to do simple analysis on a binary using linux utility. <br/>
Using the `strings` command we can take a look at strings found in the binary. <br/>
```sh
$ strings static 

--------------------------------

Oh hai! Wait what? A flag? Yes, it's around here somewhere!
;*3$"
picoCTF{d15a5m_t34s3r_ae0b3ef2}

--------------------------------
```

Looking at the output we can find the flag which concludes this writeup.