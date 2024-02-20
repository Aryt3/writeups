# Obedient Cat

## Description
```
Description
This file has a flag in plain sight (aka "in-the-clear"). 
```

## Provided Files
```
- flag
```

## Writeup

Taking a look at the provided file we can see that it has no externsion like `.pdf` or `.md`. <br/>
Using the basic `strings` command in linux we can take a look at the readable content of the file. <br/>
```sh
$ strings flag
picoCTF{s4n1ty_v3r1f13d_4a2b35fd}
```

Executing the command reveals the flag and concludes this writeup. <br/>

