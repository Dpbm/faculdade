#include <stdio.h>

struct Number {
  int real;
  int complex;
}

int main(){
  struct Number n1, n2;

  printf("First Complex number: ");
  scanf("%d %d*c", &n1.real, &n1.complex);

  printf("\nSecond Complex number: ");
  scanf("%d %d*c", &n2.real, &n2.complex);

  int real_part_sum = n1.real + n2.real;
  int complex_part_sum = n1.complex + n2.complex;

  char complex_signal = "-";

  if (complex_part_sum >= 0)
    complex_signal = "+";

  printf("%d %c %d", real_part_sum, complex_signal, complex_part_sum);
}
