#include <stdio.h>
#include <stdlib.h>

void test(){
	printf("Test\n");
}

void test2(void func(void)){
	func();
}

int main(){
	test2(test);
	exit(EXIT_SUCCESS);
}
