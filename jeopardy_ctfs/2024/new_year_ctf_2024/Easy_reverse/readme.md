# Easy reverse

## Description
```
Nothing special

Flag in format: grodno{text}
```

## Provided Files
`easy_reverse`

## Writeup

Using my own workflow for file analysis I start off with a `strings` on the file. <br/>
```sh
kali@kali strings easy_reverse

-------------------------------
D0nT_st0r3_str1nGs_1n_pla1nt3xt
-------------------------------
```

Between everything else I found this suspicous string. <br/>
Combing the string with flag prefix we obtain `grodno{D0nT_st0r3_str1nGs_1n_pla1nt3xt}` which concludes this writeup. 