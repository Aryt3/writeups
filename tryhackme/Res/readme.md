# Res

Basic Recon:
```sh
nmap -sV $ip -p-
Starting Nmap 7.94 ( https://nmap.org ) at 2023-10-10 08:43 CEST
Nmap scan report for 10.10.57.136
Host is up (0.070s latency).
Not shown: 65533 closed tcp ports (reset)
PORT     STATE SERVICE VERSION
80/tcp   open  http    Apache httpd 2.4.18 ((Ubuntu))
6379/tcp open  redis   Redis key-value store 6.0.7

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 81.22 seconds
```

Question: 
Scan the machine, how many ports are open? <br/>
Answer:
`2` Ports are open.

Question:
What's is the database management system installed on the server? <br/>
Answer:
The database management system running on Port 6379 is `redis`.

Question:
What port is the database management system running on? <br/>
Answer:
The Port Redis is running on is `6379`.

Question:
What's is the version of management system installed on the server? <br/>
Answer:
The version of Redis is `6.0.7`.




