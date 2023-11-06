# Baking

## Description 
```
Do you know how to make cookies? How about HTTP flavored?
```

## Writeup

Taking a look at the website we find this: <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/117dd9c2-dfea-4fe5-9a5b-426a89fa2299)

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
![grafik](https://github.com/Aryt3/writeups/assets/110562298/a3d505de-296f-41ca-88ef-3e6ac4f97d4e)

Like this I was able to obtain the flag: `flag{c36fb6ebdbc2c44e6198bf4154d94ed4}`.
