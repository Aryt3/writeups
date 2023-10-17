# BaseFFFF+1

Starting the challenge we get the following description: `Maybe you already know about base64, but what if we took it up a notch?`. <br/>
Now everybody should know base64 encoding and also maybe base85 but looking at the content of the file I can instantly see that it's not your typical base85. <br/>

The content of the file looks like this: `鹎驣𔔠𓁯噫谠啥鹭鵧啴陨驶𒄠陬驹啤鹷鵴𓈠𒁯ꔠ𐙡啹院驳啳驨驲挮售𖠰筆筆鸠啳樶栵愵欠樵樳昫鸠啳樶栵嘶谠ꍥ啬𐙡𔕹𖥡唬驨驲鸠啳𒁹𓁵鬠陬潧㸍㸍ꍦ鱡汻欱靡驣洸鬰渰汢饣汣根騸饤杦样椶𠌸`. 

Trying out the magic module of CyberChef doesn't get us far so let's look for another approach. <br/>

Now taking a look at the file name `baseFFFF+1`. <br/>
This does really look like hexadecimal numbers so translating the `FFFF` to decimal numbers we receive `65535`.<br/>

Counting this together we receive `Base65536`. <br/>
After a quick google search I found this website https://www.better-converter.com/Encoders-Decoders/Base65536-Decode. <br/>

Using this website to deocde the file we get the flag: `flag{716abce880f09b7cdc7938eddf273648}`.

