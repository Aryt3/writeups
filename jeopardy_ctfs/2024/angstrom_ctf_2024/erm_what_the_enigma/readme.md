# erm what the enigma

## Description
```
In the dimly lit, smoke-filled war room, the Enigma M3 machine sat at the center of the table like a cryptographic sentinel. 
Its reflector, UKW B, gleamed ominously in the low light. 
The three rotors, I, II, and III, stood proudly in their respective slots, each at position 1 with their rings set to 1. 
The plugboard, conspicuously vacant, indicated a reliance on the rotor settings alone to encode the day's crucial messages. 
As the operator's fingers hovered over the keys, the silence was heavy with anticipation. 
Each clack of the keys transformed plaintext into an unbreakable cipher, the resulting ciphertext, brht{d_imhw_cexhrmwyy_lbvkvqcf_ldcz}, a guardian of wartime secrets.
```

## Writeup

After reading the description I made a quick searched for `engima decrypter` which lead me to [dcode](https://www.dcode.fr/enigma-machine-cipher). <br/>
Entering the `ciphertext brht{d_imhw_cexhrmwyy_lbvkvqcf_ldcz}` from the description I obtained `ACTFILOVEENIGMATICMACHINESMWAH` which is the flag `actf{i_love_enigmatic_machines_mwah}`.
