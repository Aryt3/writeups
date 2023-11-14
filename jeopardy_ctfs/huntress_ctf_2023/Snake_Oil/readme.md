# Snake Oil

## Description
```
One of our workstations was exhibiting strange network communications... we found this binary that looked to be the culprit. Can you find anything suspicious? 

Provided Files: snake-oil
```

## Writeup

Starting off I did a `strings` on the file and searched for interesting things. <br/>
This resulted in nothing so I uploaded the file to VirusTotal. <br/>

In VirusTotal we find some interesting things in the behavior tab. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/f87cfc4b-fcfd-44a4-b87e-d1e144f78f8f)

After taking a look at these IPs I concluded that they are a rabbit hole and took a look at the other things. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/534db4c4-0f1b-4ea1-a270-cc5636dd20cb)

Now there are a lot of things going on, so let's just execute the file in a windows sandbox VM. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/a61bae91-5640-4c25-9b83-157597892762)

Running the executable it seems to download an ngrok file. <br/>
This may be interesting but we do know that it deletes the files after creating them. <br/>
Knowing that I opened the file with x64dbg. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/37934504-09af-476b-9195-1ecc6a05ca38)

After running the file I paused it with the button in x64dbg before it can delete the files. <br/>
Now taking a look at our file system where we executed the file in we see a new folder. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/2525162a-9c9e-43ad-a366-87c001636c27)

In the folder itself there seems to be a file. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/a6552456-232f-422a-83e8-8dfcdcecaf36)

Opening the `ngrok.yml`. <br/>
```yml
authtoken: flag{d7267ce26203b5cc69f4bab679cc78d2}
```
