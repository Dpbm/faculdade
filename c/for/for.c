#include <stdio.h>

int main() {
  int num;
  int i = 0;

  scanf("%d", &num);
  printf("\n");

  while (i <= 10) {
    printf("%d x %d = %d", i, num, i * num);
    i++;
  }

  return 0;
}
