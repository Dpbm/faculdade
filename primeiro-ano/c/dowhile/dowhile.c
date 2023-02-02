#include <stdio.h>

int main() {

  int sum = 0;
  int input;

  do {
    scanf("%d", &input);
    sum += input;
  } while (input != 0);

  printf("A soma de todos os números são --> %d", sum);

  return 0;
}
