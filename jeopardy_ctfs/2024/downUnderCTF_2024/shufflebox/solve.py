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