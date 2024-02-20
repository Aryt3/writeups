# Python Wrangling

## Description
```
Python scripts are invoked kind of like programs in the Terminal... Can you run this Python script using this password to get the flag?
```

## Provided Files
```
- ende.py
- pw.txt
- flag.txt.en
```

## Writeup

Starting off we can try to just run the python file before further analyzing it. <br/>
```
$ python3 ./ende.py
Usage: ./ende.py (-e/-d) [file]
```

Here we can see that we can run the pythonfile using a `file` as parameter after either `-e` or `-d`. <br/>
Given the context of this challenge `-e` probably stands for `encrypting` and `-d` stands for `decrypting`. <br/>
Knowing this we can try to run the python script onto our `flag.txt.en`. <br/>
```sh
$ python3 .\ende.py -d .\flag.txt.en
Please enter the password:
```

Seems like this worked. We can now simply take the `password` from `pw.txt` and enter it into the terminal. <br/>
```sh
$ python3 .\ende.py -d .\flag.txt.en
Please enter the password:68f88f9368f88f9368f88f9368f88f93
picoCTF{4p0110_1n_7h3_h0us3_68f88f93}
```

Decrypting the file `flag.txt.en` finishes this challenge and concludes this writeup. 