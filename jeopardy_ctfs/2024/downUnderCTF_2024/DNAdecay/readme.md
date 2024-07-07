# DNAdecay

## Description
```
Our flightless birds can run upto 50km/h but we want them to go faster. I've been messing with a mutigen but it seems to have corrupted. Can you help me recover this research?

Author: BootlegSorcery@
```

## Provided Files
```
- dna.rb
```

## Writeup

Starting off I inspected the given file. <br/>
```rb
require "doublehelix"

 AT
A--T
T- -A
G----C
 G---- 
     --C
   T---A
    G--C
     AT
     GC
    T-- 
   G- - 
  T----A
 A--- T
T ---A
G---C
C--G
 AT
 CG
```

Seeing this I researched the `doublehelix` ruby library where I found the [github-repo](https://github.com/mame/doublehelix/). <br/>
The example shows that there are no disconnections in the `-` between the letters. Seeing this I knew I simply had to repair the `dna-string`. <br/>
Used syntax of the library: <br/>
```rb
# Those letter-combinations are possible with either "-" inbetween or not
AT
TA
GC
CG
```

Knowing this I repaired it manually as best as I could. <br/>
Once finished I wrote the script below which bruteforces the used letters by forming the same dna-string until it finds a letter that matches. <br/>
```rb
require "doublehelix"

file_content = File.read('flag.txt')

out = ''

chars = (0..255).map(&:chr)

while true do
    chars.each do |char|
        if file_content.include?(doublehelix(out + char))
        out += char
        puts out
        end
    end
end
```

From this I obtained the flag `puts"DUCTF{7H3_Mit0cHOneRi4o15_7he_P0wEr_HoUqE_of_DA_C3L}` which seemed kind of faulty. <br/>
These were the side effects of guessing certain letter-combinations during repairing where neither of both letters were given. <br/>
To fix this I searched for the phrase online and found it. <br/>
```rb
# Searching in browser reveals:
------the-mitochondria-is-the-powerhouse-of-the-cell-

# mapping the above below:
DUCTF{7H3_Mit0cHOndRi4_15_7he_P0wEr_HoUsE_of_DA_C3LL}
```

Mapping the above below revealed the real flag which concludes this writeup. 