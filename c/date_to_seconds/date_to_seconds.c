#include <stdio.h>

int main() {
  int days, hours, minutes;
  long seconds;

  printf("Dias - Horas - Minutos - Segundos\n");
  scanf("%d %d %d %ld", &days, &hours, &minutes, &seconds);

  printf("%d dias %d horas %d minutos %ld segundos\n", days, hours, minutes,
         seconds);

  seconds += days * 24 * 60 * 60;
  seconds += hours * 60 * 60;
  seconds += minutes * 60;

  printf("Total em segundos: %ld", seconds);

  return 0;
}
