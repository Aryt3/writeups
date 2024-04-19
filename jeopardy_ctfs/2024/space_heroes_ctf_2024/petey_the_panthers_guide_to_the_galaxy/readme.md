# Petey the Panther's Guide to the Galaxy

## Description
```
Petey the Panther has stumbled upon the greatest treasure this side of the Milky Way: a bonafide Hitchhikers Guide to the Galaxy! 
What kind of secrets does this thing hold?
```

## Provided Files
```
- A_Real_Space_Hero.jpg 
```

## Writeup

Starting off, we can analyze the provided image file. <br/>
Using binwalk reveals a lot of hidden files. <br/>
```sh
$ binwalk -e A_Real_Space_Hero.jpg 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
1891          0x763           Certificate in DER format (x509 v3), header length: 4, sequence length: 1573
3471          0xD8F           Certificate in DER format (x509 v3), header length: 4, sequence length: 1746
5224          0x1468          Certificate in DER format (x509 v3), header length: 4, sequence length: 1455
6719          0x1A3F          Object signature in DER format (PKCS header length: 4, sequence length: 5928
6888          0x1AE8          Certificate in DER format (x509 v3), header length: 4, sequence length: 1730
8622          0x21AE          Certificate in DER format (x509 v3), header length: 4, sequence length: 1710
10336         0x2860          Certificate in DER format (x509 v3), header length: 4, sequence length: 1421
13067         0x330B          TIFF image data, big-endian, offset of first image directory: 8
256834        0x3EB42         Zip archive data, at least v1.0 to extract, name: secrets/
256872        0x3EB68         Zip archive data, at least v2.0 to extract, compressed size: 123, uncompressed size: 164, name: secrets/piece_0.png
257044        0x3EC14         Zip archive data, at least v2.0 to extract, compressed size: 106, uncompressed size: 120, name: secrets/piece_1.png
257199        0x3ECAF         Zip archive data, at least v2.0 to extract, compressed size: 152, uncompressed size: 182, name: secrets/piece_10.png

---------------------------------------------------------------------------------------------------------------------------------------------------
```

Seems like there were hundreds of images hidden within the single image. <br/>
Looking at those images we should realize that those pictures are actually small pieces of a single `QR-Code`. <br/>
To piece all those pieces together we can write a simple python script. <br/>
```py
from PIL import Image
import os

images = []
for filename in os.listdir("pieces"):
    if filename.endswith(".png"):
        img = Image.open(os.path.join("pieces", filename))
        images.append((filename, img))

images.sort(key=lambda x: int(x[0].split("_")[1].split(".")[0]))

piece_width, piece_height = images[0][1].size
num_cols = 20 
num_rows = 20 

final_image = Image.new('RGB', (num_cols * piece_width, num_rows * piece_height))

for i, (filename, img) in enumerate(images):
    col_index = i % num_cols
    row_index = i // num_cols
    final_image.paste(img, (col_index * piece_width, row_index * piece_height))

final_image.show()
```

Running the script returns a `QR-Code`. <br/>
![image](https://github.com/Aryt3/writeups/assets/110562298/c44b4e9b-09c7-4880-9f4d-9ce33bc57cd1)

Scanning it reveals the flag `shctf{s0_l0ng_4nd_th4nks_f0r_4ll_th3_flags}` which concludes this writeup. 


