# Backdoor Splunk

## Description
```
You've probably seen Splunk being used for good, but have you seen it used for evil?

Provided File: Splunk_TA_Windows.zip
```

## Writeup

Starting with this challenge we have to start a machine which can be accessing via web. So I used curl:
```sh
kali@kali curl -v http://chal.ctf.games:31069/
> GET / HTTP/1.1
> Host: chal.ctf.games:31069
> User-Agent: curl/7.82.0
> Accept: */*

* Mark bundle as not supporting multiuse
< HTTP/1.1 401 UNAUTHORIZED
< Content-Type: application/json
< Content-Length: 52

{"error":"Missing or invalid Authorization header"}
```

Knowing that there are different types of Request Headers I tried some and got the correct Syntax:
```sh
kali@kali curl -v http://chal.ctf.games:31069/ -H "Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ=="
> GET / HTTP/1.1
> Host: chal.ctf.games:31069
> User-Agent: curl/7.82.0
> Accept: */*
> Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==

< HTTP/1.1 403 FORBIDDEN
< Content-Type: application/json
< Content-Length: 32

{"error":"Invalid credentials"}
```

So basically we have to pass along `Authorization: Basic [Base64-Encoded-Credentials]`. <br/>
The syntax for the base64-encoded-credentials is the following: `username:password`.
So knowing that we have to find an Auth token I used the following command:
```sh
find ./ -type f -exec grep -l "Auth" {} \; | xargs cat | grep Authorization

{Authorization=("Basic YmFja2Rvb3I6dXNlX3RoaXNfdG9fYXV0aGVudGljYXRlX3dpdGhfdGhlX2RlcGxveWVkX2h0dHBfc2VydmVyCg==")}
```

This gives us some stuff in which we find the base64 encoded credentials we need. <br/>
So adding this to our request we are able to send a working curl:
```sh
kali@kali curl -v http://chal.ctf.games:31069/ -H "Authorization: Basic YmFja2Rvb3I6dXNlX3RoaXNfdG9fYXV0aGVudGljYXRlX3dpdGhfdGhlX2RlcGxveWVkX2h0dHBfc2VydmVyCg=="
> GET / HTTP/1.1
> Host: chal.ctf.games:31158
> User-Agent: curl/7.82.0
> Accept: */*
> Authorization: Basic YmFja2Rvb3I6dXNlX3RoaXNfdG9fYXV0aGVudGljYXRlX3dpdGhfdGhlX2RlcGxveWVkX2h0dHBfc2VydmVyCg==

< HTTP/1.1 200 OK
< Content-Type: text/html; charset=utf-8
< Content-Length: 69
< 

<!-- ZWNobyBmbGFnezYwYmIzYmZhZjcwM2UwZmEzNjczMGFiNzBlMTE1YmQ3fQ== -->
```

Decoding thisobvious Base64 encoded string we are able to get the flag: `flag{60bb3bfaf703e0fa36730ab70e115bd7}`.
