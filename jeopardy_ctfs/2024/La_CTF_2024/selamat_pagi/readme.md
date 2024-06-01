# Selamat Pagi

## Description
```
If you talk in another language, nobody can understand what you say! Check out this message I sent in Indonesian. To add some extra security, I also applied a monoalphabetic substitution cipher on it!
```

## Provided Files
`message.txt`

## Writeup

I started off by taking a look at the provided file. <br/>
```
Efe kqkbkx czwkf akfs kdkf qzfskf wzdcjtfk
Ieqku kqk akfs ikxj kck akfs wkak ukikukf :Q
Lzfqztk ukdj kqk qe wefe: bkvim{wzbkdki_ckse_kckukx_ukdj_wjuk_kfkbewew_mtzujzfwe}
```

From the description I knew that it was an indonesian `Substitution-Cipher`. <br/>
Knowing this and the flag prefix `lactf` I was able to map some characters to certain other letters. <br/>
```
Efe kqkbkx czwkf akfs kdkf qzfskf wzdcjtfk
??? a?ala? ????? ?a?? a?a? ????a? ???????a

Ieqku kqk akfs ikxj kck akfs wkak ukikukf :Q
???a? a?a ?a?? ta?? a?a ?a?? ?a?a ?ata?a? :?

Lzfqztk ukdj kqk qe wefe: bkvim{wzbkdki_ckse_kckukx_ukdj_wjuk_kfkbewew_mtzujzfwe}
??????a ?a?? a?a ?? ????: lactf{??la?at_?a??_a?a?a?_?a??_???a_a?al????_f????????}
```

Remembering the challenge name `selamat pagi` I was able to map it to the first 2 words of the flag. <br/>
```
Efe kqkbkx czwkf akfs kdkf qzfskf wzdcjtfk
i?i a?ala? ?es?? ?a?g ama? ?e?ga? sem????a

Ieqku kqk akfs ikxj kck akfs wkak ukikukf :Q
?i?a? a?a ?a?g ta?? a?a ?a?g sa?a ?ata?a? :?

Lzfqztk ukdj kqk qe wefe: bkvim{wzbkdki_ckse_kckukx_ukdj_wjuk_kfkbewew_mtzujzfwe}
?e??e?a ?am? a?a ?i si?i: lactf{selamat_pagi_a?a?a?_?am?_s??a_a?al?s?s_f?e??e?s?}
```

Having this I was also able to map a lot of other letters due to words missing only 1 letter. <br/>
To find these words I used the following ressources:
- https://dictionary.cambridge.org/dictionary/indonesian-english/
- https://www.deepl.com/translator

Found words:
- `ini`
- `dengan`
- `di sini`

```
Efe kqkbkx czwkf akfs kdkf qzfskf wzdcjtfk
ini adala? ?es?n ?ang ama? dengan sem???na

Ieqku kqk akfs ikxj kck akfs wkak ukikukf :Q
?ida? ada ?ang ta?? a?a ?ang sa?a ?ata?an :D

Lzfqztk ukdj kqk qe wefe: bkvim{wzbkdki_ckse_kckukx_ukdj_wjuk_kfkbewew_mtzujzfwe}
?ende?a ?am? ada di sini: lactf{selamat_pagi_a?a?a?_?am?_s??a_anal?s?s_f?e??ens?}
```

Filling in the rest wasn't too hard because there are not so many words with such combinations. <br/>
```
Efe kqkbkx czwkf akfs kdkf qzfskf wzdcjtfk
ini adalah pesan yang aman dengan sempurna

Ieqku kqk akfs ikxj kck akfs wkak ukikukf :Q
tidak ada yang tahu apa yang saya katakan :D

Lzfqztk ukdj kqk qe wefe: bkvim{wzbkdki_ckse_kckukx_ukdj_wjuk_kfkbewew_mtzujzfwe}
bendera kamu ada di sini: lactf{selamat_pagi_apakah_kamu_suka_analisis_frekuensi}
```

Obtaining `lactf{selamat_pagi_apakah_kamu_suka_analisis_frekuensi}` concludes this writeup. 