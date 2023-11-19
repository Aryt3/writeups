# Flag Checker

## Description
```
Can you beat this FlagChecker?
```

## Provided Files
```
flagchecker [binary]
source.rs
```

## Writeup

Taking a look at the `source.rs` file. <br/>
```rs
use std::io;

fn check_flag(flag: &str) -> bool {
    flag.as_bytes()[18] as i32 * flag.as_bytes()[7] as i32 & flag.as_bytes()[12] as i32 ^ flag.as_bytes()[2] as i32 == 36 &&
    flag.as_bytes()[1] as i32 % flag.as_bytes()[14] as i32 - flag.as_bytes()[21] as i32 % flag.as_bytes()[15] as i32 == -3 &&
    flag.as_bytes()[10] as i32 + flag.as_bytes()[4] as i32 * flag.as_bytes()[11] as i32 - flag.as_bytes()[20] as i32 == 5141 &&
    flag.as_bytes()[19] as i32 + flag.as_bytes()[12] as i32 * flag.as_bytes()[0] as i32 ^ flag.as_bytes()[16] as i32 == 8332 &&
    flag.as_bytes()[9] as i32 ^ flag.as_bytes()[13] as i32 * flag.as_bytes()[8] as i32 & flag.as_bytes()[16] as i32 == 113 &&
    flag.as_bytes()[3] as i32 * flag.as_bytes()[17] as i32 + flag.as_bytes()[5] as i32 + flag.as_bytes()[6] as i32 == 7090 &&
    flag.as_bytes()[21] as i32 * flag.as_bytes()[2] as i32 ^ flag.as_bytes()[3] as i32 ^ flag.as_bytes()[19] as i32 == 10521 &&
    flag.as_bytes()[11] as i32 ^ flag.as_bytes()[20] as i32 * flag.as_bytes()[1] as i32 + flag.as_bytes()[6] as i32 == 6787 &&
    flag.as_bytes()[7] as i32 + flag.as_bytes()[5] as i32 - flag.as_bytes()[18] as i32 & flag.as_bytes()[9] as i32 == 96 &&
    flag.as_bytes()[12] as i32 * flag.as_bytes()[8] as i32 - flag.as_bytes()[10] as i32 + flag.as_bytes()[4] as i32 == 8277 &&
    flag.as_bytes()[16] as i32 ^ flag.as_bytes()[17] as i32 * flag.as_bytes()[13] as i32 + flag.as_bytes()[14] as i32 == 4986 &&
    flag.as_bytes()[0] as i32 * flag.as_bytes()[15] as i32 + flag.as_bytes()[3] as i32 == 7008 &&
    flag.as_bytes()[13] as i32 + flag.as_bytes()[18] as i32 * flag.as_bytes()[2] as i32 & flag.as_bytes()[5] as i32 ^ flag.as_bytes()[10] as i32 == 118 &&
    flag.as_bytes()[0] as i32 % flag.as_bytes()[12] as i32 - flag.as_bytes()[19] as i32 % flag.as_bytes()[7] as i32 == 73 &&
    flag.as_bytes()[14] as i32 + flag.as_bytes()[21] as i32 * flag.as_bytes()[16] as i32 - flag.as_bytes()[8] as i32 == 11228 &&
    flag.as_bytes()[3] as i32 + flag.as_bytes()[17] as i32 * flag.as_bytes()[9] as i32 ^ flag.as_bytes()[11] as i32 == 11686 &&
    flag.as_bytes()[15] as i32 ^ flag.as_bytes()[4] as i32 * flag.as_bytes()[20] as i32 & flag.as_bytes()[1] as i32 == 95 &&
    flag.as_bytes()[6] as i32 * flag.as_bytes()[12] as i32 + flag.as_bytes()[19] as i32 + flag.as_bytes()[2] as i32 == 8490 &&
    flag.as_bytes()[7] as i32 * flag.as_bytes()[5] as i32 ^ flag.as_bytes()[10] as i32 ^ flag.as_bytes()[0] as i32 == 6869 &&
    flag.as_bytes()[21] as i32 ^ flag.as_bytes()[13] as i32 * flag.as_bytes()[15] as i32 + flag.as_bytes()[11] as i32 == 4936 &&
    flag.as_bytes()[16] as i32 + flag.as_bytes()[20] as i32 - flag.as_bytes()[3] as i32 & flag.as_bytes()[9] as i32 == 104 &&
    flag.as_bytes()[18] as i32 * flag.as_bytes()[1] as i32 - flag.as_bytes()[4] as i32 + flag.as_bytes()[14] as i32 == 5440 &&
    flag.as_bytes()[8] as i32 ^ flag.as_bytes()[6] as i32 * flag.as_bytes()[17] as i32 + flag.as_bytes()[12] as i32 == 7104 &&
    flag.as_bytes()[11] as i32 * flag.as_bytes()[2] as i32 + flag.as_bytes()[15] as i32 == 6143
}

fn main() {
    let mut flag = String::new();
    println!("Enter the flag: ");
    io::stdin().read_line(&mut flag).expect("Failed to read line");
    let flag = flag.trim();

    if check_flag(flag) {
        println!("Correct flag");
    } else {
        println!("Wrong flag");
    }
}
```

Taking a look at this I instantly knew that this basically checks if I input the correct flag. <br/>
My first thoughts were that the only thing I can start off is the flag format `INTIGRITI{...}`. <br/>

Knowing this I could basically map the first few letters and looking at the code it would basically convert the letters to the `ASCII` numbers. <br/>
Having this information I converted the equations to python code and wrote a little script to solve the equations and receive a flag. <br/>
```py
import re

equations = [
    'flag[18] * flag[7] & flag[12] ^ flag[2] == 36',
    'flag[1] % flag[14] - flag[21] % flag[15] == -3',
    'flag[10] + flag[4] * flag[11] - flag[20] == 5141',
    'flag[19] + flag[12] * flag[0] ^ flag[16] == 8332',
    'flag[9] ^ flag[13] * flag[8] & flag[16] == 113',
    'flag[3] * flag[17] + flag[5] + flag[6] == 7090',
    'flag[21] * flag[2] ^ flag[3] ^ flag[19] == 10521',
    'flag[11] ^ flag[20] * flag[1] + flag[6] == 6787',
    'flag[7] + flag[5] - flag[18] & flag[9] == 96',
    'flag[12] * flag[8] - flag[10] + flag[4] == 8277',
    'flag[16] ^ flag[17] * flag[13] + flag[14] == 4986',
    'flag[0] * flag[15] + flag[3] == 7008',
    'flag[13] + flag[18] * flag[2] & flag[5] ^ flag[10] == 118',
    'flag[0] % flag[12] - flag[19] % flag[7] == 73',
    'flag[14] + flag[21] * flag[16] - flag[8] == 11228',
    'flag[3] + flag[17] * flag[9] ^ flag[11] == 11686',
    'flag[15] ^ flag[4] * flag[20] & flag[1] == 95',
    'flag[6] * flag[12] + flag[19] + flag[2] == 8490',
    'flag[7] * flag[5] ^ flag[10] ^ flag[0] == 6869',
    'flag[21] ^ flag[13] * flag[15] + flag[11] == 4936',
    'flag[16] + flag[20] - flag[3] & flag[9] == 104',
    'flag[18] * flag[1] - flag[4] + flag[14] == 5440',
    'flag[8] ^ flag[6] * flag[17] + flag[12] == 7104',
    'flag[11] * flag[2] + flag[15] == 6143'
]

def find_flag():
    flag_len = 22
    flag = [0] * flag_len

    # Set initial values for the first few characters
    flag[:10] = map(ord, "INTIGRITI{")
    flag[21] = 125

    while 0 in flag:
        for equation in equations:
            missing_char = None
            counter = 0
            flag_occurrences = re.findall(r'flag\[\d+\]', equation)
            for piece in flag_occurrences:
                index = int(re.search(r'\d+', piece).group())
                value = flag[index]
                if value == 0:
                    match = re.match(r'flag\[(\d+)\]', piece)
                    if match:
                        missing_char = match.group(1)
                    counter += 1
            
            if counter == 1 and missing_char is not None:
                modified_equation = re.sub(fr'flag\[{missing_char}\]', "candidate", equation)
                
                for candidate in range(ord(' '), ord('~') + 1):
                    # Replace "candidate" in the equation with the actual candidate value
                    candidate_equation = modified_equation.replace("candidate", str(candidate))

                    # Evaluate the modified equation
                    result = eval(candidate_equation)

                    if result:
                        print("flag[" + str(missing_char) + "] = " + str(candidate))
                        flag[int(missing_char)] = candidate
                        break
                else:
                    print("No solution found for the given equation.")

    ascii_characters = [chr(num) for num in flag]
    result_string = ''.join(ascii_characters)
    print(flag)
    print(result_string)

    return None

result = find_flag()
```

Converting the equatiosn was easy I only needed to delete every occurance of `.as_bytes()` and ` as i32`. <br/>
The script basically works by checking if there is only 1 unknown value in an equation and than proceed to sovle this equation to get the unknown value. <br/>
Executing the script: <br/>
```sh
kali@kali python3 .\solving.py
flag[17] = 95
flag[19] = 84
flag[18] = 66
flag[15] = 95
flag[12] = 74
flag[11] = 72
flag[20] = 71
flag[10] = 116
flag[13] = 51
flag[16] = 106
flag[14] = 51
[73, 78, 84, 73, 71, 82, 73, 84, 73, 123, 116, 72, 74, 51, 51, 95, 106, 95, 66, 84, 71, 125]
INTIGRITI{tHJ33_j_BTG}
```

Trying to input the flag it seems as if some parts of it are wrong. <br/>
I instantly realised the issue, the problem was the some equations can actually have multiple results because of the `XOR` and `AND`. <br/> 

To solve the issue I thought that I could bruteforce the parts of the flag I wasn't sure about. <br/>
Remembering that we can just use the binary we got from the challenge we can just try every different flag. <br/>
So I wrote another small python script to bruteforce the following characters I wasn't sure about `INTIGRITI{tHJ33_X_XTX}`. <br/>
```py
import subprocess, time

binary_path = "/home/kali/Desktop/flagchecker"
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!§$%&/()?_*#"

start_time = time.time()

for first_char in characters:
    for second_char in characters:
        for third_char in characters:
            flag = f"INTIGRITI{{tHr33_{first_char}_{second_char}T{third_char}}}"
            
            command = [binary_path]

            try:
                result = subprocess.run(command, input=flag, text=True, capture_output=True, check=True)

                print(f"Trying flag: {flag}", end='\r')

                if "Wrong flag" not in result.stdout:
                    print(f"Found the correct flag: {flag}")

                    end_time = time.time()
                    elapsed_time = end_time - start_time

                    print(f"\nTotal time taken: {elapsed_time:.2f} seconds")
                    exit() 

            except subprocess.CalledProcessError as e:
                print(f"Error executing with flag {flag}: {e}")
```

Bruteforcing the flag: <br/>
```sh
kali@kali python3 bruteforce_flag.py 
Found the correct flag: INTIGRITI{tHr33_Z_FTW}

Total time taken: 78.03 seconds
```

Like this we found the correct flag to finish this challenge. 