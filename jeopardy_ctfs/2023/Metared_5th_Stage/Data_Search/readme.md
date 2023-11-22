# Data Search

## Description
```
The management of XYZ company is suspicious of certain employees who are stealing confidential information from the company website. The company manager asks you to check if this is really happening, for which he gives you a capture of the image of a USB device. The goal is to find some information from the website that has been saved or deleted on the device.

Md5 hash: 7782a9d1ef584827b0d30b7320331c00 Format flag: flat{xxxxxxxxxx} Image: [https://filesender.cedia.org.ec/?s=download&token=b0c53b0b-ba0a-a071-5dda-c752201c2c7e]
```

## Writeup

Inspecting the image using `autopsy` I was able to recover a file called `indexx.php`. <br/>
```php
<b>CTF</b>
<!-- index_0.php?secretword= 66 6C 61 74 7B 5F 35 30 6C 75 63 31 6F 6E 41 64 4F 5F 73 31 67 55 33 5F 61 44 33 6C 61 4E 74 33 7D-->
<br><br>
```

After inputing `66 6C 61 74 7B 5F 35 30 6C 75 63 31 6F 6E 41 64 4F 5F 73 31 67 55 33 5F 61 44 33 6C 61 4E 74 33 7D` into CyberChef and using the `from hex` module I obtained the flag `flat{_50luc1onAdO_s1gU3_aD3laNt3}` which concludes the challenge.
