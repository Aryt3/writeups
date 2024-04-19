# A Window into Space

## Description
```
I think aliens are testing us again and they they are poking fun at our internet protocols by using them in close proximity to earth. 
We were able to intercept something but I cant figure out what it is. Take a crack at it for me.
```

## Provided Files
```
- space.pcapng 
```

## Writeup

Starting off, we can use simple linux utility to inspect the file. <br/>
```sh
$ strings space.pcapng 
AMD Ryzen 7 7700X 8-Core Processor (with SSE4.2)
64-bit Windows 10 (22H2), build 19045
Dumpcap (Wireshark) 4.2.4 (v4.2.4-0-g1fe5bce8d665)
\Device\NPF_Loopback    
64-bit Windows 10 (22H2), build 19045
\+ ??
+ ?CP
{"I":"86189"}
Counters provided by dumpcap
```

The only interesting thing in the output is `{"I":"86189"}` which doesn't tell us much. <br/>
Opening the file in wireshark shows that there are not too many packages which allows us to inspect them all 1 by 1. <br/>

Inspecting the 19th package reveals nothing interesting on its own. <br/>
Just a bunch of random letters can be seen, but the interesting thing is the `s`. <br/>
![image](https://github.com/Aryt3/writeups/assets/110562298/451d1001-9e29-4628-b337-03907b5a75d9)

If we look at the next package we can actually see the letter `h` which does actually resemble the flag syntax `shctf{`. <br/>
![image](https://github.com/Aryt3/writeups/assets/110562298/9a48c2f7-6e40-4832-b244-70c1706513e2)

Going through the rest of the packages we can piece the flag together. <br/>
Obtaining the flag `shctf{1_sh0uld_try_h1d1ng_1n_th3_ch3cksum_n3xt_t1me_0817}` concludes this writeup. 


