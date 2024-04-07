line_size db 10


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

  ; draw a pixel at x=100 y=100 color=red
  mov ah, 0Ch 
  mov al, 4
  mov cx, 100+line_size
  mov dx, 100+line_size
  int 10h

  mov bx, [line_size]
  dec bx
  mov [line_size], bx

  jmp loop

exit:
  mov ax, 3
  int 10h

  mov ax, 4C00h
  int 21h

