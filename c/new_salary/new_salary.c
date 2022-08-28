#include <stdio.h>

int main() {
  float salary, percentage, new_salary;

  printf("Salário: ");
  scanf("%f", &salary);

  printf("\nReajuste: ");
  scanf("%f", &percentage);

  new_salary = salary * (1 + (percentage / 100));

  printf("\nNovo salário com um reajuste de %.2f é %.2f", percentage,
         new_salary);

  return 0;
}
