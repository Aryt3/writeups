# Bug Bank

## Description
```
Welcome to BugBank, the world's premier banking application for trading bugs! 
In this new era, bugs are more valuable than gold, and we have built the ultimate platform for you to handle your buggy assets. 
Trade enough bugs and you have the chance to become a premium member. 
And in case you have any questions, do not hesitate to contact your personal assistant. Happy trading!
```

## Writeup

Taking a look at the website: <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/a5b37637-320c-4ce4-ae6c-d772012eaf25)

Creating an account: <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/9be6c612-1aa0-493e-b95d-bf2885d2db17)

Seems like we need a lot of bugs to upgrade to premium. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/de42b27b-c2e0-483f-b358-e53067932873)

Knowing this I created a second account and tried some things. <br/>
First of all I tried normal transfers but this didn't really work. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/6c3c1056-c5bb-44c6-91bd-a578e159d8b3)

Than I tried to send negative sums. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/846667fd-d390-4200-b7d3-e3484b49d1dd)

Seems like this doesn't send Bugs to another user but to yourself. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/7057244b-8f25-4d6d-91a3-b01de653119c)

I assume this works because the application tries to get the sum from your account so basically a `-` operation, but because I entered `-10000000` it tries to subtract a negative sum which just results in `- -10000000`. I suppose that this returns a `+` and therefore adds it to my balance. <br/>

Going back to settings page I tried to upgrade to premium. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/655977bb-77c6-465a-8c12-c6ba98966829)


