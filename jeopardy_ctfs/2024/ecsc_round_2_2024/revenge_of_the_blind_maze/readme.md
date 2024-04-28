# Revenge of the Blind maze

## Description
```
Welcome back to the blind maze, this time you'll have a harder time finding the flag, good luck.

Site: http://blindmazerevenge.challs.open.ecsc2024.it
```

## Provided Files
```
capture.pcap
```

## Writeup

Starting off, I took a look at the provided `.pcap`. <br/>
```html
HTTP/1.1 200 OK
Server: nginx/1.18.0 (Ubuntu)
Date: Mon, 22 Apr 2024 10:17:19 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 740
Connection: keep-alive
Vary: Cookie
Set-Cookie: session=M6zEOx_oFzz3nlbCPHC1IlLq5WQzGgkLTWTPyfnkga4; Expires=Thu, 23 May 2024 10:17:19 GMT; HttpOnly; Path=/
<html>
<head>
<style>
    #container {
        text-align: center;
    }
    button {
        margin: 10px;
        padding: 10px 20px;
        font-size: 16px;
    }
</style>
</head>
<body>
<div id="container">
    <h2>Directional Movement Control</h2>
    <h4>Last Move: right</h4>
    <form action="/maze" method="get">
        <button type="submit" name="direction" value="up">Up</button><br>
        <button type="submit" name="direction" value="left">Left</button>
        <button type="submit" name="direction" value="right">Right</button><br>
        <button type="submit" name="direction" value="down">Down</button><br>
        <button type="submit" name="direction" value="start">Reset</button>
    </form>
</div>
</body>
</html>/9&f`
/9&f
GET /maze?direction=right HTTP/1.1
Host: localhost:5000
User-Agent: python-requests/2.25.1
Accept-Encoding: gzip, deflate
Accept: */*
Connection: keep-alive
Cookie: session=M6zEOx_oFzz3nlbCPHC1IlLq5WQzGgkLTWTPyfnkga4
/9&f
HTTP/1.1 200 OK
Server: nginx/1.18.0 (Ubuntu)
Date: Mon, 22 Apr 2024 10:17:19 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 52
Connection: keep-alive
Vary: Cookie
Set-Cookie: session=M6zEOx_oFzz3nlbCPHC1IlLq5WQzGgkLTWTPyfnkga4; Expires=Thu, 23 May 2024 10:17:19 GMT; HttpOnly; Path=/
The flag will appear here after the start of the CTF/9&f
```

There were a lot of such occurances which lead to my conclusion that we had to navigate a maze and the `.pcap` file did already contain the correct maze walkthrough. <br/>
Knowing this I was able to cut out the correct path using a simple regex. <br/>
```sh
$ strings capture.pcap | grep 'Last Move' | grep -v 'FAILED' | grep -oP '(?<=Last Move: )\w+' > directions.txt
```

After obtaining the correct path I made a small python script to automate the process of navigating through the maze. <br/>
```py
import requests

base_url = "http://blindmazerevenge.challs.open.ecsc2024.it"

session = requests.Session()

for line in open('directions.txt', 'r'):

    while True:
        res = session.get(f'{base_url}/maze?direction={line.strip()}')

        if 'FAILED' not in res.text:
            if 'openECSC{' in res.text:
                print(res.text)
                break

            break
```

Upon executing the script, I didn't instantly get the flag because I accidentally cut off the last move. <br/>
```sh
$ strings capture.pcap | tail -n 19

GET /maze?direction=right HTTP/1.1
Host: localhost:5000
User-Agent: python-requests/2.25.1
Accept-Encoding: gzip, deflate
Accept: */*
Connection: keep-alive
Cookie: session=M6zEOx_oFzz3nlbCPHC1IlLq5WQzGgkLTWTPyfnkga4
/9&f
HTTP/1.1 200 OK
Server: nginx/1.18.0 (Ubuntu)
Date: Mon, 22 Apr 2024 10:17:19 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 52
Connection: keep-alive
Vary: Cookie
Set-Cookie: session=M6zEOx_oFzz3nlbCPHC1IlLq5WQzGgkLTWTPyfnkga4; Expires=Thu, 23 May 2024 10:17:19 GMT; HttpOnly; Path=/
The flag will appear here after the start of the CTF/9&f
/9&f
/9&f
```

As I always searched for `<h4>Last Move: [DIRECTION]</h4>` it didn't add the last move which was `right`. <br/>
After debugging that and running the script again I obtained the flag which concludes this writeup. <br/>
```sh
$ python3 solve.py 
Here is the FLAG: openECSC{flag_inside_the_attachment_yes_we_like_it_665a901b}
```