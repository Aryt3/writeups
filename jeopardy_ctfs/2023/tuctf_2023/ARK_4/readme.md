# A.R.K. 4

## Description
```
What does the fox say?
```

## Provided Files
`fox.7z`

## Writeup

Starting off I downloaded the zipped archive and inspected it. <br/>
```sh
ls fox/
AlternateServices.txt         content-prefs.sqlite        favicons.sqlite      permissions.sqlite       sessionstore-backups
SiteSecurityServiceState.txt  cookies.sqlite              favicons.sqlite-wal  pkcs11.txt               settings
addonStartup.json.lz4         cookies.sqlite-shm          formhistory.sqlite   places.sqlite            shield-preference-experiments.json
addons.json                   cookies.sqlite-wal          gmp-gmpopenh264      places.sqlite-wal        storage
broadcast-listeners.json      crashes                     handlers.json        prefs.js                 storage.sqlite
cert9.db                      datareporting               key4.db              protections.sqlite       times.json
compatibility.ini             extension-preferences.json  logins-backup.json   search.json.mozlz4       webappsstore.sqlite
containers.json               extensions.json             logins.json          sessionCheckpoints.json  xulstore.json
```

From the name of the challenge and my general knowledge of web browsers I could deduct that this is some sort of firefox dump. <br/>
I had encountered such challenges in other CTFs and therefore I thought that in almost every case it would be useles to search around in those file, so I just used a tool to extract data from the dump. <br/>
```sh
python firefox_decrypt.py ../foxy/_fox.extracted/fox 
2023-12-03 14:57:21,893 - WARNING - profile.ini not found in ../foxy/_fox.extracted/fox
2023-12-03 14:57:21,893 - WARNING - Continuing and assuming '../foxy/_fox.extracted/fox' is a profile location

Website:   https://www.example.com
Username: 'fox'
Password: 'TUCTF{B3w4R3_7h3_f1r3_4nd_7h3_f0x}'
```

A relatively easy challenge if you know the tools. (https://github.com/unode/firefox_decrypt)
