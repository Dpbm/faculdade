#include <stdio.h>

void f(int *a){
        if(a == NULL)
        	return;

	printf("%d\n", *a);

}

int main(){
        int a = 1;
        f(&a);
        return 0;
}
