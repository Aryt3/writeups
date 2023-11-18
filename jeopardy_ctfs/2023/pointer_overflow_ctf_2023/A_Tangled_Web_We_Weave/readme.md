# A Tangled Web We Weave

## Description
```
The flag has been hidden in these assembly instructions, except I forgot how to decode it... If you figure it out you get the flag.
```

## Provided Files
`re2.asm`

## Writeup

Taking a look at the provided script. <br/>
```asm
section .data
    encoded_message db 0x0F, 0x10, 0x1C, 0x0B, 0x19, 0x04, 0x0A, 0x08, 0x0C, 0x0F, 0x20, 0x14, 0x4E, 0x11, 0x46, 0x20, 0x14, 0x4F, 0x11, 0x46, 0x20, 0x46, 0x4F, 0x48, 0x20, 0x11, 0x4F, 0x48, 0x17, 0x4E, 0x11, 0x46, 0x20, 0x4F, 0x11, 0x20, 0x12, 0x4C, 0x02

section .text
    global _start

_start:
    mov ecx, 0
    mov edi, encoded_message
    find_length:
        cmp byte [edi], 0
        je print_message
        inc ecx
        inc edi
        jmp find_length

    print_message:
        xor esi, esi
        mov edi, encoded_message
        decode:
            xor eax, eax
            mov al, byte [edi + esi]
            xor al, ; something missing?
            mov byte [edi + esi], al
            inc esi
            cmp byte [edi + esi], 0
            jne decode

        mov edx, ecx
        mov eax, 4
        mov ebx, 1
        mov ecx, encoded_message
        int 0x80

    mov eax, 1
    xor ebx, ebx
    int 0x80
```

Looking at this assembly code we can instantly see the comment `; something missing?`. <br/>
The comment probably means that the `xor` is missing an operand because xor only works with 2 operands. <br/>
Also after reading the code some more I understood that this `xor` is used for convertion. <br/>
After a little research I found that to convert ASCII-encoded decimal digits to their corresponding numeric values I would need the operand `0x30`. <br/>
Knowing this I changed the line to `xor al, 0x30`. <br/>

Using an online interpreter I execute the code. (https://onecompiler.com/assembly/3ztdysdgq) <br/>
The output seems to be the following `? ,;)4:8<?$~!v$!vvx!x'~!v!"|2`. <br/>
At first it looked like nonsense but using the magic module from CyberChef we actually got a result. <br/>
Seems like it was another XOR `poctf{REDACTED}`.

