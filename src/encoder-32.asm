BITS 32

global _start

section .text

_start:
        call $ + 5
        pop ebx
        xor eax, eax
        mov ecx, eax
        mov cx, 256
        add ebx, 18
_loop:
        not DWORD [ebx + ecx * 4]
        loop _loop
        add ebx, 4
        push ebx
        ret
