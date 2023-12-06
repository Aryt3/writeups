# A.R.K. 2

## Description
```
Woof woof bark bark (Note: to speed up the process, only include entries containing "dog" in your attempts)
```

## Provided Files
`woof`

## Writeup

Starting off with file analysis again. <br/>
```sh
file woof

woof: Keepass password database 2.x KDBX
```

Seems like the challenge is going to be similar to `A.R.K. 1`. <br/>
Knowing this I created a wordlist again and started cracking the file. <br/>
```sh
grep "dog" rockyou.txt > dog_wordlist.txt
keepass2john woof > converted_file
john --format=KeePass converted_file --wordlist=dog.txt
--------------------------------------------------------
john --show converted_file

woof:wholetthedogsout

1 password hash cracked, 0 left
```

Getting the password we haven't finished the challenge yet so I opened the file using `keepass2`. <br/>
```sh
keepass2 woof
```

Taking a look at the Recycle Bin:
![grafik](https://github.com/Aryt3/writeups/assets/110562298/793b3a4a-b5b8-454c-95c6-f4cbb8070c76)

Seems like we found the flag but the actual flag itself is not there. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/340f5bba-3460-4357-bea7-59023542b2b0)

Using the restore function we found the flag. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/1242b5be-46c6-4b86-bb86-89bdc209b10d)

Finding the flag `TUCTF{K3eP_M4_Pa$s_rE4L_SaF3}` we finish this challenge. 












