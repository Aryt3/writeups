f = open("msg.enc", "r") # open file
line = f.readlines() # get content of file
f.close() # close file

enc_msg = line[0].strip() # convert file content to correct format

ct = bytes.fromhex(enc_msg) # transform hex to bytes

# decryption function
def decryption(ct):
    msg = [] # define empty array
    for char in ct:
        inverse = pow(123, -1, 256) 
        msg.append((inverse * (char - 18)) % 256) # inverse encryption to decrypt bytes
    return bytes(msg)

decrypted_message = decryption(ct) # Call decryption function with bytes from file-content

print(decrypted_message.decode("utf-8")) # print to cli