# Needle in a Haystack

## Description
```
I lost my flag and I can't seem to find it. I know I put it in this folder, but it is not showing up.

Can you help me find it?
```

## Writeup

Downloading the compressed folder we ca nunzip it and view its contents. <br/>
```sh
kali@kali unzip haystack
Archive:  haystack.zip
replace haystack/Abraxas.webp? [y]es, [n]o, [A]ll, [N]one, [r]ename: A
  inflating: haystack/Abraxas.webp   
  inflating: haystack/dark_and_stormy.txt  
  inflating: haystack/do-you-know-the-muffin-man.gif  
  inflating: haystack/dusclops.png   
 extracting: haystack/flag.txt.txt   
  inflating: haystack/folklore/flying-dutchman.jpg  
  inflating: haystack/folklore/Headless-Horseman.jpg  
  inflating: haystack/folklore/jersey-devil.jpg  
  inflating: haystack/folklore/marshman.jpg  
  inflating: haystack/giratina.png   
  inflating: haystack/more_horror stories.txt  
  inflating: haystack/pumpkaboo.png  
  inflating: haystack/pumpkin_man.jfif  
  inflating: haystack/spooky-halloween.gif  
  inflating: haystack/The Tale of the Haunted Hollow.docx  
  inflating: haystack/the_haunting_of_blackwood_manor/the_arrival.txt  
  inflating: haystack/the_haunting_of_blackwood_manor/the_final_countdown.txt  
  inflating: haystack/the_haunting_of_blackwood_manor/the_investigation.txt  
  inflating: haystack/the_haunting_of_blackwood_manor/the_malevolent_force.txt  
  inflating: haystack/the_haunting_of_blackwood_manor/the_price_of_freedom.txt  
  inflating: haystack/the_haunting_of_blackwood_manor/the_unexplained_phenomena.txt  
  inflating: haystack/trevenant.png

kali@kali ls -la haystack/
total 1376
drwxr-xr-x  4 root root   4096 Oct 28 09:26  .
drwxr-xr-x 13 kali kali   4096 Oct 28 08:47  ..
-rw-r--r--  1 root root  70132 Sep 14 15:30  Abraxas.webp
-rw-r--r--  1 root root  13836 Sep 14 15:37 'The Tale of the Haunted Hollow.docx'
-rw-r--r--  1 root root    976 Sep 14 14:20  dark_and_stormy.txt
-rw-r--r--  1 root root 341653 Sep 17 18:39  do-you-know-the-muffin-man.gif
-rw-r--r--  1 root root 129830 Sep 14 15:25  dusclops.png
-rw-r--r--  1 root root     19 Oct 14 23:41  flag.txt.txt
drwxr-xr-x  2 root root   4096 Oct 28 09:26  folklore
-rw-r--r--  1 root root 203539 Sep 14 15:26  giratina.png
-rw-r--r--  1 root root   4040 Sep 14 15:24 'more_horror stories.txt'
-rw-r--r--  1 root root 140445 Sep 14 14:18  pumpkaboo.png
-rw-r--r--  1 root root  66860 Sep 14 15:46  pumpkin_man.jfif
-rw-r--r--  1 root root 223376 Sep 17 18:38  spooky-halloween.gif
drwxr-xr-x  2 root root   4096 Oct 28 09:26  the_haunting_of_blackwood_manor
-rw-r--r--  1 root root 171336 Sep 14 15:24  trevenant.png
```

Seems like we found some interesting things but we also found a `flag.txt`, <br/>
```sh
kali@kali cat haystack/flag.txt.txt 
NICC{th4t_w45_345y}
```

Seems like we found our flag.

