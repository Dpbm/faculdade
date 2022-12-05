#include <stdio.h>

void getClassification(int age) {
  if (age >= 5 && age <= 7)
    printf("Infantil A");
  else if (age >= 8 && age <= 11)
    printf("Infantil B");
  else if (age >= 12 && age <= 13)
    printf("Juvenil A");
  else if (age >= 14 && age <= 17)
    printf("Juvenil B");
  else if (age >= 18)
    printf("Adultos");
  else
    printf("Nenhum!");
}

int main() {
  int age;

  scanf("%d", &age);

  getClassification(age);

  return 0;
}
