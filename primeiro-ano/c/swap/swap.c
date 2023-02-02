#include <stdio.h>
#include <stdlib.h>

void swap(int *a, int *b) {
  printf("\n\n%p %p\n", a, b);
  int temp = *a;
  *a = *b;
  *b = temp;
}

int main() {
  int a = 20;
  int b = 12;

  printf("a: %d\nb: %d\n\n", a, b);

  int temp = a;
  a = b;
  b = temp;

  printf("a: %d\nb: %d\n", a, b);

  int *prta = &a;
  int *prtb = &b;

  swap(prta, prtb);

  printf("a: %d\nb: %d\n", a, b);
  printf("\n\n%p %p %p %p\n\n", &a, &b, prta, prtb);

  return 0;
}
