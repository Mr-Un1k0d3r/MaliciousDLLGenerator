BITS 64

global _start

section .text:

_start:
	call $ + 5
	pop rbx
	xor rax, rax
	mov rcx, rax
	mov ax, 1024
	mov cl, 128
	add rbx, 25
_loop:
	neg QWORD [rbx + rcx * 8]
	loop _loop
	push rbx
	ret
 	db 0x11, 0x22

