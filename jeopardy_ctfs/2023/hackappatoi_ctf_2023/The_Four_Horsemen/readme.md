# The Four Horsemen

## Provided Files
`thefourhorsemen`

## Writeup

Starting off I took a look at the binary with ghidra. <br/>
Looking at the main function I instantly saw some hardcoded hex strings. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/55ccd272-e518-46e1-9ba0-b90a5e2024a8)

Looking at the provided `C` code we can basically throw away everything but the hex strings. <br/>
```c
void FUN_001011c9(void)

{
  long in_FS_OFFSET;
  uint local_3c;
  undefined8 local_38;
  undefined8 local_30;
  undefined8 local_28;
  undefined8 local_20;
  undefined8 local_18;
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  local_38 = 0x68626c7b73677075;
  local_30 = 0x6c716e72655f7265;
  local_28 = 0x636267665f62675f;
  local_20 = 0x62636e5f7275675f;
  local_18 = 0x7d7266636c796e70;
  for (local_3c = 0; local_3c < 0x28; local_3c = local_3c + 1) {
    putchar((int)*(char *)((long)&local_38 + (long)(int)local_3c));
  }
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}
```

Decrypting them in CyberChef we get the following result: <br/>
```
0x68626c7b73677075
0x6c716e72655f7265
0x636267665f62675f
0x62636e5f7275675f
0x7d7266636c796e70

hctf{you
re_ready
_to_stop
_the_apo
calypse}
```

Putting this string together we obtain `hctf{youre_ready_to_stop_the_apocalypse}` which concludes the challenge. 

