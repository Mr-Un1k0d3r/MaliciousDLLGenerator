BITS 64

global _start

section .text

_start:
        call $ + 5
        pop rbx
        xor rax, rax
        mov rcx, rax
        mov cl, 128
        add rbx, 16
_loop:
        not QWORD [rbx + rcx * 8]
        loop _loop
        add rbx, 8
        push rbx
        ret
