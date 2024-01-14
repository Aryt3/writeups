# Broken file

## Description
```
Is there something wrong with the image?
```

## Provided Files
`image.jpg`

## Writeup

Let's take a look at the image with some tools. <br/>
```sh
kali@kali exiftool image.jpg 
ExifTool Version Number         : 12.70
File Name                       : image.jpg
Directory                       : Downloads
File Size                       : 208 bytes
File Modification Date/Time     : 2024:01:08 14:39:16+01:00
File Access Date/Time           : 2024:01:08 14:39:16+01:00
File Inode Change Date/Time     : 2024:01:08 14:39:16+01:00
File Permissions                : -rw-r--r--
Warning                         : Install Archive::Zip to decode compressed ZIP information
File Type                       : ZIP
File Type Extension             : zip
MIME Type                       : application/zip
Zip Required Version            : 10
Zip Bit Flag                    : 0
Zip Compression                 : None
Zip Modify Date                 : 2023:12:22 22:59:18
Zip CRC                         : 0x93d2c8ee
Zip Compressed Size             : 42
Zip Uncompressed Size           : 42
Zip File Name                   : flag.txt
```

Open archive. <br/>
```sh
kali@kali binwalk -e image.jpg 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             Zip archive data, at least v1.0 to extract, compressed size: 42, uncompressed size: 42, name: flag.txt
186           0xBA            End of Zip archive, footer length: 22


kali@kali ls
drwxr-xr-x   - w1sh  8 Jän 14:47  _image.jpg.extracted
.rw-r--r-- 208 w1sh  8 Jän 14:39  image.jpg

kali@kali cd _image.jpg.extracted/
kali@kali ls
.rw-r--r-- 208 w1sh  8 Jän 14:47  0.zip
.rw-r--r--  42 w1sh 22 Dez  2023  flag.txt

kali@kali cat flag.txt 
File: flag.txt
grodno{X9pZ2qY7rL4sW8tH1uA3vB6wK0xJ5yC2z}
```

Obtaining the flag `grodno{X9pZ2qY7rL4sW8tH1uA3vB6wK0xJ5yC2z}` concludes this writeup. 