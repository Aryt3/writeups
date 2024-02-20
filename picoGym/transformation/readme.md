# Transformation

## Description
```
I wonder what this really is... ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
```

## Provided Files
```
- enc
```

## Writeup

Starting off we should take a look at the provided file and the code in the description. <br/>
Content of `enc`:
```
灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥㜰㍢㐸㙽
```

Taking a look at those characters you can see that those are chinese characters, but before further going into that we should analyze the provided code. <br/>
```py
''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
```

Now what is this code doing? Let's split it up to have a better view. <br/>
```py
flag = '?'

output = ''

for i in range(0, len(flag), 2):
    output += chr((ord(flag[i]) << 8) + ord(flag[i + 1]))
```

Now analyzing this we see that the python code loops through the string `flag` in pairs of `2`. <br/>
The first letter will actually be transformed from `letter` to `ASCII-value`. The `ASCII-value` will than be shifted bitwise to the left using `<<`. <br/>

Example: <br/>
```py
ord('a') # result is 97
ord('a') << 8 # result is 24832
```

The value `97` will be multiplied with `256`(2^8). <br/>
The `ASCII-value` of the second letter will also be calculated using `ord(flag[i + 1])`. <br/>
The values will than be a aggregated meaning `ord('a') << 8` + `ord(flag[i + 1])`. <br/>
In the end we get a value like `28777`(using 'p' and 'i' in the code above) which returns the string `灩`(`chr(28777)`). <br/>
Seeing that we were able to replicate the first letter of the encrypted message we can try to make a solution script. <br/>
```py
# Open file with encrypted flag
with open('enc', 'rb') as file:
    encrypted_flag = file.read().decode('utf-8') # default encdoing utf-8 (unicode transformation format)

# Possible chars used in the flag
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ{}1234567890_'
flag = ''

# Possible values for ord(character) << 8
possible_result_values = [ord(char) << 8 for char in chars]

# Ascii representation of every char, ord(character)
char_values = [ord(char) for char in chars]

# Check if ord(character) from encrypted text can be found fusing known values
for char in encrypted_flag:
    for possible_index, x in enumerate(possible_result_values):
        for char_index, y in enumerate(char_values):
            if x + y == ord(char):
                flag += f'{chr(possible_result_values[possible_index] >> 8)}{chr(char_values[char_index])}'

print(flag)
```

In the script we define all possible characters of the flag, `lowercase letter`, `uppercase letters`, `integers`, `special charatcers` like `{`, `}` and `_`. <br/>
We can than get the value of every character in the `enc` file and check if we can guess the character combinations. <br/>
Running the script reveals the flag to us which concludes this writeup. <br/>
```sh
$ python3 ./solve.py
picoCTF{16_bits_inst34d_of_8_e703b486}
```