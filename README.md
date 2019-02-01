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

# Credit
Mr.Un1k0d3r RingZer0 Team
