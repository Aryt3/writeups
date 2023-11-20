# Vigil of the Ceaseless Eyes

## Description
```
Hey, contestants! Allow me to take this opportunity to debut the hottest new social media platform on the planet. 
I call it ManyKins! There is also ZERO chance it has ANY vulnerabilities that might allow one to find the flag (under /secret/flag.pdf)!
```

## Writeup

The first thing I thought of after seeing the desc. was a path traversal vulnerability. <br/>
Accessing the website via `https://nvstgt.com/ManyKin/index.html`. <br/>

Trying Path Traversal. <br/>
```sh
https://nvstgt.com/secret/flag.pdf
```

Seems like this didn't work. <br/>
Trying another one. <br/>
```sh
https://nvstgt.com/ManyKin/secret/flag.pdf
```

Seems like there is an empty pdf in this location. <br/>
Downloading it we can use some linux utility. <br/>
```sh
kali@kali wget https://nvstgt.com/ManyKin/secret/flag.pdf
kali@kali strings flag.pdf 
poctf{uwsp_71m3_15_4n_1llu510n}
```

This concludes the challenge. 

