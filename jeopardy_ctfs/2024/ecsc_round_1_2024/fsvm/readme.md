# Fsvm

## Description
```
I want this VM to generate a good description, but all I get is "no".
```

## Provided Files
```
- vm
- bytecode
```

## Writeup

Starting off, I took a look at the provided files. <br/>
`vm` seemed to be a linux binary and `bytecode` contained a lot of random characters. <br/>
Before analyzing the binary I wanted to check the behavior of `vm`. <br/>
```sh
$ ./vm bytecode
flag:
test
no
```

The important thing to notice during the executing is that after initial binary execution a directory will be created in the directory the binary was executed in. <br/>
The directory `regs/` will be created when running the binary, inside this dir some files will be created with some useles information, upon entering an input for `flag:` the directory will be deleted again. <br/>
Upon noticing this, I decided to track file changes in my system, using the Linux utility `inotifywait`. <br/>

Testing file changes by running the binary: <br/>
```sh
$ ./vm bytecode
flag:
```

Setting up the listener in the `regs/` directory and entering something into the `flag:` prompt outputs a lot of stuff. <br/>
```sh
$ while inotifywait -e close_write -r regs/; do cat regs/*; done
Setting up watches.  Beware: since -r was given, this may take a while!
Watches established.
regs/ CLOSE_WRITE,CLOSE reg0
10011flag:011210111410197115121118109995210156559935074Setting up watches.  Beware: since -r was given, this may take a while!
Watches established.
regs/ CLOSE_WRITE,CLOSE reg1
0111flag:011210111069678367123115117112101114101971151211181099952101565599350740000000000000000000000000000Setting up watches.  Beware: since -r was given, this may take a while!
Watches established.
regs/ CLOSE_WRITE,CLOSE reg2
cat: 'regs/*': No such file or directory
Setting up watches.  Beware: since -r was given, this may take a while!
Couldn't watch regs/: No such file or directory
```

In the output I saw that there were a lot of numbers being written to the files before being deleted. <br/>
Taking a portion of the string I tried to further analyze `011101121011106967836712311511711210111410197115121118109995210156559935074000`. <br/>
To make sure i don't f**k anything up, I first tried to convert the flag prefix `openECSC{` to decimal using [CyberChef](https://cyberchef.org/#recipe=To_Decimal('Space',false)&input=b3BlbkVDU0N7). <br/>
Below you can see the convertion. <br/>
```
o   p   e   n   E  C  S  C  {
111 112 101 110 69 67 83 67 123
```

Seeing this I tried to match it to the output from `inotifywait` command. <br/>
```
011101121011106967836712311511711210111410197115121118109995210156559935074000
111 112 101 110 69 67 83 67 123 115 117 112 101 114 101 97 115 121 118 109 99 52 101 56 55 99
```

This basically translated to `openECSC{supereasyvmc` and some more characters which I wasn't if they were part of the flag. <br/>
Tampering with the input some more and watching the file-changes I was able to finally narrow the output down to the right flag. <br/>
I confirmed that I had the correct flag by using the binary which concludes this writeup. <br/>
```sh
$ ./vm bytecode
flag:
openECSC{supereasyvmc4e87c4d}
ok 
```

