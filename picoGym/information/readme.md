# Information

## Description
```
Files can always be changed in a secret way. Can you find the flag?
```

## Provided Files
```
- cat.jpg
```

## Writeup

Knowing that this is a `Forensics` challenge we can use simple tools to analyze image files. <br/>
```sh
$ exiftool cat.jpg            
ExifTool Version Number         : 12.65
File Name                       : cat.jpg
Directory                       : .
File Size                       : 878 kB
File Modification Date/Time     : 2024:02:20 16:47:32+01:00
File Access Date/Time           : 2024:02:20 16:47:36+01:00
File Inode Change Date/Time     : 2024:02:20 16:47:35+01:00
File Permissions                : -rwxrw-rw-
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.02
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
Current IPTC Digest             : 7a78f3d9cfb1ce42ab5a3aa30573d617
Copyright Notice                : PicoCTF
Application Record Version      : 4
XMP Toolkit                     : Image::ExifTool 10.80
License                         : cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9
Rights                          : PicoCTF
Image Width                     : 2560
Image Height                    : 1598
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 2560x1598
Megapixels                      : 4.1
```

`exiftool` is probably the most well-known tool to analyze a picture. <br/>
We can see that it displayed a lot of interestinf information. <br/>
The only thing we are interested in though are suspicious strings like `cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9`. <br/>
Now for those that don't know this encoding CyberChef may help you, but to those who know you can use simple linx utility to decode it. <br/>
```sh
$ echo 'cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9' | base64 -d
picoCTF{the_m3tadata_1s_modified} 
```

Decoding the flag from the encoded message concludes this writeup. <br/>

> [!NOTE]
> `Base64` is one of the most used encodings ever and is often used in CTFs.