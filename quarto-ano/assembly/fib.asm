section .text

    global _main

    _main:
        mov eax, 0x4
        mov ebx, 0x1
        mov ecx, 0x39
        mov edx, 1
        int 0x80

        mov eax, 0x1
        xor ebx, ebx
        int 0x80