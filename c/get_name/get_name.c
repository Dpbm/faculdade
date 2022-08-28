#include <stdio.h>

int main() {
  char name[30];

  printf("Nome do seu colega: ");
  scanf("%30[A-Za-z ]s", &name);
  printf("\nEae %s", name);

  return 0;
}
