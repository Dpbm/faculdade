#include <stdio.h>

int main(){
  int *p;
  int a = 45;

  p = &a;

  printf("%x\n", p);

  *p = 23;

  printf("%x, %d\n", p, *p);
}
