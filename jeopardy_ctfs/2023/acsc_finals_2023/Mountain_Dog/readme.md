# Mountain Dog

## Introduction
```
Welcome to the "Mountain Dog" challenge!
```

## Goal
```
The "Mountain Dog" challenge aims at what a dog is up to.
```

## Task
```
To begin the challenge, follow these steps:
Download the provided video file from the given resources.
Find out what the dog is up to and get the flag
```

Flag
```
HL{FLAG}
```

## Note 
```
characters are smallcase
```

## Writeup

Starting off I download the .mp4 and take a look at it. <br/>
```sh
kali@kali file mountain-dog.mp4      
mountain-dog.mp4: ISO Media, MP4 Base Media v1 [ISO 14496-12:2003]

kali@kali binwalk -e mountain-dog.mp4
-----------------------------------------

kali@kali ls -la _mountain-dog.mp4.extracted/
total 2380
drwxr-xr-x 2 root root    4096 Oct  2 17:27 .
drwxr-xr-x 3 root root    4096 Oct  2 20:45 ..
-rw-r--r-- 1 root root 1016811 Jul 17 23:25 dog.gif
-rw-r--r-- 1 root root  956989 Oct  2 17:26 dog.jpg
-rw-r--r-- 1 root root  447371 Jul 17 23:29 mountain.png
```

This extracts some data from the image. Inside we find another three images. <br/>
After doing some analysis on the images I came up with nothign so I took another look at them in an image viewer. <br/>
![dog](https://github.com/Aryt3/writeups/assets/110562298/08c2bbd7-fd65-49c5-8d58-067a6161be7c)

Seems like they put a QR code into the image. Scanning it we get the output below. <br/>
```
https://qrx.codes/ckuu31
```

Visiting the website we get an interesting word `CompetitiveKnightWalks55`. <br/>
I also found a password protected `.rar` file in a subfolder of the extracted `mountain_dog.mp4`. <br/>
Knowing this I tried to use the word above as a password after getting a negative response I remembered that characters should be smallcase as stated in the description, so I changed the phrase to `competitiveknightwalks55` and got the contents of the `.rar`. <br/>
```sh
kali@kali ls -la source               
total 1012
drwxr-xr-x 2 root root    4096 Sep 18 17:33 .
drwxr-xr-x 4 root root    4096 Nov 16 22:32 ..
-rw-r--r-- 1 root root 1016811 Jul 17 23:25 dog.gif
-rw-r--r-- 1 root root    1689 Jul 17 23:28 index.html
-rw-r--r-- 1 root root      40 Jul 17 23:32 logo.png
```

Analysing them I found that `logo.png` was kind of strange. <br/>
```sh
kali@kali file logo.png        
logo.png: ASCII text, with no line terminators

kali@kali strings logo.png             
SEx7MDBfd2hvX2xldF90aGVfZG9nc19vdXRfMDB9
```

After getting this string which oddly looked like base64 encoded data I tried to deocde it. <br/>
```sh
kali@kali echo "SEx7MDBfd2hvX2xldF90aGVfZG9nc19vdXRfMDB9" | base64 -d  
HL{00_who_let_the_dogs_out_00}
```

Seems like I found the flag.






