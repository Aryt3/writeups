# Mind your Ps and Qs

## Description
```
In RSA, a small e value can be problematic, but what about N? Can you decrypt this?
```

## Provided Files
```
- values
```

## Writeup

We should start off by taking a look at the provided file. <br/>
```
Decrypt my super sick RSA:
c: 421345306292040663864066688931456845278496274597031632020995583473619804626233684
n: 631371953793368771804570727896887140714495090919073481680274581226742748040342637
e: 65537
```

Now if we take a look at the provided values we can see that `N` is relatively small for a `public key value` in `RSA`. <br/>
The concern with small values of `N` lies in the existence of databases containing precomputed values for such cases. It is crucial to recognize that deriving `p` and `q` should pose a computationally challenging problem, as their factorization needs to be difficult to ensure the security of RSA encryption. <br/>
Knowing that we can search for a online tool which has integrated such a database. <br/>
One good webtool for such purpose is https://www.dcode.fr/rsa-cipher. Not only does this platform provide help to crack `RSA`, it does also provide a huge variety of analysis engines and other useful tools. <br/>
Entering the values of the file into the online tool we are able to obtain the flag `picoCTF{sma11_N_n0_g0od_55304594}` which concludes this writeup.  