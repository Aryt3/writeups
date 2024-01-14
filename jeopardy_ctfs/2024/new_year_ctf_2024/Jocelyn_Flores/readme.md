# Jocelyn Flores

## Description
```
I know you so well, so well
I mean, I can do anything that he can
I've been pretty—
```

## Provided Files
`jf.pyc` <br/>
`jocelyn_flores`

## Writeup

Decompiling the `jf.pyc` file online I obtained the actual code. <br/>
```py
import random

flag = input('>')

seed = random.randint(1, 1000)
random.seed(seed)

flag = list(flag)
random.shuffle(flag)
flag = ''.join(flag)
print(flag)
```

The `jocelyn_flores` file seemed to contain the shuffled flag. <br/>
```
}r3,_oeL'_lNS1NIfNF____0pnGjl3eo1APbN_tilB_H10{IdlN33_L'4l_uoggT_D
```

Now this script simply takes any input and than uses a random seet between 1 and 1000 which is than being used to randomly shuffle the actual input. <br/>
Reversing this is pretty easy as we can just bruteforce the seed and check if the flag prefix is in the output. <br/>
For this purpose I wrote a small python script. <br/>
```py
import random

# shuffled flag
shuffled_flag = "}r3,_oeL'_lNS1NIfNF____0pnGjl3eo1APbN_tilB_H10{IdlN33_L'4l_uoggT_D"
shuffled_list = list(shuffled_flag)

# for-loop to bruteforce correct seed
for i in range(1, 1001):
    # iniate seed
    random.seed(i)

    # shuffle 1 time to recreate original shuffle with provided seed
    indices = list(range(len(shuffled_list)))
    random.shuffle(indices)

    # use indices to reverse the shuffle
    reversed_list = [None] * len(shuffled_list)
    for i, j in zip(indices, range(len(shuffled_list))):
        reversed_list[i] = shuffled_list[j]

    # parse reversed list back into a string
    reversed_string = ''.join(reversed_list)

    # check if flag prefix is in string
    if 'grodno{' in reversed_string:
        print(reversed_string)
```

Executing the script I obtained the reversed output. <br/>
```sh
kali@kali python3 .\solve.py

I'll_b3_F33liNg_p41N,_grodno{1'Ll_Be_fe3L1NG_PAIN}_juST_t0_H0lD_oN
```

Obtaining the flag `grodno{1'Ll_Be_fe3L1NG_PAIN}` concludes this writeup. 

