# CSS Password

## Description
```
My web developer friend said JavaScript is insecure so he made a password vault with CSS. 
Can you find the password to open the vault?

Wrap the flag in uoftctf{}

Make sure to use a browser that supports the CSS :has selector, such as Firefox 121+ or Chrome 105+. 
The challenge is verified to work for Firefox 121.0.

Author: notnotpuns
```

## Provided Files
`css-password.html`

## Writeup

Taking a look at the provided `html` file. <br/>
![image](https://github.com/Aryt3/writeups/assets/110562298/7916a21f-7b42-481e-b4df-49564a6e9b62)

Now looking at the provided file we can't see any javascript just some css and html. <br/>
After further analysis I found that there are basically `if statements` in the css. <br/>
Also we need to keep the instruction on the website in mind `The password is correct when all LEDs turn green`. <br/>
Knowing this I looked at the css and found some interesting comments. <br/>
```css
/* LED4 */
/* b5_7_l4_c1 */
.wrapper:has(.byte:nth-child(5) .latch:nth-child(7) .latch__reset:active) .checker:nth-of-type(5) .checker__state:nth-child(1) {
    transform: translateX(-100%);
    transition: transform 0s;
}

.wrapper:has(.byte:nth-child(5) .latch:nth-child(7) .latch__set:active) .checker:nth-of-type(5) .checker__state:nth-child(1) {
    transform: translateX(0%);
    transition: transform 0s;
}

/* b5_8_l4_c2 */
.wrapper:has(.byte:nth-child(5) .latch:nth-child(8) .latch__reset:active) .checker:nth-of-type(5) .checker__state:nth-child(2) {
    transform: translateX(-100%);
    transition: transform 0s;
}

.wrapper:has(.byte:nth-child(5) .latch:nth-child(8) .latch__set:active) .checker:nth-of-type(5) .checker__state:nth-child(2) {
    transform: translateX(0%);
    transition: transform 0s;
}

/* b6_7_l4_c3 */
.wrapper:has(.byte:nth-child(6) .latch:nth-child(7) .latch__reset:active) .checker:nth-of-type(5) .checker__state:nth-child(3) {
    transform: translateX(-100%);
    transition: transform 0s;
}

.wrapper:has(.byte:nth-child(6) .latch:nth-child(7) .latch__set:active) .checker:nth-of-type(5) .checker__state:nth-child(3) {
    transform: translateX(0%);
    transition: transform 0s;
}

/* b6_8_l4_c4 */
.wrapper:has(.byte:nth-child(6) .latch:nth-child(8) .latch__reset:active) .checker:nth-of-type(5) .checker__state:nth-child(4) {
    transform: translateX(-100%);
    transition: transform 0s;
}

.wrapper:has(.byte:nth-child(6) .latch:nth-child(8) .latch__set:active) .checker:nth-of-type(5) .checker__state:nth-child(4) {
    transform: translateX(0%);
    transition: transform 0s;
}

/* b19_7_l4_c5 */
.wrapper:has(.byte:nth-child(19) .latch:nth-child(7) .latch__reset:active) .checker:nth-of-type(5) .checker__state:nth-child(5) {
    transform: translateX(-100%);
    transition: transform 0s;
}

.wrapper:has(.byte:nth-child(19) .latch:nth-child(7) .latch__set:active) .checker:nth-of-type(5) .checker__state:nth-child(5) {
    transform: translateX(0%);
    transition: transform 0s;
}

/* b19_8_l4_c6 */
.wrapper:has(.byte:nth-child(19) .latch:nth-child(8) .latch__reset:active) .checker:nth-of-type(5) .checker__state:nth-child(6) {
    transform: translateX(-100%);
    transition: transform 0s;
}

.wrapper:has(.byte:nth-child(19) .latch:nth-child(8) .latch__set:active) .checker:nth-of-type(5) .checker__state:nth-child(6) {
    transform: translateX(0%);
    transition: transform 0s;
}
```

It seems that I found the `if statements` needed to turn the 4th LED green. <br/>
To check it I tried to turn all the marked positions True and got a green LED as result. <br/>
Knowing that those are really `if statements` I wrote a script to automatically get the result. <br/>
```py
import re

# Copied all css if clauses
css = '''
        /* LED1 */
        /* b1_7_l1_c1 */
        .wrapper:has(.byte:nth-child(1) .latch:nth-child(7) .latch__reset:active) .checker:nth-of-type(2) .checker__state:nth-child(1) {
            transform: translateX(0%);
            transition: transform 0s;
        }
--------------------------------------------
        .wrapper:has(.byte:nth-child(19) .latch:nth-child(6) .latch__set:active) .checker:nth-of-type(6) .checker__state:nth-child(95) {
            transform: translateX(0%);
            transition: transform 0s;
        }
'''

# regex to get byte to edit, position in byte to edit and check if position is 0 or 1
pattern = r'\.byte:nth-child\((\d+)\) \.latch:nth-child\((\d+)\)[\s\S]*?translateX\(([-\d]+)%\)'

# get all if clauses with regex pattern
matches = re.findall(pattern, css)

# create dictionary for values
byte_dict = {}

# fill dictionary with empty values 
for i in range(1, 20):
    inner_dict = {j: False for j in range(1, 9)}
    byte_dict[f'Byte_{i}'] = inner_dict

# initiate var
last_match = (0, 0)

# loop through matches and check if values are either 0/True or 1/False
for match in matches:
    check = (match[0], match[1])
    if last_match != check:
        if match[2] == '-100':
            byte_dict[f'Byte_{match[0]}'][int(match[1])] = True
    last_match = (match[0], match[1])

# declare var to store flag
result = ''

# loop through bytes-dictionary and convert binary to asci
for byte in byte_dict:
    bin_out = ''
    for i in range(1, 9):
        if byte_dict[byte][i] == True:
            bin_out += '0'
        else:
            bin_out += '1'
    
    result += chr(int(bin_out, 2))

print(f"uoftctf{{{result}}}")
```

The script converts the binary to asci characters. <br/>
```sh
kali@kali python3 .\solve.py

uoftctf{CsS_l0g1c_is_fun_3h}
```

Executing the script returns the flag which concludes this writeup. 
