# Magikarp Ground Mission

## Description
```
Do you know how to move between directories and read files in the shell? Start the container, `ssh` to it, and then `ls` once connected to begin. 
Login via `ssh` as `ctf-player` with the password, `6dee9772`

Additional details will be available after launching your challenge instance.
```

## Writeup

We should start off by starting an instance and connect to the provided hostname. <br/>
```sh
$ ssh ctf-player@venus.picoctf.net -p 53183
ctf-player@venus.picoctf.net's password: 
Welcome to Ubuntu 18.04.5 LTS (GNU/Linux 5.4.0-1041-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage
This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

ctf-player@pico-chall$ pwd
/home/ctf-player/drop-in
ctf-player@pico-chall$ ls -la
total 16
drwxr-xr-x 1 ctf-player ctf-player 4096 Mar 16  2021 .
drwxr-xr-x 1 ctf-player ctf-player 4096 Feb 21 20:46 ..
-rw-r--r-- 1 ctf-player ctf-player   14 Mar 16  2021 1of3.flag.txt
-rw-r--r-- 1 ctf-player ctf-player   56 Mar 16  2021 instructions-to-2of3.txt
```

Using basic linux commands we can take a look at where we are currently located at in the filesystem. (`pwd`) <br/>
Another basic command is `ls` with the parameters `-la` to list a directory, in this case the one we are located at right now. <br/>
```sh
ctf-player@pico-chall$ cat 1of3.flag.txt 
picoCTF{xxsh_
ctf-player@pico-chall$ cat instructions-to-2of3.txt 
Next, go to the root of all things, more succinctly `/`
```

Using `cat` we are able to read the contents of the file `1of3.flag.txt` which is the first part of our flag. <br/>
By reading the instructions we now know that we need to navigate to the root of the filesystem. <br/>
```sh
ctf-player@pico-chall$ ls -la /
total 92
drwxr-xr-x   1 root root 4096 Feb 21 20:45 .
drwxr-xr-x   1 root root 4096 Feb 21 20:45 ..
-rwxr-xr-x   1 root root    0 Feb 21 20:45 .dockerenv
-rw-r--r--   1 root root   17 Mar 16  2021 2of3.flag.txt
drwxr-xr-x   1 root root 4096 Mar 16  2021 bin
drwxr-xr-x   2 root root 4096 Apr 24  2018 boot
drwxr-xr-x   5 root root  340 Feb 21 20:45 dev
drwxr-xr-x   1 root root 4096 Feb 21 20:45 etc
drwxr-xr-x   1 root root 4096 Mar 16  2021 home
-rw-r--r--   1 root root   51 Mar 16  2021 instructions-to-3of3.txt
drwxr-xr-x   1 root root 4096 Mar 16  2021 lib
drwxr-xr-x   2 root root 4096 Feb 22  2021 lib64
drwxr-xr-x   2 root root 4096 Feb 22  2021 media
drwxr-xr-x   2 root root 4096 Feb 22  2021 mnt
drwxr-xr-x   1 root root 4096 Mar 16  2021 opt
dr-xr-xr-x 191 root root    0 Feb 21 20:45 proc
drwx------   2 root root 4096 Feb 22  2021 root
drwxr-xr-x   1 root root 4096 Feb 21 20:46 run
drwxr-xr-x   1 root root 4096 Mar 16  2021 sbin
drwxr-xr-x   2 root root 4096 Feb 22  2021 srv
dr-xr-xr-x  13 root root    0 Feb 21 20:45 sys
drwxrwxrwt   1 root root 4096 Mar 16  2021 tmp
drwxr-xr-x   1 root root 4096 Feb 22  2021 usr
drwxr-xr-x   1 root root 4096 Feb 22  2021 var
ctf-player@pico-chall$ cat /2of3.flag.txt 
0ut_0f_\/\/4t3r_
ctf-player@pico-chall$ cat /instructions-to-3of3.txt 
Lastly, ctf-player, go home... more succinctly `~`
```

We start off again by listing the root directory with the command `ls -la /`. <br/>
Using `cat /2of3.flag.txt` we are able to read the second part of the flag `0ut_0f_\/\/4t3r_`. <br/>
By reading the next instructions we know the location of the last flag-piece. <br/>
```sh
ctf-player@pico-chall$ ls -la ~/
total 32
drwxr-xr-x 1 ctf-player ctf-player 4096 Feb 21 20:46 .
drwxr-xr-x 1 root       root       4096 Mar 16  2021 ..
drwx------ 2 ctf-player ctf-player 4096 Feb 21 20:46 .cache
-rw-r--r-- 1 ctf-player ctf-player   80 Mar 16  2021 .profile
drw------- 1 ctf-player ctf-player 4096 Mar 16  2021 .ssh
-rw-r--r-- 1 ctf-player ctf-player   10 Mar 16  2021 3of3.flag.txt
drwxr-xr-x 1 ctf-player ctf-player 4096 Mar 16  2021 drop-in
ctf-player@pico-chall$ cat ~/3of3.flag.txt 
540e4e79}
```

Doing this process once again we obtained the last piece. <br/>
Putting the parts together we get `picoCTF{xxsh_0ut_0f_\/\/4t3r_540e4e79}` which concludes this writeup.