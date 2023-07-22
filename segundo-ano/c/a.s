	.file	"his_tree.c"
	.section .rdata,"dr"
.LC0:
	.ascii "Valor: \0"
.LC1:
	.ascii "%d\0"
	.text
	.globl	CAPB
	.def	CAPB;	.scl	2;	.type	32;	.endef
	.seh_proc	CAPB
CAPB:
	pushq	%rbp
	.seh_pushreg	%rbp
	movq	%rsp, %rbp
	.seh_setframe	%rbp, 0
	subq	$48, %rsp
	.seh_stackalloc	48
	.seh_endprologue
	movl	%ecx, 16(%rbp)
	cmpl	$0, 16(%rbp)
	jne	.L2
	movq	$0, -8(%rbp)
	jmp	.L3
.L2:
	movl	$24, %edx
	movl	$1, %ecx
	call	calloc
	movq	%rax, -8(%rbp)
	leaq	.LC0(%rip), %rcx
	call	printf
	movq	-8(%rbp), %rax
	addq	$8, %rax
	movq	%rax, %rdx
	leaq	.LC1(%rip), %rcx
	call	scanf
	movl	16(%rbp), %eax
	movl	%eax, %edx
	shrl	$31, %edx
	addl	%edx, %eax
	sarl	%eax
	movl	%eax, %ecx
	call	CAPB
	movq	%rax, %rdx
	movq	-8(%rbp), %rax
	movq	%rdx, (%rax)
	movl	16(%rbp), %eax
	movl	%eax, %edx
	shrl	$31, %edx
	addl	%edx, %eax
	sarl	%eax
	movl	%eax, %edx
	movl	16(%rbp), %eax
	subl	%edx, %eax
	subl	$1, %eax
	movl	%eax, %ecx
	call	CAPB
	movq	%rax, %rdx
	movq	-8(%rbp), %rax
	movq	%rdx, 16(%rax)
.L3:
	movq	-8(%rbp), %rax
	addq	$48, %rsp
	popq	%rbp
	ret
	.seh_endproc
	.globl	Imprime
	.def	Imprime;	.scl	2;	.type	32;	.endef
	.seh_proc	Imprime
Imprime:
	pushq	%rbp
	.seh_pushreg	%rbp
	movq	%rsp, %rbp
	.seh_setframe	%rbp, 0
	subq	$32, %rsp
	.seh_stackalloc	32
	.seh_endprologue
	movq	%rcx, 16(%rbp)
	cmpq	$0, 16(%rbp)
	je	.L5
	movq	16(%rbp), %rax
	movl	8(%rax), %eax
	movl	%eax, %edx
	leaq	.LC1(%rip), %rcx
	call	printf
	movq	16(%rbp), %rax
	movq	(%rax), %rax
	movq	%rax, %rcx
	call	Imprime
	movq	16(%rbp), %rax
	movq	16(%rax), %rax
	movq	%rax, %rcx
	call	Imprime
	nop
.L5:
	addq	$32, %rsp
	popq	%rbp
	ret
	.seh_endproc
	.section .rdata,"dr"
.LC2:
	.ascii "-%d-\0"
	.text
	.globl	Folhas
	.def	Folhas;	.scl	2;	.type	32;	.endef
	.seh_proc	Folhas
Folhas:
	pushq	%rbp
	.seh_pushreg	%rbp
	movq	%rsp, %rbp
	.seh_setframe	%rbp, 0
	subq	$32, %rsp
	.seh_stackalloc	32
	.seh_endprologue
	movq	%rcx, 16(%rbp)
	cmpq	$0, 16(%rbp)
	jne	.L8
	jmp	.L7
.L8:
	movq	16(%rbp), %rax
	movq	(%rax), %rax
	testq	%rax, %rax
	jne	.L10
	movq	16(%rbp), %rax
	movq	16(%rax), %rax
	testq	%rax, %rax
	jne	.L10
	movq	16(%rbp), %rax
	movl	8(%rax), %eax
	movl	%eax, %edx
	leaq	.LC2(%rip), %rcx
	call	printf
.L10:
	movq	16(%rbp), %rax
	movq	(%rax), %rax
	movq	%rax, %rcx
	call	Folhas
	movq	16(%rbp), %rax
	movq	16(%rax), %rax
	movq	%rax, %rcx
	call	Folhas
	nop
.L7:
	addq	$32, %rsp
	popq	%rbp
	ret
	.seh_endproc
	.section .rdata,"dr"
.LC3:
	.ascii "%d \0"
	.text
	.globl	Descendentes_Diretos
	.def	Descendentes_Diretos;	.scl	2;	.type	32;	.endef
	.seh_proc	Descendentes_Diretos
Descendentes_Diretos:
	pushq	%rbp
	.seh_pushreg	%rbp
	movq	%rsp, %rbp
	.seh_setframe	%rbp, 0
	subq	$32, %rsp
	.seh_stackalloc	32
	.seh_endprologue
	movq	%rcx, 16(%rbp)
	movl	%edx, 24(%rbp)
	cmpq	$0, 16(%rbp)
	jne	.L12
	jmp	.L11
.L12:
	movq	16(%rbp), %rax
	movl	8(%rax), %eax
	cmpl	24(%rbp), %eax
	jne	.L14
	movq	16(%rbp), %rax
	movq	(%rax), %rax
	testq	%rax, %rax
	je	.L15
	movq	16(%rbp), %rax
	movq	(%rax), %rax
	movl	8(%rax), %eax
	movl	%eax, %edx
	leaq	.LC3(%rip), %rcx
	call	printf
.L15:
	movq	16(%rbp), %rax
	movq	16(%rax), %rax
	testq	%rax, %rax
	je	.L16
	movq	16(%rbp), %rax
	movq	16(%rax), %rax
	movl	8(%rax), %eax
	movl	%eax, %edx
	leaq	.LC1(%rip), %rcx
	call	printf
.L16:
	movl	$10, %ecx
	call	putchar
.L14:
	movq	16(%rbp), %rax
	movq	(%rax), %rax
	movl	24(%rbp), %edx
	movq	%rax, %rcx
	call	Descendentes_Diretos
	movq	16(%rbp), %rax
	movq	16(%rax), %rax
	movl	24(%rbp), %edx
	movq	%rax, %rcx
	call	Descendentes_Diretos
	nop
.L11:
	addq	$32, %rsp
	popq	%rbp
	ret
	.seh_endproc
	.globl	Descendentes
	.def	Descendentes;	.scl	2;	.type	32;	.endef
	.seh_proc	Descendentes
Descendentes:
	pushq	%rbp
	.seh_pushreg	%rbp
	movq	%rsp, %rbp
	.seh_setframe	%rbp, 0
	subq	$32, %rsp
	.seh_stackalloc	32
	.seh_endprologue
	movq	%rcx, 16(%rbp)
	movl	%edx, 24(%rbp)
	cmpq	$0, 16(%rbp)
	jne	.L18
	jmp	.L17
.L18:
	movq	16(%rbp), %rax
	movl	8(%rax), %eax
	cmpl	24(%rbp), %eax
	jne	.L20
	movq	16(%rbp), %rcx
	call	Imprime
	jmp	.L17
.L20:
	movq	16(%rbp), %rax
	movq	(%rax), %rax
	movl	24(%rbp), %edx
	movq	%rax, %rcx
	call	Descendentes
	movq	16(%rbp), %rax
	movq	16(%rax), %rax
	movl	24(%rbp), %edx
	movq	%rax, %rcx
	call	Descendentes
	nop
.L17:
	addq	$32, %rsp
	popq	%rbp
	ret
	.seh_endproc
	.section .rdata,"dr"
.LC4:
	.ascii " %d \0"
	.text
	.globl	In_Order
	.def	In_Order;	.scl	2;	.type	32;	.endef
	.seh_proc	In_Order
In_Order:
	pushq	%rbp
	.seh_pushreg	%rbp
	movq	%rsp, %rbp
	.seh_setframe	%rbp, 0
	subq	$32, %rsp
	.seh_stackalloc	32
	.seh_endprologue
	movq	%rcx, 16(%rbp)
	cmpq	$0, 16(%rbp)
	jne	.L22
	jmp	.L21
.L22:
	movq	16(%rbp), %rax
	movq	(%rax), %rax
	movq	%rax, %rcx
	call	In_Order
	movq	16(%rbp), %rax
	movl	8(%rax), %eax
	movl	%eax, %edx
	leaq	.LC4(%rip), %rcx
	call	printf
	movq	16(%rbp), %rax
	movq	16(%rax), %rax
	movq	%rax, %rcx
	call	In_Order
	nop
.L21:
	addq	$32, %rsp
	popq	%rbp
	ret
	.seh_endproc
	.globl	Pre_Order
	.def	Pre_Order;	.scl	2;	.type	32;	.endef
	.seh_proc	Pre_Order
Pre_Order:
	pushq	%rbp
	.seh_pushreg	%rbp
	movq	%rsp, %rbp
	.seh_setframe	%rbp, 0
	subq	$32, %rsp
	.seh_stackalloc	32
	.seh_endprologue
	movq	%rcx, 16(%rbp)
	cmpq	$0, 16(%rbp)
	jne	.L25
	jmp	.L24
.L25:
	movq	16(%rbp), %rax
	movl	8(%rax), %eax
	movl	%eax, %edx
	leaq	.LC4(%rip), %rcx
	call	printf
	movq	16(%rbp), %rax
	movq	(%rax), %rax
	movq	%rax, %rcx
	call	Pre_Order
	movq	16(%rbp), %rax
	movq	16(%rax), %rax
	movq	%rax, %rcx
	call	Pre_Order
	nop
.L24:
	addq	$32, %rsp
	popq	%rbp
	ret
	.seh_endproc
	.globl	Pos_Order
	.def	Pos_Order;	.scl	2;	.type	32;	.endef
	.seh_proc	Pos_Order
Pos_Order:
	pushq	%rbp
	.seh_pushreg	%rbp
	movq	%rsp, %rbp
	.seh_setframe	%rbp, 0
	subq	$32, %rsp
	.seh_stackalloc	32
	.seh_endprologue
	movq	%rcx, 16(%rbp)
	cmpq	$0, 16(%rbp)
	jne	.L28
	jmp	.L27
.L28:
	movq	16(%rbp), %rax
	movq	(%rax), %rax
	movq	%rax, %rcx
	call	Pre_Order
	movq	16(%rbp), %rax
	movq	16(%rax), %rax
	movq	%rax, %rcx
	call	Pre_Order
	movq	16(%rbp), %rax
	movl	8(%rax), %eax
	movl	%eax, %edx
	leaq	.LC4(%rip), %rcx
	call	printf
	nop
.L27:
	addq	$32, %rsp
	popq	%rbp
	ret
	.seh_endproc
	.def	__main;	.scl	2;	.type	32;	.endef
	.globl	main
	.def	main;	.scl	2;	.type	32;	.endef
	.seh_proc	main
main:
	pushq	%rbp
	.seh_pushreg	%rbp
	movq	%rsp, %rbp
	.seh_setframe	%rbp, 0
	subq	$48, %rsp
	.seh_stackalloc	48
	.seh_endprologue
	call	__main
	movq	$0, -8(%rbp)
	movl	$7, %ecx
	call	CAPB
	movq	%rax, -8(%rbp)
	movq	-8(%rbp), %rax
	movq	%rax, %rcx
	call	In_Order
	movl	$10, %ecx
	call	putchar
	movq	-8(%rbp), %rax
	movq	%rax, %rcx
	call	Pre_Order
	movl	$10, %ecx
	call	putchar
	movq	-8(%rbp), %rax
	movq	%rax, %rcx
	call	Pos_Order
	movl	$0, %eax
	addq	$48, %rsp
	popq	%rbp
	ret
	.seh_endproc
	.ident	"GCC: (tdm64-1) 4.9.2"
	.def	calloc;	.scl	2;	.type	32;	.endef
	.def	printf;	.scl	2;	.type	32;	.endef
	.def	scanf;	.scl	2;	.type	32;	.endef
	.def	putchar;	.scl	2;	.type	32;	.endef
