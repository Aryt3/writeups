# aw man

## Description
```
Man? Is that you?
```

## Provided Files
<div style="text-align:center;">
    <img src="https://github.com/Aryt3/writeups/tree/main/jeopardy_ctfs/2024/angstrom_ctf_2024/aw_man/mann.jpg" alt="Image" />
</div>

## Writeup

Starting off, I tried to inspect the image using tools like `exiftool` and basic utility like `strings`. <br/>
After finding nothing I used the online-tool [aperisolve](https://www.aperisolve.com/787587fd20283c2cf0682e1c00546dac) to get further details. <br/>
The results contained a `steghide` file `enc.txt` which contained `5RRjnsi3Hb3yT3jWgFRcPWUg5gYXe81WPeX3vmXS`. <br/>

Using [CyberChef](https://gchq.github.io/CyberChef/#recipe=Magic(3,false,false,'')&input=NVJSam5zaTNIYjN5VDNqV2dGUmNQV1VnNWdZWGU4MVdQZVgzdm1YUw) I extracted the flag `actf{crazy?_i_was_crazy_once}` which concludes this writeup.