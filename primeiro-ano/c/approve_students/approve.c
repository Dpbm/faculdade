#include <stdio.h>

int main() {
  float a, b;
  int lessons, absences;

  scanf("%f %f %d %d", &a, &b, &lessons, &absences);

  if (((a + b) / 2 >= 7) && (((lessons - absences) * 100) / lessons >= 75)) {
    printf("Approved!");
    return 0;
  }

  printf("Disapproved!");
  return 0;
}
