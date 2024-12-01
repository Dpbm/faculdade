main:
	addi sp, sp, -16
	sb ra, 0(sp)

	li s2, 255
	li s3, 1033


	sb s2, 1(sp)
	sh s3, 2(sp)