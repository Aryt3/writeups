# President

## Description
```
Italian politicians are the best! And they always have a wise advice to share with us.
Just give them some time 😎
```

## Writeup

Starting off I took a look at the website. <br/>
```html
<!doctype html>
<html lang="en">

  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>President</title>
    <link href="static/css/main.css" rel="stylesheet">
    <link rel="icon" type="image/x-icon" href="static/img/favicon.png">
  </head>

  <body>
    <div class="center">
      <h1>
        If you are really interested about the future of children, you should listen to the famous answer of our former
        president Andreotti.
        <br>
        Don't worry if you are not italian, you'll understand 😎
      </h1>
      <iframe width="560" height="315" src="https://www.youtube.com/embed/hnBuaJDNagU?si=cT0Xkh8Qr2yCJxS0"
        title="YouTube video player" frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowfullscreen></iframe>
      <h1>
        P.S. If you have any other question, just ask for the president :)
      </h1>
    </div>
  </body>

</html> 
```


The youtube video didn't really lead anywhere and after a bit of reconnaissance I just started and active webscanner. <br/>
```sh
nikto -h https://president.hackappatoi.com/                    
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          92.246.89.201
+ Target Hostname:    president.hackappatoi.com
+ Target Port:        443
---------------------------------------------------------------------------
+ SSL Info:        Subject:  /CN=president.hackappatoi.com
                   Ciphers:  ECDHE-ECDSA-AES256-GCM-SHA384
                   Issuer:   /C=US/O=Let's Encrypt/CN=R3
+ Start Time:         2023-12-07 20:02:58 (GMT1)
---------------------------------------------------------------------------
+ Server: nginx/1.25.3
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The site uses TLS and the Strict-Transport-Security HTTP header is not defined. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ /: Cookie session created without the secure flag. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies
+ OPTIONS: Allowed HTTP Methods: HEAD, OPTIONS, PRESIDENTE, GET .
```

Seems like `nikto` found that we are able to the `HTTP-Method` **PRESIDENTE**. <br/>

Sending such a request we receive the flag which concludes this challenge. <br/>
```html
curl -X PRESIDENTE https://president.hackappatoi.com/

<!doctype html>
<html lang="en">

    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>President</title>
        <link rel="icon" type="image/x-icon" href="static/img/favicon.png">
    </head>

    <body>
        <code><span class="ascii" style="color: black; background: white;
            display:inline-block;
            white-space:pre;
            letter-spacing:0;
            line-height:1.4;
            font-family:'Consolas','BitstreamVeraSansMono','CourierNew',Courier,monospace;
            font-size:6px;
            
            border-width:1px;
            border-style:solid;
            border-color:lightgray;
-------------------------------------------------------------------
            </span></code>
        <h3>
            hctf{cust0m_ht7p_m3thod_1s_alway5_4_th1ng}
        </h3>
    </body>

</html> 
```

