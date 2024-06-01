# Shattered Memories

## Description
```
I swear I knew what the flag was but I can't seem to remember it anymore... can you dig it out from my inner psyche?
```

## Provided Files
`shattered-memories`

## Writeup

I started off by doing a `strings` into the file. <br/>
```
kali@kali strings shattered-memories

-------------
t_what_f
t_means}
nd_forge
lactf{no
orgive_a
-------------
```

Finding these pieces I was able to determine the order pretty quickly. <br/>
```
lactf{no
t_what_f
orgive_a
nd_forge
t_means}
```

Putting this together I obtained `lactf{not_what_forgive_and_forget_means}` which concludes this writeup. 
