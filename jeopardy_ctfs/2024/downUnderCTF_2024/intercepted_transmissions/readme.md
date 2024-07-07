# Intercepted Transmissions

## Description
```
Those monsters! They've kidnapped the Quokkas! Who in their right mind would capture those friendly little guys.. We've managed to intercept a CCIR476 transmission from the kidnappers, we think it contains the location of our friends! Can you help us decode it? We managed to decode the first two characters as '##'

NOTE: Wrap the decoded message in DUCTF{}.
```

## Provided Files
```
- encoding
```

## Writeup

Contents of provided file: <br/>
```
101101001101101101001110100110110101110100110100101101101010110101110010110100101110100111001101100101101101101000111100011110011011010101011001011101101010010111011100100011110101010110110101011010111001011010110100101101101010110101101011001011010011101110001101100101110101101010110011011100001101101101101010101101101000111010110110010111010110101100101100110111101000101011101110001101101101001010111001011101110001010111001011100011011
```

Now the important part of this challenge was to carefully read the description and notice `CCIR476` which is a character encoding used by radios. <br/>
From there we searched for decoders where we found the following [github-repo](https://github.com/AI5GW/CCIR476/blob/main/src/CCIR476.cpp). <br/>
Using the found mapping inside the `cpp` file and the information on the [Wikipedia-page](https://en.wikipedia.org/wiki/CCIR_476) that it is a `7` bit code I made a script which maps the `binary` to `ascii-chars`. <br/>
```py
enc_str = '101101001101101101001110100110110101110100110100101101101010110101110010110100101110100111001101100101101101101000111100011110011011010101011001011101101010010111011100100011110101010110110101011010111001011010110100101101101010110101101011001011010011101110001101100101110101101010110011011100001101101101101010101101101000111010110110010111010110101100101100110111101000101011101110001101101101001010111001011101110001010111001011100011011'

split_by_bits = 7

split_binary = [enc_str[i:i+split_by_bits] for i in range(0, len(enc_str), split_by_bits)]

# Convert from binary to decimal (Not Ascii-values -> custom mapping)
flag = [int(i, 2) for i in split_binary]

out1 = '''case '0': { CCIR_MODE = 0; return 0x2D; }
case '1': { CCIR_MODE = 0; return 0x2E; }
case '2': { CCIR_MODE = 0; return 0x27; }
case '3': { CCIR_MODE = 0; return 0x56; }
case '4': { CCIR_MODE = 0; return 0x55; }
case '5': { CCIR_MODE = 0; return 0x74; }
case '6': { CCIR_MODE = 0; return 0x2B; }
case '7': { CCIR_MODE = 0; return 0x4E; }
case '8': { CCIR_MODE = 0; return 0x4D; }
case '9': { CCIR_MODE = 0; return 0x71; }     
case '\'': { CCIR_MODE = 0; return 0x17; }      
case '!': { CCIR_MODE = 0; return 0x1B; }
case ':': { CCIR_MODE = 0; return 0x1D; }
case '(': { CCIR_MODE = 0; return 0x1E; }
case '&': { CCIR_MODE = 0; return 0x35; }
case '.': { CCIR_MODE = 0; return 0x39; }
case '/': { CCIR_MODE = 0; return 0x3A; }
case '=': { CCIR_MODE = 0; return 0x3C; }
case '-': { CCIR_MODE = 0; return 0x47; }
case '$': { CCIR_MODE = 0; return 0x53; }
case ',': { CCIR_MODE = 0; return 0x59; }
case '+': { CCIR_MODE = 0; return 0x63; }
case ')': { CCIR_MODE = 0; return 0x65; }
case '#': { CCIR_MODE = 0; return 0x69; }
case '?': { CCIR_MODE = 0; return 0x72; }'''

out2 = '''case 0x47: { return 'A'; }  
case 0x72: { return 'B'; }
case 0x1D: { return 'C'; }
case 0x53: { return 'D'; }
case 0x56: { return 'E'; }
case 0x1B: { return 'F'; }
case 0x35: { return 'G'; }
case 0x69: { return 'H'; }
case 0x4D: { return 'I'; }
case 0x17: { return 'J'; }
case 0x1E: { return 'K'; }
case 0x65: { return 'L'; }
case 0x39: { return 'M'; }
case 0x59: { return 'N'; }
case 0x71: { return 'O'; }
case 0x2D: { return 'P'; }
case 0x2E: { return 'Q'; }
case 0x55: { return 'R'; }
case 0x4B: { return 'S'; }
case 0x74: { return 'T'; }
case 0x4E: { return 'U'; }
case 0x3C: { return 'V'; }
case 0x27: { return 'W'; }
case 0x3A: { return 'X'; }
case 0x2B: { return 'Y'; }
case 0x63: { return 'Z'; }'''

number_mapping = out1.split('\n')
letter_mapping = out2.split('\n')

mapping2 = {}

for i in letter_mapping:
    char = i.split("return '")[1].split("';")[0]
    hex_char = i.split("case ")[1].split(":")[0]

    mapping2[int(hex_char, 16)] = char

mapping = {}

for i in number_mapping:
    char = i.split("case '")[1].split("':")[0]
    hex_char = i.split("return ")[1].split(";")[0]

    mapping[int(hex_char, 16)] = char


viable_out = ''

letters = True

for i in flag:
    if i == 54:
        letters = False
    elif i == 90:
        letters = True
    else:
        if letters == True:
            if i in mapping2:
                viable_out += mapping2[i]
        else:
            if i in mapping:
                viable_out += mapping[i]

print(viable_out)
```

The encoding uses a switch to change between `letters` and `numbers + speical chars`. <br/>
Using the script returned something which looked like a flag. <br/>
```sh
$ python3 solve.py 
##TH3QU0KK4SAR3H3LD1NF4C1LITY#11911!
```

Sadly it wasn't the actual flag but with some tinkering (adding spaces and ') we finally found the required flag `DUCTF{##TH3 QU0KK4'S AR3 H3LD 1N F4C1LITY #11911!}` which concludes this writeup. 