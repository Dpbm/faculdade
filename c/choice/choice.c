#include <stdio.h>

void printit(int a, int b) {
  if (a > b) {
    printf("%d %d", b, a);
    return;
  }

  printf("%d %d", a, b);
}

int main() {
  int a, b;
  scanf("%d %d", &a, &b);

  printit(a, b);

  return 0;
}
