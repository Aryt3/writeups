# Wacky Recipe

## Description
```
Our Cyber Chef has been creating some wacky recipes recently, though he has been rather protective of his secret ingredients. 
Use this Chicken Parmi recipe and decipher the missing values to discover the chef's secret ingredient!

Authors: TurboPenguin & joseph
```

## Provided Files
```
- recipe.txt
```

## Writeup

Starting off by looking at the content of the provided file. <br/>
```
Chicken Parmi.

Our Cyber Chef has been creating some wacky recipes recently, though he has been rather protective of his secret ingredients.
Use this Chicken Parmi recipe and decipher the missing values to discover the chef's secret ingredient!
This recipe produces the flag in flag format.

Ingredients.
?? dashes pain
?? cups effort
1 cup water
4 kg bread crumbs
26 ml hot canola oil
13 kg egg yolks
24 teaspoons all purpose spices
7 teaspoons herbs
26 kg flour
26 kg sliced chicken breasts
1 dashes salt
11 dashes pepper
7 dashes pride and joy
10 kg tomato sauce
14 g cheese
13 kg ham
2 g pasta sauce
6 dashes chilli flakes
5 kg onion
9 dashes basil
19 dashes oregano
10 dashes parsley
20 teaspoons sugar

Cooking time: 25 minutes.

Pre-heat oven to 180 degrees Celsius.

Method.
Put water into 1st mixing bowl.
Add water to 1st mixing bowl.
Add water to 1st mixing bowl.
Add water to 1st mixing bowl.
Combine pain into 1st mixing bowl.
Remove bread crumbs from 1st mixing bowl.
Add effort to 1st mixing bowl.
Put water into 1st mixing bowl.
Add water to 1st mixing bowl.
Combine pain into 1st mixing bowl.
Add hot canola oil to 1st mixing bowl.
Add effort to 1st mixing bowl.
Put water into 1st mixing bowl.
Add water to 1st mixing bowl.
Add water to 1st mixing bowl.
Add water to 1st mixing bowl.
---------------------------------------
```

Now to solve this challenge you did need to know about [esolangs](https://esolangs.org/wiki/) which also contains [Chef](https://esolangs.org/wiki/Chef). <br/>
`Chef` is essentially a language where programs look like cooking recipes (I know :/). <br/>
The challenge itself was just about finding the correct values for `pain` and `effort`. <br/>
Sadly we found no working interpreter for this sh!tty language so we used online tools. <br/>

Using this [online-interpreter](https://esolangpark.vercel.app/ide/chef) we tried combinations between `12-28` with both values because in this scope we found the most useable results. <br/>
I tried automating it but that would have kind of included exploiting one of the online interpreters which is kind of ... and we didn't find any usable interpreter we could download. <br/>
Using the `monkey-brain-approach` I just manually tried every combination in that scope until I found `27 dashes pain` and `21 cups effort` which revealed the flag `DUCTF{2tsp_Vegemite}` and concludes this writeup. 