# Comprezz

## Description
```
Someone stole my S's and replaced them with Z's! Have you ever seen this kind of file before?
```

## Writeup

A compressed folder, let's try some tools on it:
```sh
kali@kali gzip -d comprezz
bzip2 -d comprezz
tar -xvf comprezz
unzip comprezz
7z x comprezz

gzip: comprezz: unknown suffix -- ignored
bzip2: Can't guess original name for comprezz -- using comprezz.out
bzip2: comprezz is not a bzip2 file.
Archive:  comprezz
  End-of-central-directory signature not found.  Either this file is not
  a zipfile, or it constitutes one disk of a multi-part archive.  In the
  latter case the central directory and zipfile comment will be found on
  the last disk(s) of this archive.
note:  comprezz may be a plain executable, not an archive
unzip:  cannot find zipfile directory in one of comprezz or
        comprezz.zip, and cannot find comprezz.ZIP, period.

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=C.UTF-8,Utf16=on,HugeFiles=on,64 bits,128 CPUs AMD Ryzen 9 7900X 12-Core Processor             (A60F12),ASM,AES-NI)

Scanning the drive for archives:
1 file, 45 bytes (1 KiB)

Extracting archive: comprezz
--
Path = comprezz
Type = Z

Everything is Ok

Size:       39
Compressed: 45

kali@kali ls
comprezz  comprezz~

kali@kali file comprezz\~ 
comprezz~: ASCII text

kali@kali strings comprezz\~ 
flag{196a71490b7b55c42bf443274f9ff42b}
```

Like this we received the flag `flag{196a71490b7b55c42bf443274f9ff42b}`.
