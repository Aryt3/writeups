# Indirect Payload

Starting the with the challenge I make a curl request to the website: <br/>
```sh
kali@kali curl -v http://chal.ctf.games:31232/             
> GET / HTTP/1.1
> Host: chal.ctf.games:31232
> User-Agent: curl/7.88.1
> Accept: */*
> 
< HTTP/1.1 200 OK
< Date: Wed, 18 Oct 2023 15:41:51 GMT
< Server: Apache/2.4.38 (Debian)
< Vary: Accept-Encoding
< Content-Length: 1373
< Content-Type: text/html; charset=UTF-8
```

I than received the following html code:
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css"
        integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
    <script
  src="https://code.jquery.com/jquery-3.5.1.slim.min.js"
  integrity="sha256-4+XzXVhsDmqanXGHaHvgh1gMQKX40OUvDEBTu8JcmNs="
  crossorigin="anonymous"></script>

    <title>Indirect Payload</title>

    <script>
        $(document).ready(function(){
            $('button').click(function(){
                $('.alert').show()
            }) 
        });
    </script>
</head>

<body>
    <div class="container-fluid">
        <div class="row justify-content-center mt-5">
            <div class="card col-md-8">
                <div class="card-body">
                    <a class="notifications top-left" href="/site/flag.php"><button type="button" class="btn btn-primary btn-lg btn-block">Retrieve the Payload</button></a>
                </div>
            </div>
            
        </div>
        <div class="row justify-content-center mt-5">
            <div class="alert alert-info" style="display:none">
              Retrieving the payload, please wait...
            </div>
        </div>
    </div>

</body>

</html>
```

The interesting thing to me is `/site/flag.php` so I make a curl to this file: <br/>
```sh
kali@kali curl -v http://chal.ctf.games:31232/site/flag.php                                                          
> GET /site/flag.php HTTP/1.1
> Host: chal.ctf.games:31232
> User-Agent: curl/7.88.1
> Accept: */*
> 
< HTTP/1.1 302 Found
< Date: Wed, 18 Oct 2023 15:41:37 GMT
< Server: Apache/2.4.38 (Debian)
< Location: /site/fe3cbf06ef09be78eb8ae144888eeeae.php
< Content-Length: 0
< Content-Type: text/html; charset=UTF-8
```

Seeing that I get a redirect I activate `-L` option to take the 302. <br/>
```sh
curl -L -v http://chal.ctf.games:31232/site/flag.php
> GET /site/flag.php HTTP/1.1
> Host: chal.ctf.games:31232
> User-Agent: curl/7.88.1
> Accept: */*

< HTTP/1.1 302 Found
< Date: Wed, 18 Oct 2023 15:45:17 GMT
< Server: Apache/2.4.38 (Debian)
< Location: /site/fe3cbf06ef09be78eb8ae144888eeeae.php
< Content-Length: 0
< Content-Type: text/html; charset=UTF-8

> GET /site/fe3cbf06ef09be78eb8ae144888eeeae.php HTTP/1.1
> Host: chal.ctf.games:31232
> User-Agent: curl/7.88.1
> Accept: */*

< HTTP/1.1 302 Found
------------------------------------
```

I cut out the rest because it seems I got stuck in a redirection loop. <br/>
But I noticed that some redirects to certain files do actually include a `Content-Length`. <br/>
Knowing this I made a request to a redirection-URL without the `-L` option. <br/>
```sh
kali@kali curl -v http://chal.ctf.games:31232/site/f99cc7e975c1fdfd1b803bd248bac515.php  
> GET /site/f99cc7e975c1fdfd1b803bd248bac515.php HTTP/1.1
> Host: chal.ctf.games:31232
> User-Agent: curl/7.88.1
> Accept: */*
> 
< HTTP/1.1 302 Found
< Date: Wed, 18 Oct 2023 15:46:22 GMT
< Server: Apache/2.4.38 (Debian)
< Location: /site/0eb108f40ad71158d396d396e825fab7.php
< Content-Length: 32
< Content-Type: text/html; charset=UTF-8
< 
character 0 of the payload is f
```

Seeing this it seems like the flag is split up on different URLs. Knowing this I made a small script in Python because curl doesn't support outputing every redirection response-body. <br/>
```py
import requests

basic_url = 'http://chal.ctf.games:31232'
url = basic_url + '/site/flag.php'

max_redirects = 100

session = requests.Session()

output_file = open('redirect_responses.txt', 'wb')

for i in range(max_redirects):
    response = session.get(url, allow_redirects=False)

    output_file.write(response.content)

    if 300 <= response.status_code < 400:
        directory = response.headers['Location']
        url = basic_url + directory
    else:
        print(f"Final response status code: {response.status_code}")
        break

output_file.close()

session.close()
```

Seems like it worked because our file is now filled with this: <br/>
```txt
character 0 of the payload is f
character 1 of the payload is l
character 2 of the payload is a
character 3 of the payload is g
character 4 of the payload is {
character 5 of the payload is 4
character 6 of the payload is 4
character 7 of the payload is 8
character 8 of the payload is c
character 9 of the payload is 0
character 10 of the payload is 5
character 11 of the payload is a
character 12 of the payload is b
character 13 of the payload is 3
character 14 of the payload is e
character 15 of the payload is 3
character 16 of the payload is a
character 17 of the payload is 7
character 18 of the payload is d
character 19 of the payload is 6
character 20 of the payload is 8
character 21 of the payload is e
character 22 of the payload is 3
character 23 of the payload is 5
character 24 of the payload is 0
character 25 of the payload is 9
character 26 of the payload is e
character 27 of the payload is b
character 28 of the payload is 8
character 29 of the payload is 5
character 30 of the payload is e
character 31 of the payload is 8
character 32 of the payload is 7
character 33 of the payload is 2
character 34 of the payload is 0
character 35 of the payload is 6
character 36 of the payload is f
character 37 of the payload is }
```

Now we have the flag but I don't want to enter it manually. So I paste all the content into CyberChef and add a `Find / Replace` module. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/e4a39b6b-e53e-4674-b410-e289ff4c46ae)

There I used Regex to cut out the phrases in front of the flag-parts. The Regular Expression: `character \d+ of the payload is`. <br/>
I also used another `Find / Replace` to cut out spaces and to drop the lines. The Regular Expression: `\n `. <br/>

Like this I was able to obtain the flag: `flag{448c05ab3e3a7d68e3509eb85e87206f}`.
