# lolz#2

This was an unrelated challenge so it didn't give any points, it was fun anyway. <br/>
Starting of we got the following String `籖ꍨ穉鵨杤𒅆象𓍆穉鵨詌ꍸ穌橊救硖穤歊晑硒敤睊ꉑ硊ꉤ晊ꉑ硆詤橆赑硤ꉑ穊赑硤詥楊ꉑ睖ꉥ橊赑睤ꉥ杊𐙑硬ꉒ橆𐙑硨穒祊ꉑ硖詤桊赑硤詥晊晑牙`.

Knowing that this is Base65536 encoded from another challenge I instantly did that and obtained another encoded string. <br/>
`VGhlIEhhd2FpaWFuIEhhLUxlLEJ5Q0VCdEJ6Q1RCd0JBQkJCdkJ1QkFCdUF5QXdCQkJEQXdCeUJ4QkVBekJ5QXdBekJ2QnlCRkF5QnhCREJDQkVCdUJ3QXdCeUJ1Q1Y=`. <br/>

I instantly realised that this is base64 encoding so I decoded it another time.
```sh
kali@kali echo 'VGhlIEhhd2FpaWFuIEhhLUxlLEJ5Q0VCdEJ6Q1RCd0JBQkJCdkJ1QkFCdUF5QXdCQkJEQXdCeUJ4QkVBekJ5QXdBekJ2QnlCRkF5QnhCREJDQkVCdUJ3QXdCeUJ1Q1Y=' | base64 -d
The Hawaiian Ha-Le,ByCEBtBzCTBwBABBBvBuBABuAyAwBBBDAwByBxBEAzByAwAzBvByBFAyBxBDBCBEBuBwAwByBuCV
```

Seeing this output I couldn't think of any encoding/encryption type so I researched a bit but came up with nothing. <br/>
The thing I did notice was though that it seems like these are characters pairs. <br/>
So this means that `By` stands for 1 characters of the flag. <br/>

I also thought that this is already the flag because I saw 4 characters `By CE Bt Bz` and than I saw `CT`. <br/>
The reason I thought this was the flag is because the last 2 letters `CV` seem to be similar to `CT` and from experience I knew that `{` and `}` converted to decimal are basically 1 number apart, same as `T` and `V`. <br/>
This would mean that `CV` equals `{` and `CT` equals `}`. <br/>
Knowing this and the flag format I was able to decipher a part of the flag. <br>
`flag{BwBABBBvBuBABuAyAwBBBDAwByBxBEAzByAwAzBvByBFAyBxBDBCBEBuBwAwByBu}`
So the next thing I did was list the letter-pairs alphabetically:

| A-Pairs | B-Pairs | C-Pairs |
| :-----: | :-----: | :-----: |
| Aw | Bt | CE |
| Ay | Bu | CT |
| Az | Bv | CV |
|  | Bw |  |
|  | Bx |  |
|  | By |  |
|  | Bz |  |
|  | BA |  |
|  | BB |  |
|  | BC |  |
|  | BD |  |
|  | BE |  |
|  | BF |  |

In this table are the letter-pairs we know:
| Characters | Translation |
| ---------- | ----------- |
| By | f |
| CE | l |
| Bt | a |
| Bz | g |
| CV | { |
| CT | } |

Knowing that `By` equals `f` I now need to find how exatly this relates to the other characters. <br/>
Taking `f` and puting a number on it I am marking it as `6` as it is the 6. letter in the alphabet. <br/>
Doing this with the other letters too I got the following: `a` equals `1` and `f` equals `6`. There are 4 letters inbetween those 2 letters.<br/>

So now I got the following: `Bt`(a) and `By`(f). <br/>
taking `t` and `y` they are also 4 letters apart. <br/>

Knowing this I made a table to decode the letters I can be sure about:
| letter | Letter-Pair |
| :----: | :---------: |
| a | Bt |
| b | Bu |
| c | Bv |
| d | Bw |
| e | Bx |
| f | By |
| g | Bz |

Now we know some letters. Continuing this makes no sense as we do know that `l` equals `CE`. <br/>
I will deocde it now with the things we know: `f l a g { d BA BB c b BA b Ay Aw BB BD Aw f e BE Az f Aw Az c f BF Ay e BD BC BE b d Aw f b }`. <br/>

So let's list the remaining letter-pairs: `BA BB Ay Aw BD BE Az BF BC`. <br/>
Knowing that it can't be letters because it wouldn't make sense as we know from previous documentation. <br/>

As there are only numbers left I resume to list the following table:
| Letter-Pair | number |
| :---------: | :----: |
| Aw | 0 |
| Ax | 1 |
| Ay | 2 |
| Az | 3 |
| BA | 4 |
| BB | 5 |
| BC | 6 |
| BD | 7 |
| BE | 8 |
| BF | 9 |

This would be my first guess to put the numbers together. <br/>
Trying it out in CyberChef with around 17 `Find / Replace` filters we get the flag `flag{d45cb4b20570fe83f03cf92e768bd0fb}`.


