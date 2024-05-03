main:
  li s4, 1
  slti s2, s4, 0

  li s6,1
  xori s3, s6, -1
  xori s3, s3, -1
  xori s3, s3, -1

  li s5, 1
  slli s5, s5, 2
  srli s5, s5, 1

  lw s7, 3(s5)
  lw s10, 2(ra)

  addi sp, sp, -12
  sw s5, 8(sp)
  lw s8, 8(sp)
  addi sp, sp, 12

  addi s11, s7, 0
