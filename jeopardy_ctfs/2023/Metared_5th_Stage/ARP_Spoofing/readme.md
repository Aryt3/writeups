# ARP Spoofing 

## Description
```
Someone is on our network; we must find the intruder. To do so, we have captured the traffic where the attacker is located

The format for the flag is flag{MAC_ADDRESS}
```

## Provided Files
`ARP_Spoofing.pcapng`

## Writeup

Starting off I took a look in the `.pcapng` file. <br/>
Looking at the challenge name I used the filter `arp.opcode == 1` to search for arp requests. <br/>

After this I exported them in plaintext format. <br/>
Using bash I extracted the mac addresses need: <br/>
```sh
kali@kali grep -E -o '([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}' extracted.txt | grep -v ff:ff:ff:ff:ff:ff > actual_macs
00:da:55:bd:cb:c5
00:da:55:bd:cb:c5
00:da:55:bd:cb:c5
00:da:55:bd:cb:c5
00:da:55:bd:cb:c5
00:da:55:bd:cb:c5
f8:4d:fc:20:22:a2
f8:4d:fc:20:22:a2
f8:4d:fc:20:22:a2
f8:4d:fc:20:22:a2
f8:4d:fc:20:22:a2
f8:4d:fc:20:22:a2
00:da:55:bd:cb:c5
00:da:55:bd:cb:c5
00:da:55:bd:cb:c5
f8:4d:fc:20:22:a2
f8:4d:fc:20:22:a2
f8:4d:fc:20:22:a2
00:da:55:bd:cb:c5
00:da:55:bd:cb:c5
00:da:55:bd:cb:c5
00:da:55:bd:cb:c5
00:da:55:bd:cb:c5
00:da:55:bd:cb:c5
00:da:55:bd:cb:c5
00:da:55:bd:cb:c5
00:da:55:bd:cb:c5
00:da:55:bd:cb:c5
00:da:55:bd:cb:c5
00:da:55:bd:cb:c5
00:da:55:bd:cb:c5
00:da:55:bd:cb:c5
00:da:55:bd:cb:c5
-----------------
```

I did see some MAC-addresses which were the same so I cut them out. <br/>
```sh
kali@kali cat actual_macs | uniq
00:da:55:bd:cb:c5
f8:4d:fc:20:22:a2
00:da:55:bd:cb:c5
f8:4d:fc:20:22:a2
00:da:55:bd:cb:c5
08:00:27:ce:90:70
00:da:55:bd:cb:c5
08:00:27:ce:90:70
00:da:55:bd:cb:c5
c4:cb:e1:00:59:16
00:da:55:bd:cb:c5
c4:cb:e1:00:59:16
00:da:55:bd:cb:c5
c4:cb:e1:00:59:16
00:da:55:bd:cb:c5
c4:cb:e1:00:59:16
00:da:55:bd:cb:c5
c4:cb:e1:00:59:16
00:da:55:bd:cb:c5
60:18:95:52:97:96
08:00:27:ce:90:70
c4:cb:e1:00:59:16
00:da:55:bd:cb:c5
-----------------
```

I than proceeded to bruteforce the remaining macs like this `flag{MAC_ADDRESS}`and found a match for the third starting from the last one going upwards. <br/>

This concludes the challenge.