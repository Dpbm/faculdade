#include <stdio.h>

int main() {
  float price, consumption, distance;

  printf("price per liter - consumption - distance\n");
  scanf("%f %f %f", &price, &consumption, &distance);

  float total_liters = distance / consumption;
  float total_price = total_liters * price;

  printf("total spent R$ %.2f by %.2fL", total_price, total_liters);

  return 0;
}
