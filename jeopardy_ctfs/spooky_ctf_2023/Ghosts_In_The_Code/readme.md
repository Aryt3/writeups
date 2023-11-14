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
![grafik](https://github.com/Aryt3/writeups/assets/110562298/ef86d058-597f-437d-b275-064f171ba3dc)


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
![grafik](https://github.com/Aryt3/writeups/assets/110562298/1adad418-417b-4326-8aad-32c16994e4a1)

Also when we reload the webpage we can see the following: <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/12bf4126-395e-4115-b1db-3ed7cc46bc02)

Seems like we got another part of the flag. <br/>
I found the last part in the html code of the main page. <br/>
```html
<!--the final piece of your puzzle: r3_2_l00k!} -->
```

Putting the pieces together we receive `NICC{gh0sts_c@n_b3_tr1cky_2_s33_bu7_n0t_1f_y0u_kn0w_wh3r3_2_l00k!}`.

