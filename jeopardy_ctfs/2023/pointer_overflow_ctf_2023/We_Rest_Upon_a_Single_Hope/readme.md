# We Rest Upon a Single Hope

## Description
```
I am Vinz, Vinz Clortho, Keymaster of Gozer. Volguus Zildrohar, Lord of the Sebouillia. Are you the Gatekeeper?
```

## Writeup

Sending a curl request to the website we pull the whole content. <br/>
```sh
kali@kali curl https://nvstgt.com/Hope2/ 
```

Content: <br/>
```html
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<META charset="utf-8"/>

<HTML>
  <HEAD>
    <TITLE>I dreamed a dream the other night...</TITLE>
    <LINK rel="stylesheet" type="text/css" href="./static/style.css">
        <SCRIPT>
                function Gozer(key) {
                        var hash = 0, i, chr;
                        for (i = 0; i < key.length; i++) {
                                chr   = key.charCodeAt(i);
                                hash  = ((hash << 5) - hash) + chr;
                                hash |= 0;
                        }
                        return hash;
                }
                function conv(s)        {
                        var a = [];
                        for (var n = 0, l = s.length; n < l; n ++) {
                                var hex = Number(s.charCodeAt(n)).toString(16);
                                a.push(hex);
                        }
                        return a.join('');
                }
                function Zuul(key) {
                        if (key == v) {
                                var Gatekeeper = [];
                                var y = [];
                                var z = [];
                                Gatekeeper[0] = "706f6374667b75777370";
                                Gatekeeper[1] = "formal";
                                Gatekeeper[2] = "88410";
                                for (var i = 0, l = Gatekeeper[0].length; i < l; i ++) {
                                        if (i == 0 || i % 2 == 0) {
                                                y += String.fromCharCode(parseInt((Gatekeeper[0].substring(i, i+2)), 16));
                                        }
                                }
                                z[0] = y;
                                z[1] = Gatekeeper[2][3];
                                z[2] = Gatekeeper[2][2] + Gatekeeper[1][3];
                                z[3] = z[2][0] + Gatekeeper[1][5] + Gatekeeper[1][5];
                                z[4] = (Gatekeeper[2]/12630) + "h" + z[2][0] + (Gatekeeper[2][0]-1);
                                z[5] = z[4][0] + z[4][1] + '3' + Gatekeeper[1][2] + '3';
                                z[6] = (Gatekeeper[2]/Gatekeeper[2]) + '5';
                                z[7] = (Gatekeeper[2]*0) + Gatekeeper[1][0];
                                z[8] = (Gatekeeper[2]/12630) + "h" + '3';
                                z[9] = Gatekeeper[1][3] + (Gatekeeper[2]*0) + '5' + (Gatekeeper[2][0]-1);
                                z[10] = 'r' + '3' + z[2][0] + Gatekeeper[1][5] + '}';
                                console.log(z.join("_"));
                        } else {
                                console.log("Gozer the Traveler. He will come in one of the pre-chosen forms. During the rectification of the Vuldrini, the traveler came as a large and moving Torg! Then, during the third reconciliation of the last of the McKetrick supplicants, they chose a new form for him: that of a giant Slor! Many Shuvs and Zuuls knew what it was to be roasted in the depths of the Slor that day, I can tell you!");
                        }
                }
                var p = navigator.mimeTypes+navigator.doNotTrack;
                var o = navigator.deviceMemory;
                var c = navigator.vendor+navigator.userAgent;
                var t = navigator.product+p;
                var f = o+c+p;
                var v = Gozer(p/((o+c)*t)+f);
        </SCRIPT>
  </HEAD>

  <BODY>
    <H1>We rest upon a single hope...</H1>
        <FORM name="Gatekeeper">
                <DIV>
                    <LABEL>Are you the Keymaster?</LABEL>
                        <INPUT id="key" name="key" type="password">
                </DIV>
                <DIV>
                        <INPUT id="login" type="submit" value="Submit" onclick="return Zuul(key.value)">
                </DIV>
        </FORM>
  </BODY>
</HTML>
```

Taking another look at the suspicous javascript code. <br/>
```js
function Gozer(key) {
    var hash = 0, i, chr;
    for (i = 0; i < key.length; i++) {
            chr   = key.charCodeAt(i);
            hash  = ((hash << 5) - hash) + chr;
            hash |= 0;
    }
    return hash;
}

function conv(s)        {
    var a = [];
    for (var n = 0, l = s.length; n < l; n ++) {
            var hex = Number(s.charCodeAt(n)).toString(16);
            a.push(hex);
    }
    return a.join('');
}

function Zuul(key) {
    if (key == v) {
            var Gatekeeper = [];
            var y = [];
            var z = [];
            Gatekeeper[0] = "706f6374667b75777370";
            Gatekeeper[1] = "formal";
            Gatekeeper[2] = "88410";
            for (var i = 0, l = Gatekeeper[0].length; i < l; i ++) {
                    if (i == 0 || i % 2 == 0) {
                            y += String.fromCharCode(parseInt((Gatekeeper[0].substring(i, i+2)), 16));
                    }
            }
            z[0] = y;
            z[1] = Gatekeeper[2][3];
            z[2] = Gatekeeper[2][2] + Gatekeeper[1][3];
            z[3] = z[2][0] + Gatekeeper[1][5] + Gatekeeper[1][5];
            z[4] = (Gatekeeper[2]/12630) + "h" + z[2][0] + (Gatekeeper[2][0]-1);
            z[5] = z[4][0] + z[4][1] + '3' + Gatekeeper[1][2] + '3';
            z[6] = (Gatekeeper[2]/Gatekeeper[2]) + '5';
            z[7] = (Gatekeeper[2]*0) + Gatekeeper[1][0];
            z[8] = (Gatekeeper[2]/12630) + "h" + '3';
            z[9] = Gatekeeper[1][3] + (Gatekeeper[2]*0) + '5' + (Gatekeeper[2][0]-1);
            z[10] = 'r' + '3' + z[2][0] + Gatekeeper[1][5] + '}';
            console.log(z.join("_"));
    } else {
            console.log("Gozer the Traveler. He will come in one of the pre-chosen forms. During the rectification of the Vuldrini, the traveler came as a large and moving Torg! Then, during the third reconciliation of the last of the McKetrick supplicants, they chose a new form for him: that of a giant Slor! Many Shuvs and Zuuls knew what it was to be roasted in the depths of the Slor that day, I can tell you!");
    }
}

var p = navigator.mimeTypes+navigator.doNotTrack;
var o = navigator.deviceMemory;
var c = navigator.vendor+navigator.userAgent;
var t = navigator.product+p;
var f = o+c+p;
var v = Gozer(p/((o+c)*t)+f);
```

Taking a look at this it seems as if we receive the flag by inputing the correct key or just bypassing the check. <br/>
Seems like we need to input `v` to get the correct value. <br/>
```js
function Gozer(key) {
    var hash = 0, i, chr;
    for (i = 0; i < key.length; i++) {
            chr   = key.charCodeAt(i);
            hash  = ((hash << 5) - hash) + chr;
            hash |= 0;
    }
    return hash;
}

var v = Gozer(p/((o+c)*t)+f);
console.log(v)
```

Executing this in my browser I obtain `-267142268`. <br/>
Inputing this in my browser as the key I receive the flag `poctf{uwsp_1_4m_4ll_7h47_7h3r3_15_0f_7h3_m057_r34l}`. <br/>
