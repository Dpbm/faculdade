_inc:
	li t1,0
	lbu t1, 0(sp)
	addi t1, t1, 1

	addi sp, sp, -1
	sb t1, 0(sp)

	bne t1, s3, _inc
	jr ra


main:

	li s3, 255
	li t1, 0

	addi sp, sp, -1
	sb t1, 0(sp)

	call _inc

	li t1, 0
	li s3, 0
