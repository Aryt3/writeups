# Mod 26

## Description
```
Cryptography can be easy, do you know what ROT13 is?

cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_uJdSftmh}
```

## Writeup

Starting off we are provided the string below. <br/>
```
cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_uJdSftmh}
```

Now to those who don't know `ROT13` is comparable to a simple `caesar cipher` shift. <br/>
It will simply shift every letter in your string `13` positions to the side. <br/>
Knowing this we can input the string into [CyberChef](https://cyberchef.org/#recipe=ROT13(true,true,false,13)&input=Y3ZwYlBHU3thcmtnX2d2enJfVid5eV9nZWxfMl9lYmhhcWZfYnNfZWJnMTNfdUpkU2Z0bWh9). <br/>
```
picoCTF{next_time_I'll_try_2_rounds_of_rot13_hWqFsgzu}
```

Doing this we obtain the flag which concludes this writeup.
