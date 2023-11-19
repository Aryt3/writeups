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