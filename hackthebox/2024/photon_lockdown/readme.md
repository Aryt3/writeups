# Photon Lockdown

## Description
```
We've located the adversary's location and must now secure access to their Optical Network Terminal to disable their internet connection. 
Fortunately, we've obtained a copy of the device's firmware, which is suspected to contain hardcoded credentials. 
Can you extract the password from it?
```

## Provided Files
```
- fwu_ver
- hw_ver
- rootfs
```

## Writeup

Starting off with file inspecting I got the filetype `Squashfs filesystem`. <br/>
```sh
$ file rootfs                                      
rootfs: Squashfs filesystem, little endian, version 4.0, zlib compressed, 10936182 bytes, 910 inodes, blocksize: 131072 bytes, created: Sun Oct  1 07:02:43 2023
```

Knowing this I used `binwalk` to extract the filesystem itself. <br/>
```sh
$ binwalk -e rootfs     

-------

$ cd _rootfs.extracted      
$ ls     
0.squashfs  squashfs-root  squashfs-root-0

$ cd squashfs-root    
$ ls
bin  config  dev  etc  home  image  lib  mnt  overlay  proc  run  sbin  sys  tmp  usr  var
```

Instead of manually searching through the directories I used a `find` command to check if the flag-prefix can be found in any file. <br/>
```sh
$ find ./ -type f -exec strings {} \; | grep "HTB{"

<Value Name="SUSER_PASSWORD" Value="HTB{REDACTED}"/>
```

Obtaining the flag concludes this writeup.