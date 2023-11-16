# The Last Dance

## Description
```
To be accepted into the upper class of the Berford Empire, you had to attend the annual Cha-Cha Ball at the High Court. 
Little did you know that among the many aristocrats invited, you would find a burned enemy spy. 
Your goal quickly became to capture him, which you succeeded in doing after putting something in his drink. 
Many hours passed in your agency's interrogation room, and you eventually learned important information about the enemy agency's secret communications. 
Can you use what you learned to decrypt the rest of the messages?
```

## Writeup

Starting off we are provided the script for encryption and the encrypted data. <br/>
```py
from Crypto.Cipher import ChaCha20
from secret import FLAG
import os

def encryptMessage(message, key, nonce):
    cipher = ChaCha20.new(key=key, nonce=iv)
    ciphertext = cipher.encrypt(message)
    return ciphertext

def writeData(data):
    with open("out.txt", "w") as f:
        f.write(data)

if __name__ == "__main__":
    message = b"Our counter agencies have intercepted your messages and a lot "
    message += b"of your agent's identities have been exposed. In a matter of "
    message += b"days all of them will be captured"

    key, iv = os.urandom(32), os.urandom(12)

    encrypted_message = encryptMessage(message, key, iv)
    encrypted_flag = encryptMessage(FLAG, key, iv)

    data = iv.hex() + "\n" + encrypted_message.hex() + "\n" + encrypted_flag.hex()
    writeData(data)
```

Seems like the encrypted data can be linked to the `writeData(data)` above. <br/>
```hex
c4a66edfe80227b4fa24d431
7aa34395a258f5893e3db1822139b8c1f04cfab9d757b9b9cca57e1df33d093f07c7f06e06bb6293676f9060a838ea138b6bc9f20b08afeb73120506e2ce7b9b9dcd9e4a421584cfaba2481132dfbdf4216e98e3facec9ba199ca3a97641e9ca9782868d0222a1d7c0d3119b867edaf2e72e2a6f7d344df39a14edc39cb6f960944ddac2aaef324827c36cba67dcb76b22119b43881a3f1262752990
7d8273ceb459e4d4386df4e32e1aecc1aa7aaafda50cb982f6c62623cf6b29693d86b15457aa76ac7e2eef6cf814ae3a8d39c7
```

Now this should be a pretty easy challenge as we got 2 encrypted messages, 1 we know the cleartext of and one we do not. <br/>
Knowing this we can use the keystream of the first message to get the second one using `XOR`. <br/>

We can do it by input the cleartext statement below into CyberChef. <br/>
```
Our counter agencies have intercepted your messages and a lot of your agent's identities have been exposed. In a matter of days all of them will be captured
```

Adding a `XOR` statement now and inputing the second hex string we got from `out.txt` we can actually recreate the correct keystream. <br/>
Now we can simply add another hex string which was encrypted by the same keystream and we get the actual output. <br/>

First `XOR`: <br/>
```
7aa34395a258f5893e3db1822139b8c1f04cfab9d757b9b9cca57e1df33d093f07c7f06e06bb6293676f9060a838ea138b6bc9f20b08afeb73120506e2ce7b9b9dcd9e4a421584cfaba2481132dfbdf4216e98e3facec9ba199ca3a97641e9ca9782868d0222a1d7c0d3119b867edaf2e72e2a6f7d344df39a14edc39cb6f960944ddac2aaef324827c36cba67dcb76b22119b43881a3f1262752990
```


Second `XOR`: <br/>
```
7d8273ceb459e4d4386df4e32e1aecc1aa7aaafda50cb982f6c62623cf6b29693d86b15457aa76ac7e2eef6cf814ae3a8d39c7
```

Having inputed those two we can see the actual flag in the output field. <br/>
```
HTB{REDACTED}
---------------------
```