# ifconfig_inet

## Description
```
In the labyrinth of binary shadows, Elliot finds himself standing at the crossroads of justice and chaos. 
Mr. Robot, the enigmatic leader of the clandestine hacktivist group, has just unleashed a digital storm upon Evil Corp's fortress. 
The chaos is palpable, but this is just the beginning.

As the digital tempest rages, Elliot receives a cryptic message from Mr. Robot. 
"To bring down Evil Corp, we must cast the shadows of guilt upon Terry Colby," the message echoes in the encrypted channels. 
However, in the haze of hacktivism, Elliot loses the crucial IP address and the elusive name of the DAT file, leaving him in a digital conundrum.

To navigate this cybernetic maze, Elliot must embark on a quest through the binary underbelly of Evil Corp's servers. 
The servers, guarded by firewalls and encrypted gatekeepers, conceal the secrets needed to ensure Terry Colby's fall.

Guide Elliot to the his destiny.

Flag Format : VishwaCTF{name of DAT file with extension_IP address of Terry Colby}

E.g : VishwaCTF{file.dat_0.0.0.0}
```

## Writeup

Starting off, I searched `Terry Colby's IP address` and found https://www.reddit.com/r/MrRobot/comments/ehhs2c/im_sure_many_of_you_noticed_terry_colbys_ip/. <br/>
There I found the IP `218.108.149.373`, which doesn't seem to be an actual IP address. <br/>
Using other sources like the official fanpage https://mrrobot.fandom.com/wiki/Eps1.0_hellofriend.mov led me to the final page https://mrrobot.fandom.com/wiki/Eps1.0_hellofriend.mov/Summary which had the filename written in the provided summary. <br/>
Using these sources I pieced the flag `VishwaCTF{fsociety00.dat_218.108.149.373}` together which concludes this writeup.  

