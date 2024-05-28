# do you wanna build a snowman

## Description
```
Anna: Do you wanna build a snowman? Elsa: Sure if you can open my snowman picture
```

## Provided Files
```
- snowman.jpg
```

## Writeup

Starting off, I tried to display the picture but it seemed to be corrupted somehow. <br/>
Knowing that I looked at the `hex-bytes` of the picture using `xxd`. <br/>
```sh
$ xxd snowman.jpg | head
00000000: fdd8 ffe0 0010 4a46 4946 0001 0100 0001  ......JFIF......
00000010: 0001 0000 ffe2 01d8 4943 435f 5052 4f46  ........ICC_PROF
00000020: 494c 4500 0101 0000 01c8 0000 0000 0430  ILE............0
00000030: 0000 6d6e 7472 5247 4220 5859 5a20 07e0  ..mntrRGB XYZ ..
00000040: 0001 0001 0000 0000 0000 6163 7370 0000  ..........acsp..
00000050: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00000060: 0000 0000 0000 0000 0001 0000 f6d6 0001  ................
00000070: 0000 0000 d32d 0000 0000 0000 0000 0000  .....-..........
00000080: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00000090: 0000 0000 0000 0000 0000 0000 0000 0000  ................
```

Looking at the file header I saw an error. <br/>
The normal `jpeg` file header is `ffd8 ffe0` but in our case it seemed to be slightly broken. <br/>
Knowing this I madea `hex-dump` of the whole image file and fixed the file header. <br/>
```sh
# Hex-dump
$ xxd snowman.jpg > snowman.hex

# Editing file-header
$ vim snowman.hex

# Convert hex-dump back to image
$ xxd -r snowman.hex snowman_fixed.jpg
```

This revealed the flag which concludes this writeup. <br/>
<div style="text-align:center;">
    <img src="https://github.com/Aryt3/writeups/tree/main/jeopardy_ctfs/2024/angstrom_ctf_2024/do_you_wanna_build_a_snowman/snowman_fixed.jpg" alt="Image" />
</div>