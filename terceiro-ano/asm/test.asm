loop:
  ;read from keyboard
  ;mov ah, 0h
  xor ah, ah
  int 16h

  ; scape key pressed
  cmp ah, 1
  je exit ;end game

  jmp draw

draw:

  ;vga mode
  mov ax, 13h
  ;mov ah, 0h
  xor ah, ah
  int 10h

  mov edi, 0A0000h
  mov al, 4h ;color of the pixel
  mov [edi], al
  
  mov edi, 0A0001h
  mov al, 4h ;color of the pixel
  mov [edi], al


  mov edi, 0A0002h
  mov al, 4h ;color of the pixel
  mov [edi], al

  jmp loop

exit:
  mov ah, 2
  int 3
  ret
