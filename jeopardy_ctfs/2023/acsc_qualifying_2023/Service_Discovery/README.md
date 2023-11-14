# Service Discovery

## Introduction
```
This challenge involves discovering a hidden service by following a series of clues. 
Your task is to use your problem-solving skills to uncover the location of the hidden service.
```

## Goal
```
You will be given a series of clues that will guide you toward the location of a hidden service. 
The clues will be in the form of riddles, puzzles, or other challenges that require creative thinking to solve.
```

## Task
```
Your task is to follow the clues and use your problem-solving skills to uncover the location of the hidden service. 
Once you have found the hidden service, you will need to submit the flag to complete the challenge.
```

## Hint
```
Find ports
```

## Writeup
With the hints we start scanning the ip for open ports: <br/>
```sh
kali@kali nmap 152.96.7.6 -p 1-1023
Starting Nmap 7.92 ( https: //nmap.org ) at 2023-05-23 04:39 EDT
Stats: 0:02:00 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 99.99% done; ETC: 04:41 (0:00:00 remaining)
Nmap scan report for 152.96.7.6
Host is up (0.094s latency).
Not shown: 1022 closed tcp ports (reset)

PORT STATE SERVICE
965/tcp open unknown

Nmap done: 1 IP address (1 host up) scanned in 121.97 seconds
```

Accessing the Port via browser: <br/>
![Untitled(1)](https://github.com/Aryt3/writeups/assets/110562298/fb4cafa1-7ede-48d9-9ecc-b398f8f54c81)

With the hint to scan the registered Port Range let's do that. <br/>
```sh
kali@kali nmap -p 1023-49151 -T4 152.96.7.6

Starting Nmap 7.92 ( https://nmap.org ) at 2023-05-23 04:56 EDT
Stat: 102:10 elapsed; © hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 21.97% done; ETC: 05:06 (0:07:45 remaining)
Nmap scan report for 152.96.7.6
Host is up (0.13s latency).
Not shown: 48128 closed tcp ports (reset)

PORT STATE SERVICE
31264/tcp open unknown

Nmap done: 1 IP address (1 host up) scanned in 669.54 seconds
```

Accessing the Port via browser: <br/>
![Untitled(3)](https://github.com/Aryt3/writeups/assets/110562298/ebda8e85-0399-4c56-8094-b3bcfaa4c627)

With the hint to scan the Dynamic Port Range let's do that. <br/>
```sh
kali@kali nmap -p 49151-65535 -T4 152.96.7.6

Starting Nmap 7.92 ( https://nmap.org ) at 2023-05-23 04:56 EDT
Stat: 102:10 elapsed; © hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 21.97% done; ETC: 05:06 (0:07:45 remaining)
Nmap scan report for 152.96.7.6
Host is up (0.13s latency).
Not shown: 48128 closed tcp ports (reset)

PORT STATE SERVICE
63484/tcp open unknown

Nmap done: 1 IP address (1 host up) scanned in 669.54 seconds
```

Accessing the Port via browser: <br/>
![Untitled(5)](https://github.com/Aryt3/writeups/assets/110562298/785001be-6a68-412b-8f0d-e93d49ccd6a0)

With the hint to scan the Port Range 1248-1348 for UDP, let's do that. <br/>
```sh
kali@kali nmap -sU -p 1248-1348 -T4 152.96.7.6

Starting Nmap 7.92 ( https://nmap.org ) at 2023-05-23 04:56 EDT
Stat: 102:10 elapsed; © hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 21.97% done; ETC: 05:06 (0:07:45 remaining)
Nmap scan report for 152.96.7.6
Host is up (0.13s latency).
Not shown: 48128 closed tcp ports (reset)

PORT STATE SERVICE
1256/tcp open unknown

Nmap done: 1 IP address (1 host up) scanned in 669.54 seconds
```

Accessing the Port via browser: <br/>
![Untitled(6)](https://github.com/Aryt3/writeups/assets/110562298/362daf4d-1124-409a-838c-43a89946315d)

Like this we obtained the flag.
