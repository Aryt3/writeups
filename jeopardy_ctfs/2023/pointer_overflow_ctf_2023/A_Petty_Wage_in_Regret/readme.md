# A Petty Wage in Regret

## Description
```
Here is a very interesting image. 
The flag has been broken up into several parts and embedded within it, so it will take a variety of skills to assemble it. 
```

## Provided Files
`DF2.jpg` 

## Writeup

Starting again with a simple `strings` on the file. <br/>
```sh
kali@kali strings DF2.jpg
--------------------------------------------------------------------
3A3A50312F323A3A20706F6374667B757773705F3768335F7730726C645F683464
--------------------------------------------------------------------
```

Using the magic module again we recieve the first part of the flag `::P1/2:: poctf{uwsp_7h3_w0rld_h4d`.
Using the online stegonography tool https://www.aperisolve.com/ we can actually see that once you change the color of the image a bit you receive letters in the image. <br/>
Knowing this we can decipher the last piece of the flag `::P2/2::17:f1257`. <br/>
Trying some flags I was able to obtain the correct flag `poctf{REDACTED}`.
