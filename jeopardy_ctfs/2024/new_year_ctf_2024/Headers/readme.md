# Headers

## Description
```
https://ctf.mf.grsu.by/tasks/043db0a57ab0e71c37c90e784bed4517/
```

## Writeup

Seeing the challenge name I used curl to look at the specifics. <br/>
```sh
kali@kali curl -v --insecure -H "Yeet" https://ctf.mf.grsu.by/tasks/043db0a57ab0e71c37c90e784bed4517/

-------------------------------------------------------------
* using HTTP/1.x
> GET /tasks/043db0a57ab0e71c37c90e784bed4517/ HTTP/1.1
> Host: ctf.mf.grsu.by
> User-Agent: curl/8.5.0
> Accept: */*
> 
< HTTP/1.1 200 OK
< Server: nginx
< Date: Mon, 08 Jan 2024 14:26:36 GMT
< Content-Type: text/html; charset=UTF-8
< Content-Length: 233
< Connection: keep-alive
< Access-Control-Allow-Origin: *
< Authorization: Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJncm9kbm97MWZRRFE1c3dhaEdjVGNmMn0iLCJuYW1lIjoiSm9obiBEb2UiLCJpYXQiOjE1MTYyMzkwMjJ9.Prqxaq3rMHc1eOs7-n67mvW3h0Zmug3q417Rac3roqsQ6GA_cMsJDUEWybB4ixROTEsd3bLERJWQArD8CIuFpg
< Vary: Accept-Encoding
< Access-Control-Allow-Methods: GET, POST
< X-Content-Type-Options: nosniff
< X-XSS-Protection: 1; mode=block
< 

<!DOCTYPE html>
<html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>HTTP - Headers</title>
  </head>
  <body>
  </body>
</html>
```

The only thign we can look at here was the `Authorization` header. <br/>
Decoding this base64 string results in somethign interesting. <br/>
```sh
kali@kali echo 'eyJzdWIiOiJncm9kbm97MWZRRFE1c3dhaEdjVGNmMn0iLCJuYW1lIjoiSm9obiBEb2UiLCJpYXQiOjE1MTYyMzkwMjJ9' | base64 -d

{"sub":"grodno{1fQDQ5swahGcTcf2}","name":"John Doe","iat":1516239022} 
```

Now I only used the middle string becuase this looked like default `JSON Web Token` base64 encoded header. <br/>
Obtaining the flag concludes this writeup.