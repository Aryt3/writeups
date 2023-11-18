# An Invincible Summer

## Description
```
I seem to have misplaced the flag for this challenge. I know that it's in one of these files. I just can't remember which one... And why would I have two copies of each image in different formats... I swear, I'd forget my head if I didn't have SQL constantly orbiting it.

Archive password: poctf2023

HINT: This challenge is giving a lot of people trouble. I've double checked everything, and I can unequivocally say it's all picsel perfect. 
```

## Provided Files
`stego1.7z`

## Writeup

Starting off I unziped the provided archive and got the following files:
```sh
kali@kali ls -la       
total 21764
drwxr-xr-x  2 root root    4096 Nov 18 22:41  .
drwxr-xr-x 22 kali kali    4096 Nov 18 22:41  ..
-rw-r--r--  1 root root 2131654 Nov 27  2020  CD.bmp
-rw-r--r--  1 root root   79010 Nov 27  2020  CD.jpg
-rw-r--r--  1 root root 1960054 Nov 27  2020  bat.bmp
-rw-r--r--  1 root root  156546 Nov 27  2020  bat.png
-rw-r--r--  1 root root     247 Nov 27  2020  boi.txt
-rw-r--r--  1 root root  736710 Nov 27  2020  casette.bmp
-rw-r--r--  1 root root   37808 Nov 27  2020  casette.jpg
-rw-r--r--  1 root root 1569846 Nov 27  2020  hand.bmp
-rw-r--r--  1 root root   36078 Nov 27  2020  hand.jpg
-rw-r--r--  1 root root  827790 Nov 27  2020  key.bmp
-rw-r--r--  1 root root   42766 Nov 27  2020  key.jpg
-rw-r--r--  1 root root 1000054 Nov 27  2020  lock.bmp
-rw-r--r--  1 root root  207739 Nov 27  2020  lock.png
-rw-r--r--  1 root root  432054 Nov 27  2020  mittens.bmp
-rw-r--r--  1 root root   37595 Nov 27  2020  mittens.jpg
-rw-r--r--  1 root root 1821654 Nov 27  2020  rug.bmp
-rw-r--r--  1 root root  257636 Nov 27  2020  rug.jpg
-rw-r--r--  1 root root 1057974 Nov 27  2020  tapochki.bmp
-rw-r--r--  1 root root   77652 Nov 27  2020  tapochki.jpg
-rw-r--r--  1 root root 3984054 Nov 27  2020  vhs.bmp
-rw-r--r--  1 root root   83026 Nov 27  2020  vhs.jpg
-rw-r--r--  1 root root  571254 Nov 27  2020  walkman.bmp
-rw-r--r--  1 root root   35550 Nov 27  2020  walkman.jpg
```

After taking a look at the files and analysing them I couldn't find anything. <br/>
I did some research and came up with a Stegnography Tool. (https://www.ssuiteoffice.com/software/ssuitepicselsecurity.htm) <br/>
Using the Tool I entered every picture until I found the correct one. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/a41cbbeb-68ac-4d90-91cc-2d07faddabc0)

Like this I was able to obtain the flag. 

