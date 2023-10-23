# Chicken Wings

## Description
```
I was reading a report on past Trickbot malware, and I found this sample that looks a lot like their code! Can you make any sense of it? 

Provided File: batchfuscation
```

## Writeup
Starting off with the challenge I guessed that it was a .bat file which was provided. <br/>
Taking a look at the content I verified this as I saw an `@echo` and a environmental variable call using %env_var% which are both indicators for batch files. <br/>

Taking a look at the content itself may be hard because it's obfuscated. <br/>
```bat
@echo off
set bdevq=set
%bdevq% grfxdh= 
%bdevq%%grfxdh%mbbzmk==
%bdevq%%grfxdh%xeegh%mbbzmk%/
%bdevq%%grfxdh%jeuudks%mbbzmk%a
%bdevq%%grfxdh%rbiky%mbbzmk%c
%bdevq%%grfxdh%wzirk%mbbzmk%m
%bdevq%%grfxdh%naikpbo%mbbzmk%d
%bdevq%%grfxdh%ltevposie%mbbzmk%e
%bdevq%%grfxdh%uqcqswo%mbbzmk%x
%bdevq%%grfxdh%zvipzis%mbbzmk%i
%bdevq%%grfxdh%kquqjy%mbbzmk%t
%bdevq%%grfxdh%kmgnxdhqb%mbbzmk% 
%bdevq%%grfxdh%%xeegh%%jeuudks%%grfxdh%bpquuu%mbbzmk%4941956 %% 4941859
%rbiky%%wzirk%%naikpbo%%kmgnxdhqb%%xeegh%%rbiky%%kmgnxdhqb%%ltevposie%%uqcqswo%%zvipzis%%kquqjy%%kmgnxdhqb%%bpquuu%
```

Running the file doesn't output anything, this is of course because `@echo off` turns this off. <br/>
Turning it to `on` we can pipe the output into a file using `batchfuscation.bat > output.txt`. <br/>

Searching for flag in the `output.txt` we gain multiple results like the one below. <br/>
```bat
rem set fpxkxvovkjkbqetregflagenwrrujhqlbucr=bwiannsetinyqipqyyerfppukhzqjpugogktrlqzybzijbhcsvhoiksgelgryr 
```

Now knowing a little bit of batch syntax I know that `rem` is equal to `#` in python so it's trashing my output file and nothing else. <br/>
Also it seems that some deobfuscation is needed to actually reveal the flag. <br/>

Now let's do some deobfuscatibg. <br/>
```bat
@echo off
set bdevq=set
%bdevq% grfxdh= 
%bdevq%%grfxdh%mbbzmk==
%bdevq%%grfxdh%xeegh%mbbzmk%/
%bdevq%%grfxdh%jeuudks%mbbzmk%a
%bdevq%%grfxdh%rbiky%mbbzmk%c
%bdevq%%grfxdh%wzirk%mbbzmk%m
%bdevq%%grfxdh%naikpbo%mbbzmk%d
%bdevq%%grfxdh%ltevposie%mbbzmk%e
%bdevq%%grfxdh%uqcqswo%mbbzmk%x
%bdevq%%grfxdh%zvipzis%mbbzmk%i
%bdevq%%grfxdh%kquqjy%mbbzmk%t
%bdevq%%grfxdh%kmgnxdhqb%mbbzmk% 
```

doing the following deobfuscating steps.

