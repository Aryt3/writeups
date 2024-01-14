# Traffic Check

## Description
```
We received a traffic dump in which someone transmitted an unprotected password.

Flag in the format grodno{password}
```

## Provided Files
`traffic.pcapng`

## Writeup

Before using a tool to analyze the pcapng file like wireshark I did a simple `strings` on the file. <br/>
```sh
kali@kali strings traffic.pcapng | grep grodno

username=easy_login&password=grodno%7Be@sy_p@ckages_ch3ck%7D  
```

Seeing this I knew it was URL encoding, decoding it we obtain the actual flag `grodno{e@sy_p@ckages_ch3ck}` which concludes this writeup. 