# Networking

> [!NOTE]
> This directory contains every writeup on the category Networking because they are all related.
> 
> Provided Files: `packets-file.pcapng`

## Vicker IP

### Description
```
What is the victim & attacker ip?
```

### Writeup

Starting off I took a look at the `.pcapng` file with a `http` filter where I found something really interesting. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/327e82fd-24e4-4d03-b72a-2a03e08f1a0d)

This really looked like a directory scan. <br/>
Knowing this I tried the flag `KCTF{victimIp_attackerIp}` which turned out to be correct. <br/>

## Basic Enum

### Description
```
What tool did the attacker use to do basic enumeration of the server?

Please use the attachment of the first challenge.

Flag Format: KCTF{toolname} 
```

### Writeup

After making a plaintext dump from the `.pcapng` file I manually searched for enumeration tools which I personally use. <br/>
I found multiple tools like `nmap` or `nikto`. After testing those out as flag I was able to find the correct one `KCTF{nikto}`. <br/>

## Vulnerable Service 

### Description
```
What service was vulnerable to the main server?

Please use the attachment of the first challenge.

Flag Format: KCTF{service_version} >>all_lower_case
```

### Writeup

Going through the plaintext dump I found multiple services like `apache` or `nginx`, but couldn't find any vulnerabilities being exploited. <br/>
Finally after all enumeration tools I found being used I found the attacker gaining access to the system with the service `(vsFTPd 2.3.4)` which when turned into the flag `KCTF{vsftpd_2.3.4}` turned out to be the correct one. <br/>

## CVE ID

### Description
```
What's the CVE id for the vulnerable service?

Please use the attachment of the first challenge.

Flag Format: KCTF{CVE-xxxx-xxxx} 
```

### Writeup

Although I didn't directly find any CVEs being mentioned about this service I was able to find a reverse shell being opened on port `6200`. <br/>
Searching online for CVEs connected to `vsftpd` wit ha reverse shell I quickly found [one](https://nvd.nist.gov/vuln/detail/CVE-2011-2523) with a 9.8 CVE score. <br/>
Testing this one as a flag I instantly got the correct one. (KCTF{CVE-2011-2523}) <br/>

## Famous Tool

### Description
```
The attacker used a popular tool to gain access of the server. Can you name it?

Please use the attachment of the first challenge.

Flag Format: KCTF{toolname} 
```

### Writeup

Now after looking for clues a long time, I couldn't find anything in the plaintext dump I made. <br/>
Logically speaking there are not too many famous tools which provide an option for multiple explotis with reverse shells. <br/>
Knowing this I just tried the ones I knew which resulted in me finding the correct one `KCTF{metasploit}`. <br/>

## Port

### Description
```
What was the port number of the reverse shell of the server?

Please use the attachment of the first challenge.

Flag Format: KCTF{port} 
```

### Writeup

Now I actually already solved this challenge [above](#cve-id). <br/>
Reverse Shell triggered onm port 6200, flag is `KCTF{6200}`.
