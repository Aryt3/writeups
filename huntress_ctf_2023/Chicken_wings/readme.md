# Chicken Wings

## Description
```
I ordered chicken wings at the local restaurant, but uh... this really isn't what I was expecting...
```

## Writeup

Starting this challenge we receive a file. <br/>
The first thing I do is uploading the file to CyberChef to detect certain things. <br/>
The content of the file seems to be `♐●♋♑❀♏📁🖮🖲📂♍♏⌛🖰♐🖮📂🖰📂🖰🖰♍📁🗏🖮🖰♌📂♍📁♋🗏♌♎♍🖲♏❝`. <br/>
Seems like CyberChef is not able to detect the encoding which was used.

Knowing this I switched to another deocding engine: https://www.dcode.fr/cipher-identifier. <br/>
Seems like the encoding used is `wingdings font`. Using the same website to decode the content of the file above we receive nothing. <br/>
Therefore I found another website to decode it: https://lingojam.com/WingdingsTranslator.

Using the website we are able to obtain the flag `flag{e0791ce68f718188c0378b1c0a3bdc9e}`.

