# Encrypted Flag
enc_flag = 'd24fe00395d364e12ea4ca4b9f2da4ca6f9a24b2ca729a399efb2cd873b3ca7d9d1fb3a66a9b73a5b43e8f3d'

# Key is only 5 bytes in size so we dont need more of the prefix GPNCTF{
FLAG_PREFIX = 'GPNCT' 

dec_enc_flag = bytes.fromhex(enc_flag)

# Decode array from encoded bytes
decoded_list = [byte for byte in dec_enc_flag]

# Derive the key from known Flag-Prefix GPNCTF{ using XOR on the known result(decoded array above) and base(decimal value of G,P,N,C,T)
key = [a ^ b for a, b in zip([ord(i) for i in FLAG_PREFIX], [i for i in decoded_list[:5]])]

# Reverse-XOR Operations to derive the decimal values of the original flag
flag_digits = [a ^ key[b] for a, b in zip(decoded_list,[i % 5 for i in range(0, int(len(enc_flag) / 2))])]

# Convert Numbers to ASCII-Characters/Letters
flag = [chr(i) for i in flag_digits]

# Print flag parsed together from above array
print("".join(flag))