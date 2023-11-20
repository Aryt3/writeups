# The Gentle Rocking of the Sun 

## Description
```
Here's a password protected archive. Problem is that I seem to have forgotten das Passwort. 
All I have is this post-it note on my monitor that says "crack2 = 4bd939ed2e01ed1e8540ed137763d73cd8590323"
```

## Provided Files
`crack2.7z`

## Writeup

Looking at the description I thought that the random string kind of looks like a hash. <br/>
Knowing this I used Crackstation to crack the hash. https://crackstation.net/ <br/>
Cracked Hash: `zwischen`. <br/>

Unpacking archive: <br/>
```sh
kali@kali 7z x ../../../Desktop/crack2.7z
-----------------------------------------------------------------
Enter password (will not be echoed):

Path = ./crack2.7z
Type = 7z
WARNINGS:
There are data after the end of archive
Physical Size = 398
Tail Size = 14120
Headers Size = 398
Solid = -
Blocks = 0

Everything is Ok

Archives with Warnings: 1

Warnings: 1
Folders: 26
Files: 0
Size:       0
Compressed: 14518
```

Getting the flag: <br/>
```sh
kali@kali  ls -laR crack2/         
-----------------------------------------------------------------

2023/p/o/c/t/f/{uwsp_/c/4/1/1/f/0/2/n/1/4_/d/2/3/4/m/1/n/9/}:
total 8
drwx------ 2 root root 4096 Jun  2 16:35 .
drwx------ 3 root root 4096 Jun  2 16:35 ..
```

Getting this string `p/o/c/t/f/{uwsp_/c/4/1/1/f/0/2/n/1/4_/d/2/3/4/m/1/n/9/}` we can use CyberChef to get the flag. <br/>
Using regular expression from `'/'` to `''` we obtain `poctf{uwsp_c411f02n14_d234m1n9}` which ends the challenge. 
