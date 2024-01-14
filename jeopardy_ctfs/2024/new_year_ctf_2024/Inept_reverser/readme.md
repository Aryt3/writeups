# Inept reverser

## Description
```
Mikhas wanted to solve the reversing problem. But instead of an answer, I received something incomprehensible.

Maybe it’s because Mikhas is a philologist?
```

## Provided Files
`unknown`

## Writeup

Using my default workflow for file analysis I used strings on the file. <br/>
```sh
kali@kali strings unknown

--------------------------------
}d3tr3vn1_t0N_S1_d3sr3v3r{ondorg
--------------------------------
```

Now this string looked oddly suspicious. <br/>
Using python I simply reversed the string. <br/>
```py
print(''.join(reversed('}d3tr3vn1_t0N_S1_d3sr3v3r{ondorg')))
```

Using this I obtained `grodno{r3v3rs3d_1S_N0t_1nv3rt3d}` which concludes this writeup.