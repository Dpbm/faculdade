fac:
    addi s0, s0, 1

main:
    addi a0, a0, 3
    addi sp, sp, -16

    sw ra, 0(sp)

    call fac

    addi sp, sp, 16