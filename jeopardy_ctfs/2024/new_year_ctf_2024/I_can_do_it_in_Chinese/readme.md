# I can do it in Chinese

## Description
```
My friend has a crush on Chinese. I sent it, I don’t understand what...

杲潤湯等晟祯畟湥敤彩瑟楮彃桩湥獥彷敟捡湟摯彩瑟楮彃桩湥獥彽
```

## Writeup

Now I am familiar with `Base65536` which is an encoding which looks like mandarin. <br/>
Knowing this I used [CyberChef](https://cyberchef.org/#recipe=Magic(1,true,false,'')&input=5p2y5r2k5rmv562J5pmf56Wv55Wf5rml5pWk5b2p55Gf5qWu5b2D5qGp5rml542l5b235pWf5o2h5rmf5pGv5b2p55Gf5qWu5b2D5qGp5rml542l5b29) specifically its `magic module` to find the correct encoding. <br/>

The `magic module` revealed to me that the encoding type is `'UTF-16BE (1201)'`. <br/>
Like this I obtained the flag `grodno{If_you_need_it_in_Chinese_we_can_do_it_in_Chinese_}` which concludes this writeup.