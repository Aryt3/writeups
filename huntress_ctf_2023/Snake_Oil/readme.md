# Snake Oil

## Description
```
One of our workstations was exhibiting strange network communications... we found this binary that looked to be the culprit. Can you find anything suspicious? 

Provided Files: snake-oil
```

## Writeup

Starting off I did a `strings` on the file and searched for interesting things. <br/>
This resulted in nothing so I uploaded the file to VirusTotal. <br/>

In Virus Totalwe find some interesting things in the behavior tab. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/b01991df-c603-46e0-a10d-36c26927e2fb)

After taking a look at these IPs I concluded that they are a rabbit hole and took a look at the other things. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/a2313897-efa9-44e7-b962-138cacd83e60)

Now there are a lot of thigns going on, so let's just execute the file in a windows sandbox VM. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/05e2a3aa-d67b-4e0d-8c93-e20b9bec3ce3)

Running the executable it seems to download an ngrok file. <br/>
This may be interesting but we do know that it deletes the files after creating them. <br/>
Knowing that I opened the file with x64dbg. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/96b8e4db-7be7-43e1-954c-82fa56d9551e)

After runnign the file I paused it with the button in x64dbg before it can delete the files. <br/>
Now taking a look at our file system where we executed the file in we see a new folder. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/a79bb128-b14b-4bbe-bf89-950d680ba343)

In the folder itself there seems to be a file. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/8ded5834-7573-44d5-b0cc-6587ecae3cac)

And like that we found the flag for this challenge. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/4851c7a2-628c-4dd9-8bf4-14b2c1ffa982)
