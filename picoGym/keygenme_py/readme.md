# keygenme-py

## Provided Files
```
- keygenme-trial.py
```

## Writeup

Starting off, we should take a look at the provided file. <br/>
```py
# ---------------------------

username_trial = "ANDERSON"
bUsername_trial = b"ANDERSON"

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial

# ---------------------------

def check_key(key, username_trial):

    global key_full_template_trial

    if len(key) != len(key_full_template_trial):
        return False
    else:
        # Check static base key part --v
        i = 0
        for c in key_part_static1_trial:
            if key[i] != c:
                return False

            i += 1

        # TODO : test performance on toolbox container
        # Check dynamic part --v
        if key[i] != hashlib.sha256(username_trial).hexdigest()[4]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[5]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[3]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[6]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[2]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[7]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[1]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[8]:
            return False

        return True
```

Those are the pieces of the code we should be interested in because they contain the building of the flag and `if-cases` to check if we enter the correct `key`. <br/>

Looking at it piece by piece we can check the `if-cases`. <br/>
```py
if len(key) != len(key_full_template_trial):
    return False
```

First it seems to check if the key we submit is the same length as `picoCTF{1n_7h3_|<3y_of_xxxxxxxx}`. <br/>
```py
i = 0
for c in key_part_static1_trial:
    if key[i] != c:
        return False

    i += 1
```

After passing the first if case it basically checks if the first part of the flag `picoCTF{1n_7h3_|<3y_of_` equals the key from our input. <br/>
We can simply pass this `if-clause` if our flag starts with `picoCTF{1n_7h3_|<3y_of_`. <br/>
```py
if key[i] != hashlib.sha256(username_trial).hexdigest()[4]:
    return False
else:
    i += 1

if key[i] != hashlib.sha256(username_trial).hexdigest()[5]:
    return False
else:
    i += 1

if key[i] != hashlib.sha256(username_trial).hexdigest()[3]:
    return False
else:
    i += 1

if key[i] != hashlib.sha256(username_trial).hexdigest()[6]:
    return False
else:
    i += 1

if key[i] != hashlib.sha256(username_trial).hexdigest()[2]:
    return False
else:
    i += 1

if key[i] != hashlib.sha256(username_trial).hexdigest()[7]:
    return False
else:
    i += 1

if key[i] != hashlib.sha256(username_trial).hexdigest()[1]:
    return False
else:
    i += 1

if key[i] != hashlib.sha256(username_trial).hexdigest()[8]:
    return False
```

In this part it checks if we passed the correct middle part of the `key`. <br/>
We can simply reverse the result of those `if-clauses` and build the whole `key`(flag) with a small python script. <br/>
```py
import hashlib

# var extracted from original script
bUsername_trial = b"ANDERSON"

# parameters extracted from if-clauses
order = [4,5,3,6,2,7,1,8]

# define var to store results
key_part_dynamic1_trial = ""

# loop through if-clauses
for i in order:
    key_part_dynamic1_trial += hashlib.sha256(bUsername_trial).hexdigest()[i]

# print flag
print(f'picoCTF{{1n_7h3_|<3y_of_{key_part_dynamic1_trial}}}')
```

Running this script returns the key `picoCTF{1n_7h3_|<3y_of_01582419}`. <br/>
Using the key we can run the provided file `keygenme-trial.py` using the `key` above. <br/>
```sh
$ python3 keygenme-trial.py 

===============================================
Welcome to the Arcane Calculator, ANDERSON!

This is the trial version of Arcane Calculator.
The full version may be purchased in person near
the galactic center of the Milky Way galaxy. 
Available while supplies last!
=====================================================


___Arcane Calculator___

Menu:
(a) Estimate Astral Projection Mana Burn
(b) [LOCKED] Estimate Astral Slingshot Approach Vector
(c) Enter License Key
(d) Exit Arcane Calculator
What would you like to do, ANDERSON (a/b/c/d)? c

Enter your license key: picoCTF{1n_7h3_|<3y_of_01582419}

Full version written to 'keygenme.py'.

Exiting trial version...

===================================================

Welcome to the Arcane Calculator, tron!

===================================================
```

Seems like our `key` worked, which happens to be our `flag`. Verifying they `flag` concludes this writeup.  