# The Wizard

## Description
```
We intercepted a photo intended to be received by a suspected agent working with the Zorglaxians - or so it seems.

We're still decompiling the data, but we think the photo was taken nearby to where the agent was supposed to meet the Zorglaxians.

Can you find the location of the photo while our team works on decrypting the accompanying message?

We need the entire street address, city and abbreviated state or district of where it was taken to send our agents to investigate with the local authorities.

# = Number
XX = State abbreviation
All spaces are underscores

flag format: NICC{#_Street_Address_City_XX}
```

## Writeup

Starting off we have a provided image. <br/>
![the-wizard](https://github.com/Aryt3/writeups/assets/110562298/98539cae-a273-42e1-b283-9b5c20f53541)

by simply input parts of the image into google image search we are able to find some websites. <br/>
This one is especially interesting https://washington.org/de/visit-dc/where-to-find-street-murals-washington-dc. <br/>

![grafik](https://github.com/Aryt3/writeups/assets/110562298/8433a3c6-83e9-4a24-9508-d856eb523149)

Seems like we found our street name. <br/>
Now we only need to get the correct format together and after some tinkering I got it. <br/>
Correct Format: `NICC{950_24th_Street_NW_Washington_DC}`.
