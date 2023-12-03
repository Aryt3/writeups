# Table Encryption

## Description
```
You can't crack my file! I am the exclusive owner of the encryption key!
```

## Provided Files
`table_encryption.xml.enc`

## Writeup

Starting off I took a look at the file and concluded that it just contains binary data. <br/>
I basically had nothing to go off from but the file name. <br/>
The one thing which came to my mind was that the file is called **table_encryption.xml.enc**. I figured out that maybe it is a xml table and I could use that. <br/>

Using this I uploaded the whole file to CyberChef and did an `XOR` with the most common line first line in xml. <br/>
```xml
<?xml version="1.0" standalone="true" ?>
```

Using this as an `XOR` with decoding from `UTF-8` I received some decrypted plaintext. <br/>
```
Emoji Moring StaEmoj Onralos ...
```

Using `Emoji Moring StaEmoj` I did another `XOR` on the encrypted file and got a part of the flag between the binary data. <br/>
```
UCTF{x0r_t4bl3s_R_fu
```

Doing the same again with `Emoji Moring StaEmoj :Onralosw2"` as key I received the last part of the flag. <br/>
```
_fun!!!11!}
```

Combing these 2, I put together the correct flag `TUCTF{x0r_t4bl3s_R_fun!!!11!}` which concludes this crypto challenge.