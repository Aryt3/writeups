# What have we found here

## Description
```
As the sun dipped below the horizon, casting long shadows across the barren landscape, I stood alone at the edge of the world. The map had brought me here, to this remote and desolate place, in pursuit of a mystery that had captivated the world's greatest minds.

A cryptic message had been found on the ground, a message from the cosmos itself, or so it seemed. It hinted at the existence of extraterrestrial life, hidden within the depths of space. The message, a series of seemingly random characters, held secrets that could change everything we knew about the universe.

My task was to decipher it, to unlock its hidden meaning. The characters appeared to be encoded in a complex language, something that I cannot seem to figure out. The key to understanding lay within those symbols, like a cosmic puzzle waiting to be solved.

As I gazed up at the starry night sky, seeing the Leo Minor constellation in the sky, I knew that the fate of humanity rested on my ability to decode this enigmatic message, to uncover the truth hidden within the stars.
```

## Writeup

Starting off we take a look at the provided file. <br/>
Now putting it into different analyse-engines like cyberchef tells us that this is a base64 encoded string. <br/>

Decoding it leads to nothing as it is simply gibberish. <br/>
I used cat to pipe the base64 decoded string into a file. <br/>
```sh
kali@kali cat note.txt | base64 -d > output
```

I suddenly saw something interesting pop up on my screen. <br/>
Seems like the base64 decoded string is just a plain image. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/eb9fc410-1081-4a35-9e4d-0dc55dcd3160)

Seems like we found our flag. 
