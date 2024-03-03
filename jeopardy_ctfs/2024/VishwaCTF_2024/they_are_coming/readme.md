# They are Coming

## Description
```
Aesthetic Looking army of 128 Robots with AGI Capabilities are coming to destroy our locality!
```

## Writeup

Starting off I looked at basic directories like `robots.txt`. <br/>
```
# https://www.robotstxt.org/robotstxt.html
User-agent: *
Disallow: /admin
L3NlY3JldC1sb2NhdGlvbg==
Decryption key: th1s_1s_n0t_t5e_f1a9
```

Decoding the `base-64` string I got a web-directory. <br/>
```sh
$ echo 'L3NlY3JldC1sb2NhdGlvbg==' | base64 -d
/secret-location
```

Taking a look at the directory we can see a suspicious looking string in the `response-headers`. <br/>
```
preferredCurrency    USD    
language    en_US    
lastLogin    2023-01-01T12:00:00Z    
Flag    Gkul0oJKhNZ1E8nxwnMY8Ljn1KNEW9G9l+w243EQt0M4si+fhPQdxoaKkHVTGjmA    
theme    dark    
unreadMessages    5    
F1ag    Open Your Eyes!    
isLoggedIn    true    
userRole    admin    
AppVer    1.0    
DivID    205
```

The page itself didn't contain anything of interest. <br/>
Knowing this I used the online-tool https://anycript.com/. <br/>
Entering `Gkul0oJKhNZ1E8nxwnMY8Ljn1KNEW9G9l+w243EQt0M4si+fhPQdxoaKkHVTGjmA` as encrypted text and `th1s_1s_n0t_t5e_f1a9` as secret key. <br/>
This didn't quite work as the key-size seemed to be invalid. To solve this issue I shortened the key to `128-bits`. <br/>
The final key was `th1s_1s_n0t_t5e_` which I used to successfully decrypt the flag `VishwaCTF{g0_Su88m1t_1t_Qu14kl7}` which concludes this writeup. <br/>

