#include <stdio.h>

const int rows = 7;
const int columns = 3;

int main() {
  int A[rows][columns];

  for (int i = 0; i < rows; i++) {
    for (int j = 0; j < columns; j++) {
      printf("Valor da posição %d %d", i, j);
      scanf("%d", &A[i][j]);
    }
  }

  printf("\n");
  for (int i = 0; i < rows; i++) {
    for (int j = 0; j < columns; j++) {
      printf("%d ", A[i][j]);
    }
    printf("\n");
  }

  return 0;
}
