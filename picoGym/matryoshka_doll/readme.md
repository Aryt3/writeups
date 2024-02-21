# Matryoshka doll

## Description 
```
Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. 
What's the final one? 
```

## Provided Files
```
- dolls.jpg
```

## Writeup

Starting off, we should use some basic linux utility to try and extract data from the file. <br/>
This would make sense as the description states `placed one inside another`. <br/>
```sh
$ binwalk -e dolls.jpg 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 594 x 1104, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
272492        0x4286C         Zip archive data, at least v2.0 to extract, compressed size: 378954, uncompressed size: 383938, name: base_images/2_c.jpg
651612        0x9F15C         End of Zip archive, footer length: 22
```

`binwalk` is a simple tool which can extract data from a file using the parameter `-e`(extract). <br/>
We can than repeat this process a few times to check if we can do it manually. <br/>
```sh
$ binwalk -e _dolls.jpg.extracted/base_images/2_c.jpg 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 526 x 1106, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
187707        0x2DD3B         Zip archive data, at least v2.0 to extract, compressed size: 196043, uncompressed size: 201445, name: base_images/3_c.jpg
383805        0x5DB3D         End of Zip archive, footer length: 22
383916        0x5DBAC         End of Zip archive, footer length: 22


$ binwalk -e _dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images/3_c.jpg 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 428 x 1104, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
123606        0x1E2D6         Zip archive data, at least v2.0 to extract, compressed size: 77651, uncompressed size: 79807, name: base_images/4_c.jpg
201423        0x312CF         End of Zip archive, footer length: 22


$ binwalk -e _dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images/_3_c.jpg.extracted/base_images/4_c.jpg 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 320 x 768, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
79578         0x136DA         Zip archive data, at least v2.0 to extract, compressed size: 63, uncompressed size: 81, name: flag.txt
79785         0x137A9         End of Zip archive, footer length: 22


$ ls -la _dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images/_3_c.jpg.extracted/base_images/_4_c.jpg.extracted/
drwxr-xr-x   - w1sh 21 Feb 14:12  .
drwxr-xr-x   - w1sh 21 Feb 14:12  ..
.rw-r--r-- 229 w1sh 21 Feb 14:12  136DA.zip
.rw-r--r--  81 w1sh 16 Mär  2021  flag.txt

```

After 3 more repetitions we successfully found the flag. <br/>
A simple `strings flag.txt` didn't return anything and `cat` couldn't output it either. <br/>
Running into this issue we may upload `flag.txt` to [CyberChef](https://cyberchef.org/#recipe=Find_/_Replace(%7B'option':'Regex','string':'%5E%5Ba-zA-Z0-9_.-%5D*$'%7D,'',true,false,true,false)&input=cABpAGMAbwBDAFQARgB7AGIAZgA2AGEAYwBmADgANwA4AGQAYwBiAGQANwA1ADIAZgA0ADcAMgAxAGUANAAxAGIAMQBiADEAYgA2ADYAYgB9) which may help us analyze the content. <br/>

Taking a look at the contents on `CyberChef` we can see that the characters seem to be surrounded by binary values. <br/>
Deleting those reveals the flag `picoCTF{bf6acf878dcbd752f4721e41b1b1b66b}` which concludes this writeup.