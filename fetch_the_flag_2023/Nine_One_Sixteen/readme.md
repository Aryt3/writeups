# Nine-One-Sixteen

## Description
```
We found a vulnerability in this company's software and we are trying to do responsible disclosure! We want to notify the organization and contact them about the security issues... can you track down their contact info? 
```

## Writeup

Starting off we can see a normal website without any suspicious content. <br/>
[IMAGE]

We do see `RFC9116` an awful lot. <br/>
Searching for the term we find `security.txt`. <br/>

Looking at the wikipedia article we find the following: <br/>
```
security.txt files can be served under the /.well-known/ directory (i.e. /.well-known/security.txt) or the top-level directory (i.e. /security.txt) of a website. The file must be served over HTTPS and in plaintext format.
```

Navigating to `/.well-known/security.txt` we find this. <br/>
```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA512

Contact: mailto:notreal@.rfc9116.com
Expires: 2026-10-30T02:00:00.000Z
Preferred-Languages: flag{7b2bf7ec022acbddb0a75a362f4ce8ff}

-----BEGIN PGP SIGNATURE-----

iHUEARYKAB0WIQSsP2kEdoKDVFpSg6u3rK+YCkjapwUCY9qRaQAKCRC3rK+YCkja
pwALAP9LEHSYMDW4h8QRHg4MwCzUdnbjBLIvpq4QTo3dIqCUPwEA31MsEf95OKCh
MTHYHajOzjwpwlQVrjkK419igx4imgk=
=KONn
-----END PGP SIGNATURE-----
```