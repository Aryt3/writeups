# Aliens make me wanna Curl

## Description
```
We are expecting communications from an artificial intelligence device called MU-TH-UR 6000, referred to as mother by the crew. We disabled the login page and implemented a different method of authentication. The username is mother and the password is ovomorph. To ensure security, only mothers specific browser is allowed.
```

## Writeup

Ok so we instantly know that we need to make a curl request to the machine. <br/>
This should probably happen with the credentials we received so username being `mother` and password being `ovomorph`. <br/>
The are multiple options how to do this but the basic auth looks like this: <br/>
```sh
kali@kali curl -v -u mother:ovomorph https://spooky-aliens-make-me-wanna-curl-web.chals.io/flag 

------------------------------------------
< HTTP/1.1 200 OK
< X-Powered-By: Express
< Content-Type: text/html; charset=utf-8
< Content-Length: 17
< ETag: W/"11-+xBlBidHR/JNuLDy8WeziVrfMPQ"
< Date: Sat, 28 Oct 2023 04:49:33 GMT
< Connection: keep-alive
< Keep-Alive: timeout=5

Incorrect Device!  
```

It seems like this worked because actually doing it different results in this: <br/>
```sh
kali@kali curl -v  https://spooky-aliens-make-me-wanna-curl-web.chals.io/flag -H "username: mother" -H "password: ovonorph"

------------------------------------------
< HTTP/1.1 200 OK
< X-Powered-By: Express
< Content-Type: text/html; charset=utf-8
< Content-Length: 8
< ETag: W/"8-E3bLbI8EFr5TTzdttLsMCiSJtFI"
< Date: Sat, 28 Oct 2023 04:46:13 GMT
< Connection: keep-alive
< Keep-Alive: timeout=5

No auth!     
```

Now we need to bypass the error `Incorrect Device`. <br/>
Looking at the description again we see that they are talking about `MU-TH-UR 6000`. <br/>
Maybe using this one as a `User-Agent` will get us access. <br/>
```sh
kali@kali curl -u mother:ovomorph -H "User-Agent: MU-TH-UR 6000" https://spooky-aliens-make-me-wanna-curl-web.chals.io/flag 

NICC{dOnt_d3pEnD_On_h3AdeRs_4_s3eCu1ty} 
```

Seems like we got the flag. 