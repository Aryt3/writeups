# Nice netcat...

## Description
```
There is a nice program that you can talk to by using this command in a shell: $ nc mercury.picoctf.net 49039, but it doesn't speak English...
```

## Writeup

`nc` or `netcat` is a service which can read or write from or to a network connections using either the TCP or UDP protocol. <br/>
Knowing this we can connect to the service being provided to use in the description. <br/>
```sh
$ nc mercury.picoctf.net 49039
112 
105 
99 
111 
67 
84 
70 
123 
103 
48 
48 
100 
95 
107 
49 
116 
116 
121 
33 
95 
110 
49 
99 
51 
95 
107 
49 
116 
116 
121 
33 
95 
51 
100 
56 
52 
101 
100 
99 
56 
125 
10 
```

Now doing this gets us a lot of numbers. <br/>
If you see such a "random" sequence of numbers you should know it they might represent `ASCII` values of normal letters. You know this if the numbers are between `48-125`<br/>
You can use simple `python` utility to prove it. <br/>
```sh
$ python3         
Python 3.11.7 (main, Dec  8 2023, 14:22:46) [GCC 13.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print(chr(112))
p
>>> print(chr(105))
i
>>> print(chr(99))
c
>>> print(chr(111))
o
```

We see that the first letters when converted to valid letters represent the flag prefix `picoCTF`. <br/>
Knowing this we can write a simple `python script` to solve this challenge. <br/>
```py
numbers = """112 
105 
99 
111 
67 
84 
70 
123 
103 
48 
48 
100 
95 
107 
49 
116 
116 
121 
33 
95 
110 
49 
99 
51 
95 
107 
49 
116 
116 
121 
33 
95 
51 
100 
56 
52 
101 
100 
99 
56 
125"""

output = ""

# Iterate over each line
for num_str in numbers.split('\n'):
    # Convert integer to its corresponding ASCII character
    output += chr(int(num_str))

print(output)

```

Using `chr(NUMBER)` we can conert each letter. <br/>
```sh
$ python3 ./solve.py
picoCTF{g00d_k1tty!_n1c3_k1tty!_3d84edc8}
```

Running the script reveals the flag to us which concludes this writeup. 