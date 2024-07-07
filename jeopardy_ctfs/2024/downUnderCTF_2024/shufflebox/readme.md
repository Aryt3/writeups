# shufflebox

## Description
```
I've learned that if you shuffle your text, it's elrlay hrda to tlle htaw eht nioiglra nutpi aws.

Find the text censored with question marks in output_censored.txt and surround it with DUCTF{}.

Author: hashkitten
```

## Provided Files
```
- shufflebox.py
- output_censored.txt
```

## Writeup

Starting off by looking at provided files. <br/>
```py
import random

PERM = list(range(16))
random.shuffle(PERM)

def apply_perm(s):
    assert len(s) == 16
    return ''.join(s[PERM[p]] for p in range(16))

for line in open(0):
    line = line.strip()
    print(line, '->', apply_perm(line))
```

```txt
aaaabbbbccccdddd -> ccaccdabdbdbbada
abcdabcdabcdabcd -> bcaadbdcdbcdacab
???????????????? -> owuwspdgrtejiiud
```

The script essentially takes an input string with the length being exactly 16 characters long. <br/>
It then randomly shuffles the characters which can be seen in the input and output strings above. <br/>
Knowing this we can take the input strings and map all possible locations from each character. <br/>
```py
input_str = aaaabbbbccccdddd

# the first char "a" could be in positions 3,7,14,16
output_str = cc a ccd a bdbdbb a d a
```

Using this logic on both strings we have we can then filter out the equal positions and extract the correct mapping of the used shuffling method. <br/>
```py
# aaaabbbbccccdddd -> ccaccdabdbdbbada
# abcdabcdabcdabcd -> bcaadbdcdbcdacab

str_1, str_2, res_1, res_2 = 'aaaabbbbccccdddd', 'abcdabcdabcdabcd', 'ccaccdabdbdbbada', 'bcaadbdcdbcdacab'

flag_str = list('owuwspdgrtejiiud')

str_1_dict, str_2_dict, out_dict, pos_pos = {}, {}, {}, {}

## Get possible positions for char shuffling
for i1, char in enumerate(str_1):
    str_1_dict[i1] = []

    # Loop through result string to map possible positions of current character
    for i2, x in enumerate(res_1):
        if x == char:
            str_1_dict[i1].append(i2)

## Get possible positions for char shuffling
for i1, char in enumerate(str_2):
    str_2_dict[i1] = []

    # Loop through result string to map possible positions of current character
    for i2, x in enumerate(res_2):
        if x == char:
            str_2_dict[i1].append(i2)

## Compare chars to get correct position
for i in range(len(str_1_dict)):
    pos_pos[i] = []

    for x in str_1_dict[i]:
        if x in str_2_dict[i]:
            pos_pos[i].append(x)

for i in pos_pos:
    out_dict[i] = flag_str[pos_pos[i][0]]

print("".join([out_dict[i] for i in out_dict]))
```