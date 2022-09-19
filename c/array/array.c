#include <stdio.h>

int main() {
  int A[10], B[10], calc_value;

  for (int i = 0; i < 10; i++)
    scanf("%d", &A[i]);

  printf("Valor para calculo: ");
  scanf("%d", &calc_value);

  for (int i = 0; i < 10; i++)
    B[i] = A[i] + calc_value;

  printf("A --> ");
  for (int i = 0; i < 10; i++)
    printf("%d ", A[i]);

  printf("\nB --> ");
  for (int i = 0; i < 10; i++)
    printf("%d", B[i]);

  return 0;
}
