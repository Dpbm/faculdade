#include <stdio.h>

void f(int *a){
	if(a != NULL)
		printf("%d\n", *a);
	
}

int main(){
	int a = 1;
	f(&a);
	return 0;
}
