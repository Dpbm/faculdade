#include <stdio.h>

void swap(int *a, int *b){
  int c = *a;
  *a = *b;
  *b = c;
}

int main(){

  int a = 3;
  int b = 10;


  printf("Valor de a: %d, valor de b: %d\n", a, b);

  swap(&a, &b);

  printf("Valor de a: %d, valor de b: %d\n", a, b);

  return 0;
}
