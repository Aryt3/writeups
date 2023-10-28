# Quick Maths

## Description
```
I recieved this very weird email that only contained a file called "openme", it looks like an executable.

Can you see if there is anything weird in this file?
```

## Writeup

Starting off we download the provided file `openme`. <br/>
The next thing to do is a simple strings and maybe grep for the flag. <br/>
```sh
kali@kali strings openme | grep NIC        
NICC{leaky_data_huh}
```


