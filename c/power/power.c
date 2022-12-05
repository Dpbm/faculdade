#include <math.h>
#include <stdio.h>

int main() {
  int a, b;

  scanf("%d %d", &a, &b);

  int total = pow(a, 2) + pow(b, 2);

  printf("Soma do quadrado --> %d", total);
  return 0;
}
