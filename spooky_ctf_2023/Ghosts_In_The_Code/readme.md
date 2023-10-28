# Ghosts in the Code

## Description
```
Some student here spun up a site where people are submitting their stories about all of the spooky stuff on campus!

This site is clearly haunted... or, at the very least, cursed.

https://niccgetsspooky.xyz

Flag Format: NICC{w0rds_may_c0nta1n_nums_and_chars!?} - but there are no apostrophes, commas, for colons
```

## Writeup

Taking a look at the website: <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/004fcf56-8c12-45d0-b392-2a7a90747010)

Clicking on `Learn More` we get an alert outputing `BOO! ahh! You found part one... -> NICC{gh0sts`. <br/>
From this i deducted that the flag is split up in multiple peaces. <br/>

Searching for `_` in the bootstrap file we find the following: <br/>
```sh
  .flg-txt-pt2{
	  value: '_c@n_b3_tr1';
  }
```

Taking a look at the javascript code on the debugger tab in Firefox we see a lot of stuff and also another part of the flag. <br/>
```
"They shouted that you found the third!: cky_2_s33_b",
```

Taking a look at the cookies we are able to see another part. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/67dc4970-9d51-4a96-8c88-e4ad28e5d75c)

Also when we reload the webpage we can see the following: <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/26750038-c336-461c-9fcc-ad6df0dbdbf5)

Seems like we got another part of the flag. <br/>
I found the last part in the html code of the main page. <br/>
```html
<!--the final piece of your puzzle: r3_2_l00k!} -->
```

Putting the pieces together we receive `NICC{gh0sts_c@n_b3_tr1cky_2_s33_bu7_n0t_1f_y0u_kn0w_wh3r3_2_l00k!}`.

