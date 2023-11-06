# Back The Hawks

## Description
```
We are Back the Hawks! We're a non-profit that seeks to protect hawks across the world. We have a vibrant community of Backers who are all passionate about Backing the Hawks! We'd love for you to join us... if you can figure out how to get an access code.

NOTE - any resemblence to other companies, non-profits, services, login portal challenges, and/or the like, living or dead, is completely coincidental. 
```

## Writeup

Taking a look at the website: <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/b73ebcab-7c98-42a7-8fe2-840ecbcac9d0)

Taking a look around I found some javascript code. <br/>
```js
function makeInviteCode() {
    var o = "! edoc/etivni/skwah/eht/kcab/ ot tseuqer TSOP a ekaM !skwaH eht gnikcaB htiw nwod er'uoy erus ekam ot tnaw YLLAER ,yllaer eW";

    var d = o.split('').reverse().join('');

    console.log(d);
}
```

Executing the function in the browser we receive the following. <br/>
```js
makeInviteCode();
We really, REALLY want to make sure you're down with Backing the Hawks! Make a POST request to /back/the/hawks/invite/code !
```

Sending the POST request to `/back/the/hawks/invite/code`.
```sh
kali@kali curl -X POST http://challenge.ctf.games:31955/back/the/hawks/invite/code
{"hint":"this message is encrypted, there's no way to break it! Forget about backing the hawks. Your journey ends here.","message":"TB_LRQ_EBOB_YXZHFK_QEB_EXTHP_2023"}
```

Now to me this does kind of sound provocative and false. <br/>
Also I kind of thought that this might just be a sentence wit ha bit shift in there. <br/>

So doing a caesar cipher bruteforce I actually received the valid key `WE_OUT_HERE_BACKIN_THE_HAWKS_2023`. <br/>
Using the key to register we are able to find the flag. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/9f61da39-d2ac-44a1-9722-2208a361d1cc)

