# Switcher

## Description
```
It's incredible how completely indiscernible the functions are...
```

## Provided Files
```
- switcher
```

## Writeup

Starting off I inspected the binary but quickly found out that it would be kind of hard as it was stripped. <br/>
```sh
$ file switcher 
switcher: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=de318112ee9931cda68cd586f6381aa9e0abdaa1, for GNU/Linux 3.2.0, stripped
```

Knowing that I wouldn't get far with `gdb` or `ghidra` I turned to other decompilers. <br/>
Using [dogbolt](https://dogbolt.org/?id=d10a6ee2-735a-4184-8a68-34318701c255#BinaryNinja=204&Hex-Rays=180) I was successfully able to decompile an important part of the binary. <br/>
```c
 if ( *a1 == 106 )
  {
    v36 = a1 + 1;
    if ( *v36 == 117 )
    {
      v35 = v36 + 1;
      if ( *v35 == 109 )
      {
        v34 = v35 + 1;
        if ( *v34 == 112 )
        {
          v33 = v34 + 1;
          if ( *v33 == 105 )
          {
            v32 = v33 + 1;
            if ( *v32 == 110 )
            {
              v31 = v32 + 1;
              if ( *v31 == 103 )
              {
                v30 = v31 + 1;
                if ( *v30 == 95 )
                {
                  v29 = v30 + 1;
                  if ( *v29 == 109 )
                  {
                    v28 = v29 + 1;
                    if ( *v28 == 121 )
                    {
                      v27 = v28 + 1;
                      if ( *v27 == 95 )
                      {
                        v26 = v27 + 1;
                        if ( *v26 == 119 )
                        {
                          v25 = v26 + 1;
                          if ( *v25 == 97 )
                          {
                            v24 = v25 + 1;
                            if ( *v24 == 121 )
                            {
                              v23 = v24 + 1;
                              if ( *v23 == 95 )
                              {
                                v22 = v23 + 1;
                                if ( *v22 == 116 )
                                {
                                  v21 = v22 + 1;
                                  if ( *v21 == 111 )
                                  {
                                    v20 = v21 + 1;
                                    if ( *v20 == 95 )
                                    {
                                      v19 = v20 + 1;
                                      if ( *v19 == 116 )
                                      {
                                        v18 = v19 + 1;
                                        if ( *v18 == 104 )
                                        {
                                          v17 = v18 + 1;
                                          if ( *v17 == 101 )
                                          {
                                            v16 = v17 + 1;
                                            if ( *v16 == 95 )
                                            {
                                              v15 = v16 + 1;
                                              if ( *v15 == 102 )
                                              {
                                                v14 = v15 + 1;
                                                if ( *v14 == 108 )
                                                {
                                                  v13 = v14 + 1;
                                                  if ( *v13 == 97 )
                                                  {
                                                    v12 = v13 + 1;
                                                    if ( *v12 == 103 )
                                                    {
                                                      v11 = v12 + 1;
                                                      if ( *v11 == 95 )
                                                      {
                                                        v10 = v11 + 1;
                                                        if ( *v10 == 111 )
                                                        {
                                                          v9 = v10 + 1;
                                                          if ( *v9 == 110 )
                                                          {
                                                            v8 = v9 + 1;
                                                            if ( *v8 == 101 )
                                                            {
                                                              v7 = v8 + 1;
                                                              if ( *v7 == 95 )
                                                              {
                                                                v6 = v7 + 1;
                                                                if ( *v6 == 98 )
                                                                {
                                                                  v5 = v6 + 1;
                                                                  if ( *v5 == 121 )
                                                                  {
                                                                    v4 = v5 + 1;
                                                                    if ( *v4 == 95 )
                                                                    {
                                                                      v3 = v4 + 1;
                                                                      if ( *v3 == 111 )
                                                                      {
                                                                        v2 = v3 + 1;
                                                                        if ( *v2 == 110 )
                                                                        {
                                                                          v1 = v2 + 1;
                                                                          if ( *v1 == 101 )
                                                                            sub_1200(v1 + 1);
                                                                        }
// ------------------------------------------------------------------------------------------
```

Seeing these nested statements, I thought that I could derive the flag from the `if-clauses`. <br/>
Using a regex I obtained the numbers in the combination below. <br/>
```
106, 117, 109, 112, 105, 110, 103, 95, 109, 121, 95, 119, 97, 121, 95, 116, 111, 95, 116, 104, 101, 95, 102, 108, 97, 103, 95, 111, 110, 101, 95, 98, 121, 95, 111, 110, 101
```

Using [CyberChef](https://gchq.github.io/CyberChef/#recipe=Find_/_Replace(%7B'option':'Regex','string':','%7D,'',true,false,true,false)From_Decimal('Space',false)&input=MTA2LCAxMTcsIDEwOSwgMTEyLCAxMDUsIDExMCwgMTAzLCA5NSwgMTA5LCAxMjEsIDk1LCAxMTksIDk3LCAxMjEsIDk1LCAxMTYsIDExMSwgOTUsIDExNiwgMTA0LCAxMDEsIDk1LCAxMDIsIDEwOCwgOTcsIDEwMywgOTUsIDExMSwgMTEwLCAxMDEsIDk1LCA5OCwgMTIxLCA5NSwgMTExLCAxMTAsIDEwMQ) I then extracted the actual flag which concludes this writeup. 