#include <stdio.h>
#include <stdlib.h>

int main() {
  char *a = malloc(10 * sizeof(char));

  scanf("%s", a);

  for (int i = 0; i < 20; i++)
    printf("%p %c\n", a + i, *(a + i));

  return 0;
}
